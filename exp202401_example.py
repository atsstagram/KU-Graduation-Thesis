from openai import OpenAI
import json

# Set your OpenAI API key
client = OpenAI(api_key="sk-example")

with open("train_example.json") as f:
    data = json.load(f)
print(data)


def chat_with_gpt(prompt):
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",  # Select a model
        messages=[
            {"role": "system", "content": prompt},
        ],
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


def main():
    result = []
    for item in data:
        prompt = (
            "Respond only with a numerical value. "
            + "Choose the emotion for the following sentence from the following options "
            + "and reply with the corresponding number "
            + "{0:sadness, 1:joy, 2:love, 3:anger, 4:fear, 5:surprise} "
            + item["text"]
        )
        answer = chat_with_gpt(prompt)
        answer = int(answer)
        result.append({"text": item["text"], "label": answer})

    # Convert list to JSON format
    json_data = json.dumps(result)

    # Write JSON data to a file
    with open("output.json", "w") as file:
        file.write(json_data)


if __name__ == "__main__":
    main()
