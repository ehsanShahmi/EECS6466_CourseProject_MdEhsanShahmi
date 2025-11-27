import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Access and test the environment variables
# database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("GEMINI_API_KEY")
# debug_mode_str = os.getenv("DEBUG")

# Optional: Convert string to a boolean if necessary
# debug_mode = debug_mode_str == "True"

# print(f"Database URL: {database_url}")
print(f"Secret Key: {secret_key}")
# print(f"Debug Mode: {debug_mode}, Type: {type(debug_mode)}")