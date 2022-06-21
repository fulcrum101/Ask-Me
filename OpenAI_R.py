import os

import openai

openai.api_key = os.environ['OPEN_AI_KEY']


def R(text: tuple):
    '''
    Recipe
    :param text: (tuple) Meal and ingredients
    :return: (str) Instructions
    '''

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Write a recipe based on these ingredients and instructions:\n\n{text[0]}\n\nIngredients:\n{text[1]}\n\nInstructions:",
        temperature=0.3,
        max_tokens=120,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']
