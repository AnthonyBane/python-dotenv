import os
from dotenv import dotenv_values

# Loads environment variables into a shared dictionary
env_dict = {
    **dotenv_values("config\.env.secret"),
    **dotenv_values("config\.env.shared"),
}

print(env_dict)
