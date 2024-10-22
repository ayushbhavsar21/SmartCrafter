import streamlit as st
import requests
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="Smart Contract Generator",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="icon2.png",
)

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("icon.png")
st.image(image, width=350)

# App title and introduction
st.title("Smart Contract Generator ₿⛓")
st.sidebar.markdown("### Welcome to the AI-powered Smart Contract Generator!")
st.sidebar.markdown("This app harnesses power of Gemini to Build Smart Contracts for WEB3 Projects. Enter Contract Requirements and Contract Language to generate a Smart Contract for your next Web3 Project.")
st.markdown("This app uses Gemini API to generate Smart Contracts based on contract details and language.")

contract_det = st.sidebar.text_area("Enter Your Contract Details", height=200)
contract_language = st.sidebar.selectbox("Enter Contract Language", ("Solidity", "Vyper", "Ethereum", "Rust", "Move"))



def smart_contract(details, language):
    prompt = f"I am Building a project in {language}. The description of the project is below:\ndescription: {details}\n\nYour Task is to provide a code with all the requests above and no bugs.\nIn your response, provide all the code with notes and explanation of each function."
    
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={gemini_api}"

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        try:
            # Print the response to understand its structure
            st.write("Response from API:", response.json())

            # Safely extract text, checking for the structure
            json_response = response.json()

            # Check if 'contents' and 'parts' exist in the response
            if "contents" in json_response and len(json_response["contents"]) > 0:
                parts = json_response["contents"][0].get("parts", [])
                if len(parts) > 0:
                    return parts[0].get("text", "No response text found.")
                else:
                    return "No parts found in the response."
            else:
                return "No contents found in the response."
        
        except Exception as e:
            return f"Error while parsing response: {e}"
    else:
        return f"Error: {response.status_code} - {response.text}"


if st.sidebar.button("Generate", type="primary"):
    solution = smart_contract(contract_det, contract_language)
    st.markdown(solution)
