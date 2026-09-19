import random

RESPONSES = {
    "hello": ["Hi!", "Hello there!", "Hey! Nice to see you."],
    "hi": ["Hi!", "Hello there!"],
    "how are you": ["I'm fine, thanks! How about you?", "Doing great, thanks for asking!"],
    "what is your name": ["I'm CodeBot, your friendly Python chatbot!"],
    "what can you do": ["I can chat with you about simple things — try saying hello, "
                         "asking how I am, or telling me a joke!"],
    "tell me a joke": ["Why do programmers prefer dark mode? Because light attracts bugs!"],
    "thank you": ["You're welcome!", "No problem at all!"],
    "thanks": ["You're welcome!", "Anytime!"],
    "bye": ["Goodbye!", "Bye! Take care."],
    "goodbye": ["Goodbye!", "See you soon!"],
}

DEFAULT_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Hmm, I don't know how to respond to that yet.",
    "Sorry, I didn't get that. Try saying 'hello' or 'bye'.",
]


def get_response(user_input):
    """Return a chatbot reply based on simple keyword matching."""
    text = user_input.lower().strip()

    for key, replies in RESPONSES.items():
        if key in text:
            return random.choice(replies)

    return random.choice(DEFAULT_RESPONSES)


def chat():
    print("=" * 45)
    print("CodeBot: Hi! I'm CodeBot. Type 'bye' to exit.")
    print("=" * 45)

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("CodeBot: Please say something!")
            continue

        response = get_response(user_input)
        print(f"CodeBot: {response}")

        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break


if __name__ == "__main__":
    chat()
