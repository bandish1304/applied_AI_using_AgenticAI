# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.
so when I played noraml or hard version in both, it says go higher or lower(exactly the opposite) and I cannot start a new game. Looks like when I click the button for new game, nothing happens

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The Game was looking perfectly fine in the begi8nning but as i started running it the hint part was showing wrong.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The hints were backwards
  2. I cannot start a newgame when I press a new game button

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Github copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One correct AI suggestion was to move check_guess into a separate logic_utils module and compare guess and secret as numbers instead of mixing types
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One misleading AI suggestion was to rely on the original check_guess behavior that sometimes converted the secret number to a string and then compared values, which could produce wrong high-low hints

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was really fixed only after I could reproduce the old behavior first, apply a change, and then fail to reproduce the bug in repeated trie
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran pytest after each logic update, and one key test was the regression case for guess 9 vs secret 10, which showed the result stayed Too Low instead of flipping due to string-style comparison. 
- Did AI help you design or understand any tests? How?
  AI helped me design tests by suggesting focused input/output cases for check_guess.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because Streamlit reruns the whole script every time you click a button
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
I made the secret number persist in session state by initializing it only once and reusing it on every rerun, instead of recreating it during normal gameplay

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I want to reuse is writing a small regression test right after I fix a bug.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would give AI more specific prompts up front with exact requirements and expected outputs
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project taught me that AI-generated code is a useful starting point, but not something I should trust without testing
