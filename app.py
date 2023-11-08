import streamlit as st
from openai import OpenAI
from PIL import Image

client = OpenAI()

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png', 'heic'])

# Check if an image has been uploaded
if uploaded_file is not None:
    # Open the image with PIL
    image = Image.open(uploaded_file)
    st.chat_message("user").write("Analyze the safety of this image, suggest safety procedures")
    response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=st.session_state.messages
)
    
    st.chat_message("Caution Clip").write(response["content"]["text"])
    # Display the image
    st.image(image, caption='Uploaded Image', use_column_width=True)

openai_api_key = st.secrets["key"]
client.api_key = openai_api_key

st.title("💬 Caution Clip Chat")
st.caption("🚀 Upload images and chat about industrial workplace safety")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": {"type": "text", "text": "How can I help you?"}}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"]["text"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": {"type": "text", "text": prompt}})
    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=st.session_state.messages
)

    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("Caution Clip").write(msg.content)