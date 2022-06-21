import os

import openai

openai.api_key = os.environ['OPEN_AI_KEY']


def S_T(text: str):
    '''
    Gives 5 usefuyl notes when studying
    :param text: (str) Topic
    :return: (str) Notes
    '''

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"What are 5 key points I should know when studying {text}?",
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']
