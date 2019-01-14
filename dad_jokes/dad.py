import requests, random, pyfiglet
from termcolor import colored

url = "https://icanhazdadjoke.com/search?"

header = pyfiglet.figlet_format("DAD JOKES 3000!")
header = colored(header, color="red")
print(header)

topic = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
  url,
  headers = {
    "accept": "application/json"
  },
  params = {
    "term": topic
  }
)

data = response.json()
length = len(data["results"])
if length == 0:
    print(f"Sorry, I've got 0 jokes about {topic}.")
else:
    print(f"I've got {length} jokes about {topic}. Here is one!")
    print(data["results"][random.randint(0, length - 1)]["joke"])
