import brain
import memory

print("Agent started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    reply = brain.think(user_input, memory.get())

    print("Agent:", reply)

    memory.add("user", user_input)
    memory.add("assistant", reply)