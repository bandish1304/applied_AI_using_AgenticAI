import logging
from transformers import pipeline
from logic_utils import retrieve_documents


class Agent:
    """
    Agentic workflow class with text summarization, logging, and error handling.
    """
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(levelname)s %(message)s',
            handlers=[logging.StreamHandler()]
        )
        self.logger = logging.getLogger(__name__)
        try:
            self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            self.logger.info("Summarization pipeline loaded successfully.")
        except Exception as e:
            self.logger.error(f"Failed to load summarization pipeline: {e}")
            self.summarizer = None

    def plan(self, task):
        self.logger.info(f"Planning for task: {task}")
        if task.lower().startswith("summarize"):
            return ["summarize"]
        return ["act"]

    def act(self, step, data=None):
        self.logger.info(f"Acting on step: {step}")
        if step == "summarize" and data:
            if not self.summarizer:
                self.logger.error("Summarizer not available.")
                return "Summarizer not available."
            try:
                summary = self.summarizer(data, max_length=60, min_length=10, do_sample=False)
                self.logger.info("Summarization successful.")
                return summary[0]['summary_text']
            except Exception as e:
                self.logger.error(f"Summarization failed: {e}")
                return f"Summarization failed: {e}"
        return f"Executed step: {step}"

    def check(self, result):
        self.logger.info(f"Checking result: {result}")
        return bool(result and isinstance(result, str) and len(result) > 0)

    def run(self, task, data=None):
        self.logger.info(f"Running agent for task: {task}")
        plan = self.plan(task)
        for step in plan:
            if step == "summarize":
                if data is not None:
                    result = self.act(step, data)
                else:
                    text = input("Enter text to summarize: ")
                    result = self.act(step, text)
            else:
                result = self.act(step)
            if not self.check(result):
                self.logger.warning("Check failed, need to retry or revise plan.")
                return "Check failed, need to retry or revise plan."
        self.logger.info("Task completed successfully.")
        return result if plan[0] == "summarize" else "Task completed successfully."

    def summarize(self, text):
        """Convenience method for summarization, for testing and direct use."""
        return self.act("summarize", text)

    def rag_summarize(self, query, folder="documents"):
        """Retrieve relevant docs and summarize them with the query."""
        docs = retrieve_documents(query, folder)
        if not docs:
            return "No relevant documents found."
        combined = "\n".join([text for _, text in docs])
        return self.summarize(combined)

    # Agentic workflow enhancement: Multi-step reasoning with observable intermediate steps.
    def run_multistep(self, task, data=None, verbose=True):
        """
        Multi-step agentic workflow with observable intermediate steps.
        Returns a list of (step, action, result) tuples.
        """
        steps_log = []
        plan = self.plan(task)
        for step in plan:
            if verbose:
                print(f"[PLAN] Next step: {step}")
            if step == "summarize":
                if data is not None:
                    action = f"Summarize provided data"
                    result = self.act(step, data)
                else:
                    text = input("Enter text to summarize: ")
                    action = f"Summarize user input"
                    result = self.act(step, text)
            else:
                action = f"Act: {step}"
                result = self.act(step)
            steps_log.append((step, action, result))
            if verbose:
                print(f"[ACTION] {action}")
                print(f"[RESULT] {result}")
            if not self.check(result):
                if verbose:
                    print("[CHECK] Failed. Need to retry or revise plan.")
                steps_log.append(("check", "Check result", "Failed"))
                break
        if verbose:
            print("[COMPLETE] Task finished.")
        return steps_log
