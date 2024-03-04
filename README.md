# openai-scripts

## About
this is a sandbox project that houses python scripts used to prompt open ai's api.

## Using
1. first you will need an api access key [steps](https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key)
2. install requirements
  `pip install -r requirements.txt`
### prompt.py
text based query to GPT (currently hardcoded to use gpt-4)
`python prompt.py <quoted_prompt>`
```
 openai-scripts git:(main) ✗ python prompt.py "what is 2+2?"
'2+2 is 4.'
```
### picture.py
query DALL-E for image generation  (currently hardcoded to use dall-e-3)
`python picture.py <quoted_image_request_text`
```
openai-scripts git:(main) ✗ python picture.py "picture of a pizza"
```

