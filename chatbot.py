def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a program, so I don't have feelings, but thanks for asking!"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot created to assist you."
    elif "what can you do" in user_input:
        return "I can answer basic questions, chat with you, and help you with simple tasks!"
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "what is the time" in user_input or "current time" in user_input:
        return "I'm not equipped with real-time capabilities, so I can't tell you the current time. Sorry!"
    elif "who created you" in user_input:
        return "I was created by a developer learning how to build chatbots!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! I'm here to help!"
    elif "where are you from" in user_input:
        return "I'm from the digital world, where I exist to assist you."
    elif "what is love" in user_input:
        return "Love is a complex emotion that I'm still trying to understand!"
    else:
        return "I'm sorry, I don't understand that. Can you try asking something else?"

# Example usage
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break
