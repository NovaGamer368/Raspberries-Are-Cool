import os
import json
import requests
import openai


apiKey = "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"

openai.api_key = apiKey


response = openai.Completion.create(
  model="text-davinci-003",
  prompt= "Say this is a test",
  max_tokens=7,
  temperature=0
)

# Load the JSON data as a dictionary
data = json.loads(json.dumps(response))

# Access the 'choices' key
choices = data['choices']

# Print the choices
for choice in choices:
    print(choice['text'])