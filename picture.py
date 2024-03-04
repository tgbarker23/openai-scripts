import sys
import webbrowser
from openai import OpenAI
client = OpenAI()

if len(sys.argv) > 1:
    argument = sys.argv[1]
    quoted_argument = f'"{argument}"'

    response = client.images.generate(
      model="dall-e-3",
      prompt=quoted_argument,
      n=1,
      size="1024x1024"
    )
    
    print(response.data[0].url)
    webbrowser.open(response.data[0].url)
else:
    print("No command-line argument provided.")


