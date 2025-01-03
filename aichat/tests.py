# from openai import OpenAI
# from dotenv import load_dotenv
# import os


# load_dotenv()

# if not os.getenv("OPENAI_API_KEY"):
#     raise ValueError("Please set the OPENAI_API_KEY environment variable.")
#     brake
# elif os.getenv("OPENAI_API_KEY"):
#     print("API key found")

# def get_response(prompt):
#     client = OpenAI(
#                 base_url = "https://integrate.api.nvidia.com/v1",
#                 api_key = os.getenv("OPENAI_API_KEY")
#             )
    
#     completion = client.chat.completions.create(
#       model="mistralai/mistral-7b-instruct-v0.3",
#       messages=[{"role":"user","content":prompt}],
#       temperature=0.2,
#       top_p=0.7,
#       max_tokens=1024,
#       stream=True
#     )

#     result = ""
#     for chunk in completion:
#         if chunk.choices[0].delta.content is not None:
#             result += chunk.choices[0].delta.content

#     print(result)

# get_response("Hello, how are you?")  # This will raise an error because the function does not return anything