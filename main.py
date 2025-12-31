import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()
 
def main():
    # Fetch the variable
    api_key = os.getenv("API_KEY")
    
    if api_key:
        # Avoid printing the full key in real apps for security!
        print(f"API Key found: {api_key[:4]}****")
    else:
        print("API Key not found. Please set the API_KEY environment variable.")

# This ensures the function runs when you call the script
if __name__ == "__main__":
    main()