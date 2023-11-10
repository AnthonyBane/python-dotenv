import os
from dotenv import load_dotenv, dotenv_values

# Loads the environment variables into the local environment
load_dotenv()

# If you have local environment variables already set with the same name,
# the override=True parameter will ensure it takes the value from the .env file

# load_dotenv(override=True)

print(os.getenv("SECRET"))
print(os.getenv("USERNAME"))
print(os.getenv("PASSWORD"))

# Alternative, you can load these into a dictionary
env_dict = dotenv_values(".env")
print(env_dict)
