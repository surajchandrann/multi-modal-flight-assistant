import gradio as gr
from src.database import create_prices_table
from src.agents import chat

create_prices_table()  # Init DB

def put_message(message, history):
    """Add user message to chat"""
    return "", history + [{"role": "user", "content": message}]

with gr.Blocks(title="FlightAI Assistant") as ui:
    gr.Markdown("# 🔊 FlightAI - Voice + Image Travel Assistant")
    
    with gr.Row():
        chatbot = gr.Chatbot(height=500)
        image_output = gr.Image(height=500)
    
    audio_output = gr.Audio(autoplay=True)
    
    message = gr.Textbox(
        label="Ask about flights", 
        placeholder="What's the price to Mumbai?"
    )
    
    # CHAIN: message → add to history → call chat → update all 3 outputs
    message.submit(
        put_message, 
        [message, chatbot], 
        [message, chatbot]
    ).then(
        chat, 
        chatbot, 
        [chatbot, audio_output, image_output]
    )

ui.launch(share=True)
