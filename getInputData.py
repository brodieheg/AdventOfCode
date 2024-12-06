from dotenv import load_dotenv
from aocd import get_data

# Load the .env file
load_dotenv()

# Now get the environment variable

def getTodaysData(day):
    data = get_data(day=day, year=2024)
    return data
