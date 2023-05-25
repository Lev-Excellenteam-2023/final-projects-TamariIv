import openai
openai.api_key = "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"


def get_explanation(query):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query},
            {"role": "system", "content": "Answer shortly but clearly and explain unfamiliar terms. "
                                          "The context is that you are getting a slide that is a part of a powerpoint"
                                          "and you need to explain it."},
        ]
    )
    for item in completion.choices:
        print(item.message.content)


