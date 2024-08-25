# AI Voice Assistant

This repository contains a Python script for a voice-activated assistant named Frank. Frank can perform various tasks such as opening applications, browsing the web, taking photos, and more based on voice commands. The assistant uses OpenAI's GPT-3 for responses and incorporates voice recognition and text-to-speech features.

## Features

- **Voice Commands:** Recognizes and processes voice commands.
- **Text-to-Speech:** Provides verbal feedback using pyttsx3.
- **Open Applications:** Opens default software like Calculator, Notepad, etc.
- **Web Browsing:** Opens specified websites.
- **Camera Capture:** Takes photos using the webcam.
- **Location Search:** Opens Google Maps to search for locations.
- **System Commands:** Performs system actions like shutdown, hibernation, and locking the screen.
- **AI Responses:** Generates AI responses and saves them to a file.

## Requirements

- Python 3.x
- Libraries: `pyttsx3`, `pyaudio`, `speech_recognition`, `openai`, `ctypes`, `subprocess`, `ecapture`, `webbrowser`, `os`, `random`, `datetime`, `time`
- OpenAI API Key

## Installation

1. **Install the required libraries:**

   You can install the necessary libraries using pip:

   ```bash
   pip install pyttsx3 pyaudio SpeechRecognition openai ecapture
   ```

2. **Setup OpenAI API Key:**

   - Create a file named `config.py` in the root directory of the project.
   - Add your OpenAI API key to `config.py` in the following format:

     ```python
     apikey = "YOUR_OPENAI_API_KEY"
     ```

## Usage

1. **Run the script:**

   ```bash
   python voice_assistant.py
   ```

   The assistant will start listening for voice commands and will perform actions based on the recognized commands.

2. **Commands:**

   - **Open Applications:** "open calculator", "open notepad"
   - **Web Browsing:** "open youtube", "open google"
   - **Camera Capture:** "take a photo"
   - **Location Search:** "where is [location]"
   - **System Commands:** "shutdown system", "hibernate", "lock window"
   - **AI Responses:** "Frank using artificial intelligence [your prompt]"
   - **Reset Chat:** "Frank reset chat"

3. **Exit the Assistant:**

   Say "bye", "goodbye", "exit", or "quit" to stop the assistant.

## Code Explanation

- **Voice Recognition:** Uses the `speech_recognition` library to capture and recognize voice commands.
- **Text-to-Speech:** Utilizes `pyttsx3` for verbal responses.
- **OpenAI Integration:** Uses GPT-3 for generating responses to prompts.
- **System Actions:** Executes system commands like shutdown, hibernation, and locking.
- **Web and Camera Actions:** Opens websites and takes photos using the webcam.

## Acknowledgments

- OpenAI for providing the GPT-3 model.
- [dlib Models Repository](https://github.com/davisking/dlib-models) for the pre-trained shape predictor.
