# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").

When I first ran the game it looked fine on the surface but it had some clear problems once I started playing. The hints were completely backwards, so when I guessed a number that was too high it told me to go higher instead of lower. After winning a game and clicking New Game, the game would not let me play again because it still thought I had already won. Easy mode also only gave 6 attempts while Normal gave 8, which made Easy actually harder than Normal.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code as my main AI tool on this project. One example where AI was correct was when it pointed out that the New Game button was not resetting the status back to "playing", and I verified this by clicking New Game after winning and confirming I could actually play again. One example where AI was incorrect was when AI suggested moving the debug expander below the submit logic, which fixed the history delay but caused the expander to close after every guess. I had to ask for a follow up fix to add expanded=True to keep it open.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed by actually playing the game and reproducing the exact situation that caused the bug before. For example after fixing the hint bug I guessed a number higher than the secret and checked that it now said go lower. I also ran the existing pytest tests in tests/test_game_logic.py to make sure the logic functions still worked correctly after moving them to logic_utils.py. AI helped me understand that the tests were already written to import from logic_utils, which meant the tests would start passing once the functions were moved over.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because every time the user clicked a button Streamlit reruns the entire script from the top, and without session state the line that picks a random number just runs again and picks a new one. Think of it like refreshing a webpage where everything resets unless you save it somewhere. Session state is basically a place to store variables that survive those reruns, so the secret number stays the same between clicks. The fix was wrapping the secret number assignment in a check that only sets it if it does not already exist in session state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is manually reproducing the bug before and after a fix instead of just trusting that the code change looks right. Next time I work with AI I would describe the bug with more detail upfront. This project made me realize that AI generated code can look completely correct at first glance but still have subtle logic mistakes, so you always need to actually test it yourself.
