# SMARTCRAFTER - AI-based Smart Contract Generator


## Overview

The **AI-based Smart Contract Generator** is a Streamlit application that leverages the Gemini API to generate smart contracts for Web3 projects. By inputting contract requirements and selecting the desired programming language, users can quickly obtain a well-structured smart contract, complete with explanations and code comments.

## Features

- **User-friendly Interface**: Easily input contract details and select programming language through a simple sidebar.
- **AI-Powered Generation**: Utilizes Gemini API to generate smart contracts based on user-defined specifications.
- **Real-time Processing**: Displays a loading spinner while generating the contract to enhance user experience.
- **Customizable**: Supports multiple programming languages including Solidity, Vyper, Ethereum, Rust, and Move.

## Technologies Used

- **Streamlit**: For building the web application.
- **Gemini API**: For generating smart contracts based on user input.
- **Python**: The programming language used for the backend logic.
- **PIL (Pillow)**: For image processing in the application.


## Run Locally

Clone the project

```bash
  git clone https://github.com/ayushbhavsar21/SmartCrafter.git
```

Go to the project directory

```bash
  cd smart-contract-generator
```

Create and Activate Virtual Environment

```bash
  python -m venv myenv
  myenv\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create a .env file in the project root directory and add your Gemini API key:

```bash
  GEMINI_API_KEY=your_api_key_here
```

Start the Streamlit server

```bash
  streamlit run main.py
```
## Tech Stacks
- Python 
- Streamlit
- Requests
- Pillow
- python-dotenv
- NLP
- Blockchain

## Usage

1. Open the application in your web browser.
2. In the sidebar, enter your contract details in the text area.
3. Select the desired programming language from the dropdown menu.
4. Click the **Generate** button to create your smart contract.
5. The generated smart contract will be displayed below.

## Authors

- [@ayushbhavsar21](https://github.com/ayushbhavsar21)

