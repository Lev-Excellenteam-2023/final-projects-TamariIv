import os
import asyncio
import openai
import MakeQuery

openai.api_key = os.environ.get('OPENAI_API_KEY')


async def get_explanation(query: MakeQuery.Query):
    res = ""
    completion = await openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query.query},
            {"role": "system", "content": query.context},
        ]
    )
    for item in completion.choices:
        res += item.message.content
    return res
