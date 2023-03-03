import requests
from random import choice

url = "https://icanhazdadjoke.com/search"

topic=input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": topic}
).json()

results=response["results"]
total_jokes=response["total_jokes"]


if total_jokes > 1:
    print(f"I've got {total_jokes} jokes about {topic}. Here's one:\n",
    choice(results)['joke'])
elif total_jokes == 1:
    print(f"I've got {total_jokes} joke about {topic}. Here it is:\n",
    results[0]['joke'])
else:
    print(f"Sorry, I don't have any jokes about {topic}.Please try again.")



