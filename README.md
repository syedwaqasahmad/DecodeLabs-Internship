# DecodeLabs Project 1 - Rule-Based AI Chatbot

## Project
Artificial Intelligence - Project 1: Rule-Based AI Chatbot

## Objective
Create a simple rule-based chatbot that responds to predefined user inputs.

## Key Requirements
- Handle greetings and exit commands.
- Use if-else logic for responses.
- Run in a continuous loop.

## Logic Skeleton Checklist (Project 1 Specification)
- [x] **Input loop:** continuous `while True` cycle.
- [x] **Sanitization:** input is normalized with `.lower().strip()`.
- [x] **Knowledge base:** a dictionary with 5+ intents (greetings, name, how are you, help, AI definition, thanks).
- [x] **Fallback:** a default response for unknown input using `.get()`.
- [x] **Exit strategy:** `bye`, `exit`, or `quit` triggers a clean `break`.

## Project Structure
```
DecodeLabs_Project1_Rule_Based_AI_Chatbot/
|-- chatbot.py                  # Main chatbot program
|-- README.md                   # Project documentation
|-- screenshots/                # Sample runs of the chatbot
|   |-- 1_known_inputs.png
|   |-- 2_unknown_input.png
|   |-- 3_case_whitespace.png
|-- uml/
    |-- activity_diagram.png    # Program flow / loop logic
```

## UML Diagram
**Activity Diagram:** shows the program flow: welcome banner, dictionary setup, then the `while True` loop (read, sanitize, exit check, lookup, print) until an exit command is entered.

## Technologies
- Python 3
- Control flow (`while`, `if`, `break`)
- Dictionaries (hash maps) with the `.get()` method

## How to Run
1. Make sure Python 3 is installed.
2. Open a terminal in this project folder.
3. Run:

   ```
   python chatbot.py
   ```
4. Type messages such as:
   - hello
   - what is your name
   - how are you
   - what can you do
   - what is ai
   - thanks
   - bye

## Project Working
The chatbot follows the Input -> Process -> Output model:

1. **Input:** the user's message is read and sanitized (lowercased and
   stripped of extra whitespace).
2. **Process:** an `if` statement checks for exit commands. Otherwise the
   message is looked up in a dictionary of predefined responses.
3. **Output:** the matching reply is printed. If no rule matches, the
   dictionary's `.get()` method returns a default fallback message.

A `while True` loop keeps the conversation running until the user enters an
exit command, which ends the loop with `break`.

## Sample Run
```
You: hello
Bot: Hello! How can I help you?
You: tell me a joke
Bot: Sorry, I don't understand that. Please try another question.
You: bye
Bot: Goodbye! Have a great day!
```

## Project 1 Scope
This project intentionally uses explicit programmatic rules rather than
machine learning, matching the foundation phase described in the
DecodeLabs Project 1 training material. A dictionary lookup is used instead
of a long `if-elif` ladder because it is cleaner, easier to extend, and
runs in constant time regardless of how many rules are added.

## Possible Improvements
- Expand the dictionary with more intents.
- Add nested conditions for smarter responses.
- Give the bot a unique personality.
