print("chatbot")
while True:
    user = input("you: ").lower()
    if user == "hello":
        print("Bot: hi!")
    elif user == "how are youhe":
        print("Bot: I'm fine,thanks!")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")