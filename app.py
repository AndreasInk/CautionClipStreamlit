import streamlit as st
from openai import OpenAI
from PIL import Image
import base64
from io import BytesIO
import json

client = OpenAI()

def encode_image(image):
    # Create a bytes buffer for the image
    buffer = BytesIO()
    
    # Save the image to the buffer
    image.save(buffer, format="JPEG")
    
    # Get the byte data from the buffer
    img_byte = buffer.getvalue()
    
    # Encode the byte data to base64
    return base64.b64encode(img_byte).decode('utf-8')
    
# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png', 'heic'])

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

if len(st.session_state.messages) > 5:
    st.warning("You've sent too many messages, please try again later")
else:
# Check if an image has been uploaded
    if uploaded_file is not None:
        # Open the image with PIL
        image = Image.open(uploaded_file)
        st.chat_message("user").write("Analyze the safety of this image, suggest safety procedures")
        st.session_state.messages += [{"role": "user", "content": "Analyze the safety of this image, suggest safety procedures"}]
        st.session_state.messages += [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Analyze the safety of this image, suggest safety procedures"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encode_image(image)}",
                    },
                },
            ],
        }
    ]
        response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=st.session_state.messages
    )
        
        st.chat_message("Caution Clip").write(response.choices[0].message.content)
        # Display the image
        st.image(image, caption='Uploaded Image', use_column_width=True)

    st.image("https://res.craft.do/user/full/23a03a79-af5e-1af9-b4ff-27170389b6b1/doc/A52ACDBF-362E-48DB-B76E-34FDE4919297/74675152-5304-40DF-A8BA-08AE32118954_2/5H0jvy5m0s2OVG8VVKv6eCDsQOU5fcCypJG09vGUnToz/Group%2019.png")
    st.title("💬 Caution Clip Chat")
    st.caption("🚀 Upload images and chat about industrial workplace safety and ask questions about Caution Clip")

    for msg in st.session_state.messages:
        try:
            st.chat_message(msg["role"]).write(msg["content"])
        except:
            break

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        # Replace 'your_markdown_file.md' with the path to your Markdown file
        markdown_file_path = './about.md'

        # Open the file and read it into a string
        with open(markdown_file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()

            system_prompt = [{"role": "system", "content": f"Here's a document that outlines what Caution Clip is: \n\n{markdown_content}"}]

            response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=system_prompt + st.session_state.messages
        )
            new_message = [{"role": "assistant", "content": response.choices[0].message.content}]
            st.session_state.messages += new_message
            st.chat_message("Caution Clip").write(response.choices[0].message.content)