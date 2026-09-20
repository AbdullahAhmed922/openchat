from ollama import chat

messages = []

print("Chat with Qwen (type 'exit' to quit)")

while True:
    prompt = input("You: ").strip()

    if prompt.lower() in {"exit", "quit"}:
        break
    if not prompt:
        continue

    messages.append({'role': 'user', 'content': prompt})
    response = chat(model='qwen2.5:3b', messages=messages)
    messages.append(response.message)
    print(f"Qwen: {response.message.content}")
    