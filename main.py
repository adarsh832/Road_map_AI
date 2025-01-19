import streamlit as st
from ollama import chat
from ollama import ChatResponse
import time as tm
      

def roadmap(learn,time,level):
    response: ChatResponse = chat(model='llama3.2', messages=[
         {
            'role': 'system',
            'content': 'You are a AI that help people to get roadmap for learning.give them a step by step guide to learn.',
            'role': 'user',
            'content': f'I want to leant {learn} in {time} and I am {level} level. give me a roadmap to learn. step by step guide with resources.',


            },
            
        ])
    output = response['message']['content']
    for word in output.split(" "):
        yield word + " "
        tm.sleep(0.02)


st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Road-map Generator</h1>", unsafe_allow_html=True)

with st.container():
      learn = st.text_input("What do you want to learn?", placeholder="e.g., Python, Data Science")
      time = st.text_input("How much time do you want to spend on it?", placeholder="e.g., 1 month or 20 days")
      level = st.selectbox("What is your level?", ["Beginner", "Intermediate", "Advanced"])
      submit = st.button("Submit")

with st.container(height=250):
        if submit:
            if learn and time and level:
                
                st.write_stream(roadmap(learn, time, level))
                st.snow()
                st.toast("Roadmap generated successfully.")
            else:    
                st.error("Please fill all the fields.")
