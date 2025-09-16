import cohere
from pprint import pprint
import json

token = "4SodIKMCAU1yWHuUtVMM6YHEKQDfxQY7r9eot1Bo"
co = cohere.ClientV2(token)

docs = [
    {
        "data": {
            "title": "Burj Khalifa",
            "snippet": "The Burj Khalifa is the tallest building in the world at 828 meters."
        }
    }
    ,
    {
        "data":
            {"title": "Tall penguins",
             "snippet": "Emperor penguins grow up to 122cm tall"
             }

    },
    {
        "data":
            {"title": "Penguin habitats",
             "snippet": "Emperor penguins only live in Antarctica."
             }
    }
]

def send_prompt(message):
    return co.chat(
        model="command-r-plus",
        messages=[
            {"role": "user", "content": message}
        ],
        documents=docs
    )

def cohere_without_web_search():
    content = "Tell me about the tallest building in the world."
    response = send_prompt(content)
    pprint(json.loads(response.json()))

    content = "Tell me about the tallest pinquins in the world."
    response = send_prompt(content)
    pprint(json.loads(response.json()))

    content = "Tell me about the tallest pinquins habitat."
    response = send_prompt(content)
    pprint(json.loads(response.json()))

cohere_without_web_search()