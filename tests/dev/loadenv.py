from dotenv import load_dotenv
import os
print(load_dotenv())

print(os.getenv("OPENAI_API_KEY"))