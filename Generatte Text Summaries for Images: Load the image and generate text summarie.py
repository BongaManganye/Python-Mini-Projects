# RAG python
# Generatte Text Summaries for Images: Load the image and generate text summaries

import base64
import openai

png_file_path = "../datasets/images/vietnam.png"

with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    prompt = (
        "You are an assistant for visually impaired users. "
        "Describe the image in detail."
    )

    response = openai.chat.completions.create(
        model="gpt-4o", #Defing the model to use
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,
    {base64_image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=150,
    )

    content = response.choices[0].message.content
