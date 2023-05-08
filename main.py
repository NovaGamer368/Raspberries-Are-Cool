import os
import json
import requests
import openai
import config



 # INSERT API KEY FOR CHATGPT

openai.api_key = config.api_key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= "list me ingrediants for shrimp scampi",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.2,
  presence_penalty=0
)

# Load the JSON data as a dictionary
data = json.loads(json.dumps(response))

# Access the 'choices' key
choices = data['choices']

# Print the choices
for choice in choices:
  print(choice['text'])