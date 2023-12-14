import openai

openai.api_key = "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"
while True:
    mesgs = []
    user_input = input("我: ")
    if user_input == "end":
        break
    mesgs.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=mesgs)
    ai_response = response["choices"][0]["message"]["content"]
    print(f"人工智能:{ ai_response}")
