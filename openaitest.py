import openai
openai.api_key = "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"

response = openai.Completion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Write an email to my boss for resigantion"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)