import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Streamlit application title
st.title("Qwen-7B-Chatbot")

# Load the model and tokenizer (caching for faster reload)
@st.cache_resource
def load_model():
    model_name = "Qwen/Qwen-7B-Chat"
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
    return tokenizer, model

tokenizer, model = load_model()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", placeholder="Ask me anything...")

# Send button
if st.button("Send"):
    if user_input:
        # Display user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Prepare the input
        inputs = tokenizer(user_input, return_tensors="pt")
        
        # Generate response
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=200, pad_token_id=tokenizer.eos_token_id)

        # Decode and display response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.session_state.messages.append({"role": "bot", "content": response})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    else:
        st.write(f"**Qwen-7B:** {message['content']}")

# Clear history
if st.button("Clear Chat"):
    st.session_state.messages = []
