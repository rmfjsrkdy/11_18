import streamlit as st
import base64
from openai import OpenAI

st.write("Hello World")

st.divider()

api_key = st.text_input('API KEY', type="password")

client = OpenAI(api_key = api_key)

tab1, tab2 = st.tabs(["LLM", "Image generator"])

with tab1:
    user_question = st.text_area("", key="question")
    if st.button("Submit"):
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "user", "content": user_question}
                ]
                )
        answer = response.choices[0].message.content
        st.write(answer)

with tab2:
    prompt = st.text_area("", key="generator")
    if st.button("Generate"):
        img = client.images.generate(
            model="gpt-image-1-mini", prompt=prompt)
        image_bytes = base64.b64decode(img.data[0].b64_json)
        st.image(image_bytes)

