import streamlit as st
import pandas as pd
from pandasai.llm import BambooLLM
from pandasai import Agent
from pandasai.responses.streamlit_response import StreamlitResponse
import os
import matplotlib.pyplot as plt

# Define la ruta para guardar los gráficos
user_defined_path = "exports/charts"

# Crea el directorio si no existe
os.makedirs(user_defined_path, exist_ok=True)

# Dictionary to store the extracted dataframes
data = {}

def main():
    # Side Menu Bar
    with st.sidebar:
        st.title("Configuration:⚙️")
        # Activating Demo Data
        st.text("Data Setup: 📝")
        file_upload = st.file_uploader("Upload your Data", accept_multiple_files=False, type=['csv', 'xls', 'xlsx'])

        st.markdown(":green[*Please ensure the first row has the column names.*]")

        # Selecting LLM to use
        llm_type = st.selectbox(
            "Please select LLM",
            ('BambooLLM',), index=0
        )

        # Adding users API Key
        user_api_key = st.text_input('Please add your API key', placeholder='Paste your API key here', type='password')

        # Get Pandas API key here
        st.markdown("[Get Your PandasAI API key here](https://www.pandabi.ai/auth/sign-up)")

    if file_upload is not None:
        data = extract_dataframes(file_upload)
        df = st.selectbox("Here's your uploaded data!",
                          tuple(data.keys()), index=0)
        st.dataframe(data[df])

        llm = get_LLM(llm_type, user_api_key)

        if llm:
            # Instantiating PandasAI agent
            analyst = get_agent(data, llm)

            # Starting the chat with the PandasAI agent
            chat_window(analyst)
            
    else:
        st.warning("Please upload your data first! You can upload a CSV or an Excel file.")

# Function to get LLM
def get_LLM(llm_type, user_api_key):
    try:
        if llm_type == 'BambooLLM':
            if user_api_key:
                os.environ["PANDASAI_API_KEY"] = user_api_key
            else:
                os.environ["PANDASAI_API_KEY"] = os.getenv('PANDASAI_API_KEY')

            llm = BambooLLM()
            return llm
    except Exception as e:
        st.error("No/Incorrect API key provided! Please Provide/Verify your API key")

# Function for chat window
def chat_window(analyst):
    with st.chat_message("assistant"):
        st.text("Explore your data with PandasAI?🧐")

    # Initializing message history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Displaying the message history on re-run
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if 'question' in message:
                st.markdown(message["question"])
            elif 'response' in message:
                response = message['response']
                
                st.write(f"Response received: {response}")
                
                # Check if response is a valid path
                if isinstance(response, str) and response.startswith(user_defined_path):
                    show_saved_chart(response)
                else:
                    st.write(response)
                
            elif 'error' in message:
                st.text(message['error'])
    
    # Getting the questions from the users
    user_question = st.chat_input("What are you curious about? ")
    
    if user_question:
        with st.chat_message("user"):
            st.markdown(user_question)
        st.session_state.messages.append({"role": "user", "question": user_question})
       
        try:
            with st.spinner("Analyzing..."):
                response = analyst.chat(user_question)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "response": response})
        
                if isinstance(response, str) and response.startswith(user_defined_path):
                    show_saved_chart(response)
                else:
                    st.write(response)
        
        except Exception as e:
            st.write(e)
            error_message = "⚠️Sorry, Couldn't generate the answer! Please try rephrasing your question!"

    # Function to clear history
    def clear_chat_history():
        st.session_state.messages = []
    # Button for clearing history
    st.sidebar.text("Click to Clear Chat history")
    st.sidebar.button("CLEAR 🗑️", on_click=clear_chat_history)

def get_agent(data, llm):
    """
    The function creates an agent on the dataframes extracted from the uploaded files
    Args: 
        data: A Dictionary with the dataframes extracted from the uploaded data
        llm:  llm object based on the ll type selected
    Output: PandasAI Agent
    """
    agent = Agent(list(data.values()), config={"llm": llm, "save_charts_path": user_defined_path, "save_charts": True, "verbose": True, "response_parser": StreamlitResponse})
    return agent

def extract_dataframes(raw_file):
    """
    This function extracts dataframes from the uploaded file/files
    Args: 
        raw_file: Upload_File object
    Processing: Based on the type of file read_csv or read_excel to extract the dataframes
    Output: 
        dfs:  a dictionary with the dataframes
    """
    dfs = {}
    if raw_file.name.split('.')[1] == 'csv':
        csv_name = raw_file.name.split('.')[0]
        df = pd.read_csv(raw_file)
        dfs[csv_name] = df

    elif (raw_file.name.split('.')[1] == 'xlsx') or (raw_file.name.split('.')[1] == 'xls'):
        xls = pd.ExcelFile(raw_file)
        for sheet_name in xls.sheet_names:
            dfs[sheet_name] = pd.read_excel(raw_file, sheet_name=sheet_name)

    return dfs

def show_saved_chart(file_path):
    """
    Show the chart saved in the directory and provide a download link.
    """
    if os.path.exists(file_path):
        # Display the image
        st.image(file_path, caption="Generated Chart")

        # Provide a download link
        with open(file_path, "rb") as file:
            st.download_button(
                label="Download Chart",
                data=file,
                file_name=os.path.basename(file_path),
                mime="image/png"
            )
    else:
        st.error("El archivo del gráfico no se encuentra.")
main()
if __name__ == "__main__":
    main()