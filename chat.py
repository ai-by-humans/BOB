import os
import openai

# Configure the OpenAI local server
openai.api_base = "http://localhost:1234/v1"
openai.api_key = os.getenv('OPENAI_API_KEY', 'NULL')

# Initialize message history
message_history = [
    {"role": "system", "content": "Role-play as a real human in conversations with the user."},
]


# Main loop to keep the chat going
while True:
    # Get user input
    user_input = input("You: ")

        # Check if the user wants to exit
    if user_input.lower() in ['exit', 'quit', 'stop']:
        print("Exiting the chat.")
        break
    
    # Append user input to the message history
    message_history.append({"role": "user", "content": user_input})
    
    try:
        # Perform the API call to create a chat completion
        completion = openai.ChatCompletion.create(
            model="your-model-name",  # Replace 'your-model-name' with the model name your local server expects
            messages=message_history
        )
        
        # Extract the message from the response and print it
        message = completion.choices[0].message['content']
        print(f"AI: {message}")
        
        # Append AI's response to the history
        message_history.append({"role": "assistant", "content": message})
        
    except Exception as e:
        # Handle any errors that occur during the API call
        print(f"An error occurred: {e}")
        break  # Break the loop if an error occurs