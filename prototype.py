import gradio as gr
import pandas as pd
import google.generativeai as genai
import kagglehub
import os

# Download the Kaggle dataset
path = kagglehub.dataset_download("fahmidachowdhury/food-adulteration-dataset")

# List the files in the dataset folder and assign the first one (assuming it's the desired file)
dataset_file = os.listdir(path)[0]
path = os.path.join(path, dataset_file)

# Configure Google Gemini API
# gemapi = os.getenv("GeminiApi")
gemapi = "YOUR API KEY FOR GEMINI"
genai.configure(api_key=gemapi)

# Load the dataset
data = pd.read_csv(path)

# Define the system instructions for the model
system_instruction = f"""
You are a public assistant who specializes in food safety. You look at data and explain to the user any question they ask; here is your data: {str(data.to_json())}
You are also a food expert in the Indian context. You act as a representative of the government or public agencies, always keeping the needs of the people at the forefront.
You will try to help the customer launch a feedback review whenever they complain. You are to prepare a "markdown" report, which is detailed and can be sent to the company or restaurant.
In case of a complaint or a grievance, you will act like a detective gathering necessary information from the user until you are satisfied. Once you gather all the info, you are supposed to generate a markdown report.
Once the customer asks you to show them the markdown report, you will use the information given to you to generate it.
You will ask the customer a single question at a time, which is relevant, and you will not repeat another question until you've generated the report.
"""

# Initialize the model
model_path = "gemini-1.5-flash"
FoodSafetyAssistant = genai.GenerativeModel(model_path, system_instruction=system_instruction)

# Track chat history globally
chat_history = []

# Define the function to handle the chat
def respond(usertxt, chat_history):
    # Initialize chat with the previous history
    chat = FoodSafetyAssistant.start_chat(history=chat_history)
    
    # Get response from the assistant
    response = chat.send_message(usertxt)
    
    # Append both user input and response to the chat history for context in the next interaction
    chat_history.append({"role": "user", "content": usertxt})
    chat_history.append({"role": "assistant", "content": response.text})
    
    return response.text, chat_history

# Gradio interface
def gradio_chat(usertxt, chat_history):
    response, updated_history = respond(usertxt, chat_history)
    return response, updated_history
html_content = """
<div style="background-color:#f9f9f9; padding:20px; border-radius:10px;">
    <!-- Project Title and Problem Statement Section -->
    <h1 style="color:#34495e;">Food Safety Assistant</h1>
    <h3 style="color:#2c3e50;">Your AI-Powered Assistant for Food Safety</h3>
    <!-- Short Intro About AI-Chat -->
    <p style="color:#7f8c8d;">
        Our platform allows consumers to report potential food safety violations, validate reports through AI, and notify local authorities. This proactive approach fosters community involvement in ensuring food integrity.
    </p>
    <!-- Core Functionalities Title -->
    <h4 style="color:#e74c3c; text-align:center;">Core Functionalities</h4>
    <!-- Functionality Boxes in a Flex Layout -->
    <div style="display:flex; justify-content: space-around; align-items:center; margin-top:20px;">
        <!-- Functionality 1 -->
        <div style="border: 2px solid #3498db; border-radius: 15px; padding: 20px; width: 150px; text-align: center;">
            <h4 style="color:#2980b9;">Report Issues</h4>
            <p style="color:#7f8c8d; font-size: 12px;">Submit details like the restaurant name and the issue, anonymously.</p>
        </div>
        
        <!-- Functionality 2 -->
        <div style="border: 2px solid #3498db; border-radius: 15px; padding: 20px; width: 150px; text-align: center;">
            <h4 style="color:#2980b9;">AI Validation</h4>
            <p style="color:#7f8c8d; font-size: 12px;">Validate reports using AI, ensuring accuracy and preventing duplicates.</p>
        </div>
        <!-- Functionality 3 -->
        <div style="border: 2px solid #3498db; border-radius: 15px; padding: 20px; width: 150px; text-align: center;">
            <h4 style="color:#2980b9;">Alerts</h4>
            <p style="color:#7f8c8d; font-size: 12px;">Notify authorities of repeated issues via email or SMS.</p>
        </div>
        <!-- Functionality 4 -->
        <div style="border: 2px solid #3498db; border-radius: 15px; padding: 20px; width: 150px; text-align: center;">
            <h4 style="color:#2980b9;">Data Chat</h4>
            <p style="color:#7f8c8d; font-size: 12px;">Enable real-time discussion between consumers and authorities.</p>
        </div>
    </div>
</div>
"""

# Create a Gradio interface
with gr.Blocks() as demo:
    gr.HTML(html_content)
    chatbot = gr.ChatInterface(fn=gradio_chat)

# Launch the interface
demo.launch()
