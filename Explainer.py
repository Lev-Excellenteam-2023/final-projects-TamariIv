import os

import openai
import MakeQuery

openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_explanation(query: MakeQuery.Query):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query.query},
            {"role": "system", "content": query.context},
        ]
    )
    for item in completion.choices:
        print(item.message.content)
