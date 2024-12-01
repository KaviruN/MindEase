# from openai import OpenAI
# from dotenv import load_dotenv
# import os


# load_dotenv()

# if not os.getenv("OPENAI_API_KEY"):
#     raise ValueError("Please set the OPENAI_API_KEY environment variable.")
#     brake
# elif os.getenv("OPENAI_API_KEY"):
#     print("API key found")

# client = OpenAI(
#   base_url="https://integrate.api.nvidia.com/v1",
#   api_key=os.getenv("OPENAI_API_KEY")
# )

# completion = client.openai.ChatCompletion.create(
#   model="mistralai/mistral-7b-instruct-v0.3",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant specialized in mental health advice.if not show 'i cant help with that if you need help in mental helth, feel free to ask.'"},
#     {"role": "user", "content": "how to maeke a django model?"},
#   ],
#   temperature=0.5,
#   top_p=1,
#   max_tokens=1024,
#   stream=True
# )

# for chunk in completion:
#   if chunk.choices[0].delta.content is not None:
#     print(chunk.choices[0].delta.content, end="")

# # print(completion)