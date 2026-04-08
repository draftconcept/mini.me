import llm

def think(user_input, history):
    messages = history + [
        {"role": "user", "content": user_input}
    ]

    reply = llm.chat(messages)
    return reply