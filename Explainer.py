import os
import asyncio
import aiohttp
import openai
import MakeQuery

openai.api_key = os.environ.get('OPENAI_API_KEY')


async def get_explanation(query: MakeQuery.Query):
    completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query.query},
            {"role": "system", "content": query.context},
        ]
    )
    return '\n'.join([item.message.content for item in completion.choices])
