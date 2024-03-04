import sys
import textwrap
import pprint
from openai import OpenAI

client = OpenAI()
pp = pprint.PrettyPrinter(depth=6)


if len(sys.argv) > 1:
    argument = sys.argv[1]
    prompt = f'"{argument}"'

    completion = client.chat.completions.create(
      model="gpt-4",
      messages=[
        {"role": "system", "content": prompt},
      ]
    )

    pp.pprint(completion.choices[0].message.content)
else:
    pp.pprint("No command-line argument provided.")




