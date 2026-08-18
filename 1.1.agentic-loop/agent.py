from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

tools = [
    {
        "name": "calculator",
        "description": "Evaluates a mathematical expression and returns the numeric result",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate"
                }
            },
            "required" : ["expression"]
        }
    },
    
    {
        "name" : "web_search",
        "description": "Searches the web and returns relevant results",
        "input_schema": {
            "type": "object",
            "properties": {
                "query" : {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "What is 12 times 7?"
    }
]

while True:
    response = client.messages.create(
        model='claude-sonnet-5',
        max_tokens=1000,
        tools=tools,
        messages=messages
    )
    
    print("stop_reason: ", response.stop_reason)
    
    if response.stop_reason == "end_turn":
        break
    else:
        print("Claude want to use a tool")
        break