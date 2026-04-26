from agent import Agent

def main():
    print("Welcome to the Agentic Workflow Demo!")
    print("Type 'rag' to use retrieval-augmented summarization.")
    print("Type 'multistep' to see multi-step agent reasoning.")
    task = input("Enter a task for the agent: ")
    agent = Agent()
    if task.lower().startswith("rag"):
        query = input("Enter a query to search documents: ")
        result = agent.rag_summarize(query)
        print(f"Agent result: {result}")
    elif task.lower().startswith("multistep"):
        subtask = input("Enter a subtask for the agent: ")
        steps = agent.run_multistep(subtask)
        print("\n--- Multi-step Reasoning Trace ---")
        for i, (step, action, result) in enumerate(steps, 1):
            print(f"Step {i}: {step}")
            print(f"  Action: {action}")
            print(f"  Result: {result}\n")
    else:
        result = agent.run(task)
        print(f"Agent result: {result}")

if __name__ == "__main__":
    main()
