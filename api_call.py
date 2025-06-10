import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    # Get API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    # Initialize the OpenAI client
    client = openai.OpenAI(api_key=api_key)
    
    # Define a fixed system prompt
    system_prompt = "You are a helpful, concise assistant."
    
    # Get user input
    user_input = input("Enter your question: ")
    
    try:
        # Make the API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Extract and display the response
        assistant_response = response.choices[0].message.content
        
        print("\nAssistant's response:")
        print(assistant_response)
        
        # Display token usage
        print("\nToken usage:")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Completion tokens: {response.usage.completion_tokens}")
        print(f"Total tokens: {response.usage.total_tokens}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main() 