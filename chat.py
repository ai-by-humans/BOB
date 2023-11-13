import os
import openai
import json

def load_conversation_setup(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Load conversation setup from the JSON file
conversation_setup = load_conversation_setup('conversation_setup.json')

def print_welcome_message(setup):
    print("\nWelcome to the AI Chat!")
    print(f"Today's scenario: {setup['scenario']}")
    print(f"Rules: {setup['rules']}")
    print("\nType 'exit', 'quit', or 'stop' to end the chat.")
    print("Let's start the conversation!\n")

# Configure the OpenAI server
openai.api_base = "http://localhost:1234/v1"
openai.api_key = os.getenv('OPENAI_API_KEY', 'NULL')

# Print the welcome message with the loaded scenario and rules
print_welcome_message(conversation_setup)

# User input
user_name = input("Please enter your name: ")

# Prepare the system instruct message from the loaded data
system_instruct = f"<s>[INST] You are {conversation_setup['char']['name']} ({conversation_setup['char']['traits']}). You must follow the scenario: {conversation_setup['scenario']}, and adhere to these rules: {conversation_setup['rules']}. [/INST]"

message_history = [{"role": "system", "content": system_instruct}]

# Main loop to keep the chat going
while True:
    user_input = input(f"{user_name}: ")

    if user_input.lower() in ['exit', 'quit', 'stop']:
        print("Exiting the chat.")
        break

    formatted_input = f"<s>[INST] {user_input} [/INST]"
    message_history.append({"role": "user", "content": formatted_input})

    try:
        chat_completion = openai.ChatCompletion.create(
            model="mistralai/Mistral-7B-Instruct-v0.1",
            temperature=1,
            max_tokens=1024,
            messages=message_history
        )
        message = chat_completion.choices[0].message['content']
        print(f"AI: {message.strip()}\n")
        message_history.append({"role": "assistant", "content": message})

    except Exception as e:
        print(f"An error occurred: {e}")
        break
