import streamlit as st
import requests
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
gemini_api = os.getenv("GEMINI_API_KEY")

# Streamlit page configuration
st.set_page_config(
    page_title="Smart Contract Generator",
    layout="centered",  # Can be "wide" if you prefer
    initial_sidebar_state="auto",
    page_icon="icon2.png",
)

# Custom styling and media query for mobile screens
st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }

    @import url('https://fonts.googleapis.com/css2?family=Broadway&display=swap');
    .broadway-font {
        font-family: 'Broadway', sans-serif;
        font-style: italic;
        font-size: 48px;
        color: #000;
    }
    @media only screen and (max-width: 600px) {
        .broadway-font {
            font-size: 24px;
            font-family: 'Broadway', sans-serif;
            font-style: italic;
            color: #000;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Layout with two columns for logo and title
col1, col2 = st.columns([1, 5])

with col1:
    image = Image.open("icon2.png")
    st.image(image, width=100)
with col2:
    st.markdown('<p class="broadway-font">SMARTCRAFTER</p>', unsafe_allow_html=True)

# App title and introduction
st.title("Smart Contract Generator ₿⛓")
st.sidebar.markdown("### Welcome to the AI-powered Smart Contract Generator!")
st.sidebar.markdown("This app harnesses the power of Gemini to build smart contracts for Web3 projects.")
st.sidebar.markdown("Enter contract requirements and choose a contract language to generate a smart contract for your next Web3 project.")
st.markdown("This app uses Gemini API to generate smart contracts based on the provided details and language.")

# Input fields for contract details and language
contract_det = st.sidebar.text_area("Enter Your Contract Details", height=200)
contract_language = st.sidebar.selectbox("Select Contract Language", ("Solidity", "Vyper", "Ethereum", "Rust", "Move"))

# Function to call Gemini API and generate a smart contract
# def smart_contract(details, language):
#     prompt = f"I am building a project in {language}. The description of the project is below:\n" \
#              f"description: {details}\n\nYour task is to provide code with all the requested features and no bugs. " \
#              "Please provide all the code with notes and explanations of each function."
    
#     headers = {
#         "Content-Type": "application/json"
#     }

#     data = {
#         "contents": [
#             {
#                 "parts": [
#                     {
#                         "text": prompt
#                     }
#                 ]
#             }
#         ]
#     }

#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={gemini_api}"

#     # Spinner while the API request is being processed
#     with st.spinner("Generating your smart contract..."):
#         response = requests.post(url, json=data, headers=headers)

#     if response.status_code == 200:
#         try:
#             # Print the response to understand its structure
#             st.write("Response from API:", response.json())

#             # Safely extract text, checking for the structure
#             json_response = response.json()

#             # Check if 'contents' and 'parts' exist in the response
#             if "contents" in json_response and len(json_response["contents"]) > 0:
#                 parts = json_response["contents"][0].get("parts", [])
#                 if len(parts) > 0:
#                     return parts[0].get("text", "No response text found.")
#                 else:
#                     return "No parts found in the response."
#             else:
#                 return "No contents found in the response."
        
#         except Exception as e:
#             return f"Error while parsing response: {e}"
#     else:
#         return f"Error: {response.status_code} - {response.text}"

def smart_contract(details, language):
    prompt = f"I am building a project in {language}. The description of the project is below:\n" \
             f"description: {details}\n\nYour task is to provide code with all the requested features and no bugs. " \
             "Please provide all the code with notes and explanations of each function."
    
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

    with st.spinner("Generating your smart contract..."):
        response = requests.post(url, json=data, headers=headers)
        st.success('Hooray! Your smart contract has been generated!', icon='🎉')

    if response.status_code == 200:
        try:
            # Print the response to understand its structure
            # st.write("Response from API:", response.json())

            # Safely extract text, checking for the structure
            json_response = response.json()


            # For displaying API response after smart contracts
            global api_response
            api_response = json_response

            # Check if 'candidates' exist in the response
            if "candidates" in json_response and len(json_response["candidates"]) > 0:
                candidate = json_response["candidates"][0]

                # Check if 'content' and 'parts' exist
                if "content" in candidate and "parts" in candidate["content"]:
                    parts = candidate["content"]["parts"]
                    if len(parts) > 0:
                        return parts[0].get("text", "No response text found.")
                    else:
                        return "No parts found in the response."
                else:
                    return "No content or parts found in the response."
            else:
                return "No candidates found in the response."

        except Exception as e:
            return f"Error while parsing response: {e}"
    else:
        return f"Error: {response.status_code} - {response.text}"


# Generate smart contract on button click
if st.sidebar.button("Generate", type="primary"):
    solution = smart_contract(contract_det, contract_language)
    st.markdown(solution)


    # Click to expand section for displaying full API response
    st.markdown("### Full API Response:")
    with st.expander("Click to Expand", expanded=False):
        if api_response:  # Check if API response is not None
            st.json(api_response)  # Display the full API response in a readable format
