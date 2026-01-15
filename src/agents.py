import json 
from src.tools import TOOLS
from src.openai_client import client, generate_image, text_to_speech
from src.config import SYSTEM_MESSAGE,MODEL
from src.database import get_ticket_price

def handle_tool_calls(message):
    responses, cities = [], []
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_ticket_price":
            args = json.loads(tool_call.function.arguments)
            city = args["destination_city"]
            cities.append(city)
            price = get_ticket_price(city)
            responses.append({
                "role":"tool", "content":price,"tool_call_id":tool_call.id
            })
    return responses, cities

def chat(history):
    """Main chat function - YOUR ORIGINAL WORKING CODE"""
    # Convert Gradio history format to OpenAI format
    history_openai = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + history_openai
    
    response = client.chat.completions.create(
        model=MODEL, 
        messages=messages, 
        tools=TOOLS
    )
    cities = []
    image = None

    # Handle tool calls loop (YOUR ORIGINAL LOGIC)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        responses, cities = handle_tool_calls(message)
        messages.append(message)
        messages.extend(responses)
        response = client.chat.completions.create(
            model=MODEL, 
            messages=messages, 
            tools=TOOLS
        )
    
    # Final response
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})  # Add to Gradio format

    # Generate voice and image (YOUR ORIGINAL LOGIC)
    voice = text_to_speech(reply)
    if cities:
        image = generate_image(cities[0])
    
    return history, voice, image 