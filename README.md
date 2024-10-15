
# Grogu - Voice Activated Virtual Assistant

**Grogu** is a Python-powered virtual assistant designed to listen to voice commands and perform tasks like telling jokes, playing music on YouTube, retrieving stock prices, and more. It provides a simple, interactive experience for users looking to automate tasks through voice commands.

## Features
- **Play music on YouTube** with voice commands.
- **Tell jokes** to entertain the user.
- **Search Wikipedia** for information.
- **Provide the current time** and day of the week.
- **Open a web browser** for easy access to the internet.
- **Fetch current stock prices** using Yahoo Finance.

## Setup Instructions

### Step 1: Create a Virtual Environment

It's highly recommended to run this project in a virtual environment to manage dependencies efficiently.

```sh
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.env\Scriptsctivate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate
```

### Step 2: Install Dependencies

Once the virtual environment is activated, you can install the necessary dependencies by running:

```sh
pip install -r requirements.txt
```

Alternatively, you can install each module individually:

- **pyttsx3**: Text-to-speech engine
  ```sh
  pip install pyttsx3
  ```
- **speech_recognition**: Recognizes voice input
  ```sh
  pip install speech_recognition
  ```
- **webbrowser**: Web browser controller
  ```sh
  pip install webbrowser
  ```
- **pywhatkit**: Play YouTube videos and more
  ```sh
  pip install pywhatkit
  ```
- **datetime**: Get the current time and date
  ```sh
  pip install datetime
  ```
- **os**: Interact with the operating system
  ```sh
  pip install os
  ```
- **yfinance**: Fetch stock data from Yahoo Finance
  ```sh
  pip install yfinance
  ```
- **wikipedia**: Access information from Wikipedia
  ```sh
  pip install wikipedia
  ```
- **pyjokes**: Generate jokes
  ```sh
  pip install pyjokes
  ```

### Step 3: Run the Application

After installing the required modules, you can run the virtual assistant using:

```sh
python grogu_assistant.py
```

## Current Functionality (Version 1)

- **Play music** via YouTube.
- **Tell jokes** to keep you entertained.
- **Search for information** on Wikipedia.
- **Provide the current time** and day of the week.
- **Open a web browser** with voice commands.
- **Provide stock prices** from Yahoo Finance.

## Recommendations
For best performance, it's advised to use the virtual assistant in a quiet environment for better voice recognition accuracy.
