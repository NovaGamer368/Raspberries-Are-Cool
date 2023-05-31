#py -m install -r requirements.txt
import json
import openai
import config
import recordaudio
import Pro200GUI

import os
from aiy.board import Board, Led

openai.api_key = config.api_key

def api_call(string_recording):
  #API call
  print('getting response')
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= string_recording,
    temperature=0,
    max_tokens=500,
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
    return (choice['text'])
#api_call(recordaudio.get_input(7))
with Board() as board:
        while True:
            print('\n Press the button and speak when you see RECORDING!!!\n')
            board.button.wait_for_press()
            board.led.state = Led.ON
            Pro200GUI.gui(api_call(recordaudio.get_input(7)), board)
            
        
