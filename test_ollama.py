from ollama import chat

response = chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "user",
            "content": "Explain Python variables in simple words."
        }
    ],
)

print(response.message.content)