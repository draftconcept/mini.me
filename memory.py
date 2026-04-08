history = []

def add(role, content):
    history.append({"role": role, "content": content})

def get():
    return history