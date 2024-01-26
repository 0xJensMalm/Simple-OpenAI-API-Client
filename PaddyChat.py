import openai
import os
import platform

# Function to clear the console screen based on the operating system
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Function to initialize OpenAI with the API key
def initialize_openai():
    openai.api_key = 'Enter API key here'

# Function to send messages to the OpenAI API, including any context
def send_message_to_openai(message, model, context_messages=[]):
    try:
        messages = [{"role": "system", "content": context} for context in context_messages]
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main function to run the chat interface
def main():
    initialize_openai()  # Initialize the OpenAI API key

    welcome_message = ("Welcome to the custom chat interface!\n"
                       "Available commands:\n"
                       "- 'clear' : clears chat\n"
                       "- 'quit' : exit\n"
                       "- 'context' : add context\n"
                       "- 'model' : displays current model\n"
                       "- 'model 3.5' : change to model 3.5-turbo\n"
                       "- 'model 4' : change to model 4\n"
                       "- 'model 4.5' : change to model 4.5-turbo\n")
    print(welcome_message)

    context_messages = []
    current_model = "gpt-3.5-turbo"  # Default model

    while True:
        user_input = input("You: ")
        user_input_lower = user_input.lower()

        if user_input_lower == 'quit':
            break
        elif user_input_lower == 'clear':
            clear_screen()
            print(welcome_message)  # Reprint the welcome message after clearing
        elif user_input_lower == 'context':
            context = input("Enter context: ")
            context_messages.append(context)
            print("Context added.")
        elif user_input_lower == 'model':
            print(f"Current model: {current_model}")
        elif user_input_lower.startswith('model '):
            model_cmd, model_version = user_input_lower.split(maxsplit=1)
            if model_version == "3.5":
                current_model = "gpt-3.5-turbo"
            elif model_version == "4":
                current_model = "gpt-4"
            elif model_version == "4.5":
                current_model = "gpt-4.5-turbo"
            else:
                print("Invalid model version. Available versions are 3.5, 4, 4.5.")
            print(f"Model changed to: {current_model}")
        else:
            chat_response = send_message_to_openai(user_input, current_model, context_messages)
            if chat_response:
                print(f"AI: {chat_response}")

if __name__ == "__main__":
    main()
