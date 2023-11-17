import streamlit as st
from openai import OpenAI

client = OpenAI()

st.set_page_config(
    page_title="Caution Clip Chat",
    page_icon="💬",
)


if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

if len(st.session_state.messages) > 40:
    st.warning("You've sent too many messages, please try again later")
else:

    st.image("https://res.craft.do/user/full/23a03a79-af5e-1af9-b4ff-27170389b6b1/doc/A52ACDBF-362E-48DB-B76E-34FDE4919297/5F1555AE-C787-422A-A512-2666E55698DD_2/y3ZBnbZTkyxBp7XJbPbs9K7vxpFnhnrpB831zvZPfvYz/Group%2019.png")
    st.title("💬 Caution Clip Chat")
    st.caption("🚀 Ask questions about Caution Clip and industrial workplace safety")

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
            st.chat_message("assistant").write(response.choices[0].message.content)