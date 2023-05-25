import openai
import MakeQuery

openai.api_key = "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"


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
