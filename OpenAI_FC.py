import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPEN_AI_KEY']


def F_C(text: str):
    '''
    Friendly chat.
    :param text: (str) question
    :return: (str) answer
    '''
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"You: What have you been up to?\nFriend: Watching old movies.\n{text}?\nFriend:",
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )
    return response['choices'][0]['text']
