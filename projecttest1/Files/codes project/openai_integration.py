from openai import OpenAI
from config import key

# Create an OpenAI client
client = OpenAI(api_key=key)

def ask_assistant(user_msg: str) -> str:
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo",
            prompt=f"Analyze the following text and determine if it is related to corruption:\n\n{user_msg}",
            max_tokens=150
        )
        if response and response.choices:
            return response.choices[0].text.strip()
        else:
            return "No response from the assistant."
    except Exception as e:
        return f"An error occurred: {e}"
