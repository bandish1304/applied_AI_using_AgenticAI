## Original Project: Game Glitch Investigator: The Impossible Guesser

This project began as a playful take on the classic number guessing game, built with Streamlit. The original goal was to challenge players to guess a secret number within a set number of attempts, with the app providing feedback and tracking their progress. However, the initial version was intentionally buggy—hints were misleading, the secret number kept changing, and the game logic was tangled with the UI, making it both a puzzle and a debugging exercise.

# Applied_AI_using_AgenticAI

This project builds on the lessons learned from Game Glitch Investigator: The Impossible Guesser, taking the debugging mindset and applying it to a more advanced, agentic AI workflow. Here, the focus shifts from fixing game logic to harnessing the power of AI agents for tasks like text summarization. By connecting the spirit of hands-on problem solving from the original game to real-world AI applications, this project shows how the skills you develop as a game investigator—like troubleshooting, critical thinking, and iterative improvement—are just as valuable when working with modern AI systems. In short, it’s about turning playful curiosity into practical expertise.

## Architecture Overview

The system architecture centers around a clear flow of information and responsibility. User input is handled through a Streamlit web interface, which passes queries to a retriever and an agent for processing. The agent performs the main AI tasks, such as summarization, and sends results to an evaluator or tester for validation. Human feedback and testing are integrated into the loop, ensuring that outputs are checked and improved before being presented back to the user. This design keeps the system transparent, interactive, and robust—combining automation with opportunities for human oversight and learning.



## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

##  Setup Instructions

Getting started is simple, even if you’re new to Python projects. Here’s how you can get everything up and running:

1. First, make sure you have Python 3.12 installed. If you’re not sure, run python --version in your terminal.
2. (Recommended) Set up a virtual environment to keep things tidy:
   - On Windows: python -m venv .venv312
   - Then activate it: .venv312\Scripts\activate
3. Install all the project’s dependencies by running:
   - pip install -r requirements.txt
4. To launch the main web app, use:
   - python -m streamlit run app.py
5. If you want to try out the agentic AI features (like text summarization), run:
   - python main.py
6. To check that everything works, you can run the tests:
   - pytest

If you hit any snags with missing packages or version issues, double-check that your virtual environment is active and you’ve installed everything from requirements.txt. That’s it—you’re ready to explore!

## Sample Interactions

Summarization (Agentic AI)
Input: summarize The quick brown fox jumps over the lazy dog. This sentence is often used to test typing or display fonts because it contains every letter of the English alphabet.
Output: The sentence "The quick brown fox jumps over the lazy dog" is commonly used for typing tests and font displays as it includes every letter of the alphabet.

Game Guess (Correct)
Input: (User enters guess: 42, secret number is 42)
Output: 🎉 Correct! You guessed the secret number in 3 attempts. Your score increases!

Game Guess (Incorrect, with Hint)
Input: (User enters guess: 30, secret number is 42)
Output: Too low! Try a higher number. Attempts left: 5

## Design Decisions

The project was designed to be both educational and practical. By starting with a deliberately buggy game, I wanted to encourage hands-on debugging and critical thinking—skills that are essential for real-world software development. The transition to an agentic AI workflow was a natural next step, showing how the same mindset applies to more advanced, modern systems.

I chose Streamlit for the user interface because it makes building interactive web apps in Python quick and accessible. The agentic AI features were built to be modular, so you can easily swap out or extend the AI components. One trade-off was keeping the code simple and readable for learning purposes, rather than optimizing for maximum performance or scalability. This way, the project remains approachable for newcomers, but still demonstrates best practices in structuring, testing, and iterating on code.

## Testing Summary

Testing the project revealed both successes and challenges. The agentic AI summarizer worked as expected after setting up the correct Python environment and matching dependency versions (especially transformers and torch). The Streamlit web UI ran smoothly for both the game and AI features once the environment was properly configured.

What didn’t work at first: The original game logic had intentional bugs—hints were misleading, and the secret number kept changing due to state mismanagement in Streamlit. There were also issues with missing imports and dependency mismatches, especially with torch and transformers. Attempting to rename folders while the app was running caused errors, and using the wrong virtual environment led to missing package errors.

What I learned: Always activate the correct virtual environment before installing or running anything. Matching dependency versions is crucial for AI libraries. Streamlit’s state management requires careful handling to avoid bugs. Iterative testing and refactoring, along with writing and running tests, made the debugging process much smoother. Clear documentation and modular code structure helped in quickly identifying and fixing issues.
## Reflection

Working on this project deepened my understanding of both AI and practical problem-solving. Debugging the original game highlighted how even simple logic errors can create confusing user experiences, and how important it is to separate concerns (like UI and logic) for maintainability. Transitioning to agentic AI reinforced the value of modular design and the need for careful dependency management—especially with rapidly evolving AI libraries.

I learned that building with AI is as much about setting up the right environment and tools as it is about writing code. Iterative testing, clear documentation, and a willingness to experiment and refactor are crucial. Most importantly, I saw how the skills used in debugging games—like curiosity, persistence, and structured thinking—are directly transferable to working with advanced AI systems. This project showed me that effective problem-solving in AI is a blend of technical know-how and a playful, investigative mindset.


## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [] Describe the game's purpose.
   The purpose of this game is to let the player guess a secret number within a limited number of attempts based on the selected difficulty. The app gives feedback after each guess and tracks attempts, score, and guess history.
- [] Detail which bugs you found.
   I found three main bugs: the hint direction was wrong which was "Too High" and "Too Low" feedback was misleading, game logic and UI logic were mixed together in one file, and state behavior around gameplay was inconsistent enough to make debugging harder.
- [] Explain what fixes you applied.
   I refactored core functions like get_range_for_difficulty, parse_guess, check_guess, update_score into logic_utils.py, updated app.py to import and use them, and fixed hint mapping so outcomes now match the correct "Go LOWER" or "Go HIGHER" message.

## 📸 Demo

- [ ] [![alt text](image.png)]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

## System Architecture Diagram

![System Architecture](assets/system_architecture.png)

This diagram shows the main components, data flow, and where human/testing is involved in the system.

## Reliability and Evaluation

Reliability is ensured through automated testing. I wrote unit tests for the core game logic and AI summarization functions using pytest. Running these tests after each change helps catch bugs early and ensures that key features work as expected. For example, all 5 out of 5 tests currently pass, confirming that the main logic and AI outputs are correct for typical cases.

## Portfolio Artifact

- **GitHub Repository:** [https://github.com/bandish1304/applied_AI_using_AgenticAI](https://github.com/bandish1304/applied_AI_using_AgenticAI)
- **Loom Video Walkthrough:** [https://www.loom.com/share/ca3d2a287485409998a9a5bd60053935](https://www.loom.com/share/ca3d2a287485409998a9a5bd60053935)

## Reflection: What This Project Says About Me as an AI Engineer

This project demonstrates my ability to approach AI development with curiosity, critical thinking, and a strong focus on reliability and ethics. I value clear code structure, thorough testing, and honest reflection on both the strengths and limitations of AI systems. My work shows that I am committed to building practical, responsible AI solutions while always being open to learning and improvement.








