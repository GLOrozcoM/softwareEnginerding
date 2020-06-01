# I wonder what Atticus carries in the briefcase.

# I still wish there were more new things under this sun
import os

# Acquire the current working directory
foundation = os.getcwd()

files = [f for f in os.listdir(foundation) if os.path.isfile(f)]

print(foundation)
print()