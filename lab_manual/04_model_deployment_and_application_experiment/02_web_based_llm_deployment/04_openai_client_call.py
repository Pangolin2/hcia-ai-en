import openai


client = openai.OpenAI(
    base_url="http://localhost:8080/v1", # Service request address for local deployment
    api_key="sk-no-key-required",
)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Who are you?"},
    ],
)

print(completion)
print(completion.choices[0].message)
print(completion.choices[0].message.content)
