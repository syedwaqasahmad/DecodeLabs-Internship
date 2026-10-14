print("====================================")
print("       RULE-BASED AI CHATBOT")
print("====================================")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")
print()

# Knowledge base: each key is a user input (intent), each value is the bot's reply
responses = {
    # Greetings
    "hello": "Hello! How can I help you?",
    "hi": "Hello! How can I help you?",
    "hey": "Hello! How can I help you?",
    "hii": "Hello! How can I help you?",
    # Name
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "your name": "I am a Rule-Based AI Chatbot.",
    # How are you
    "how are you": "I'm doing great! Thanks for asking.",
    "how are you doing": "I'm doing great! Thanks for asking.",
    # Help
    "help": "I can respond to predefined questions using rules.",
    "what can you do": "I can respond to predefined questions using rules.",
    # AI-related
    "what is ai": (
        "AI stands for Artificial Intelligence. "
        "It enables machines to perform tasks that normally require human intelligence."
    ),
    "define ai": (
        "AI stands for Artificial Intelligence. "
        "It enables machines to perform tasks that normally require human intelligence."
    ),
    # Thank you
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",
}

exit_commands = ["bye", "exit", "quit"]
fallback = "Sorry, I don't understand that. Please try another question."

while True:
    # Input + sanitization (handle case and whitespace)
    user_input = input("You: ").lower().strip()

    # Exit strategy
    if user_input in exit_commands:
        print("Bot: Goodbye! Have a great day!")
        break

    # Dictionary lookup with fallback in a single operation
    reply = responses.get(user_input, fallback)
    print("Bot:", reply)

print()
print("====================================")
print("       Chatbot session ended.")
print("====================================")
