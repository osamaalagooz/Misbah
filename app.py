import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from pandasai.middlewares import StreamlitMiddleware
from PIL import Image


def load_dataframe(filename):
    
    if filename.type == "text/csv":
        df = pd.read_csv(filename)
        df.rename(columns=lambda x: x.strip(), inplace=True)
        return df
    else:
        df = pd.read_excel(filename)
        df.rename(columns=lambda x: x.strip(), inplace=True)
        return df

image = Image.open("./Alaadin-lamb.webp")
st.image(image, caption=None, width=150, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.title("Misbah")
st.subheader('Chat with your Data')
st.divider()
st.write("Please upload your CSV file below.")

filenames = st.file_uploader("Upload a CSV", accept_multiple_files=True,type=["csv","xls", "xlsx"])

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"]== "assistant" and message.get("chart") != None:
            chart_image = message.get("chart")
            st.image(chart_image)
        

# user input
if user_prompt := st.chat_input("Your prompt"):
    if len(filenames) == 1:
        df = load_dataframe(filenames[0])

    else:
        df = []
        for filename in filenames:
            df = load_dataframe(filename)
            df.append(df)

    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # generate responses
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        #llm = ChatOpenAI(streaming=True)
        llm = OpenAI(streaming=True)
        pandas_ai = PandasAI(llm, enable_cache= False, save_charts=True, save_charts_path="./imags/")
        res = pandas_ai.run(df, user_prompt, True)
        
        image_path = f"/imags/exports/charts/{pandas_ai._prompt_id}/chart.png"
        working_dir = os.getcwd()
        path = working_dir + image_path
        print(f"path to image:  {path}")

        try:
            chart_image = Image.open(path)
            st.image(chart_image)
        except:
            chart_image=None
        
        full_response += res
        message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)


    st.session_state.messages.append({"role": "assistant", "content": full_response, "chart":chart_image})

    #
    #text/csv
    #application/vnd.openxmlformats-officedocument.spreadsheetml.sheet