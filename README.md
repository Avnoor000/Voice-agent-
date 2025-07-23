# Voice-agent-

A simple voice-controlled personal assistant powered by Python's speech_recognition, pyttsx3, and Google's search API via SerpAPI. This assistant listens to your voice, performs a Google search, and responds using text-to-speech.

🎯 Features
🎤 Voice Input: Uses your microphone to listen to commands.

🔍 Google Search: Answers queries using SerpAPI.

🗣️ Voice Output: Responds with speech using pyttsx3.

🖥️ GUI Interface: Simple tkinter GUI with button control.

💬 Multithreaded: Uses threading to keep the UI responsive.

🛠️ Tech Stack
Python 3.x

Tkinter — for GUI

speech_recognition — for converting speech to text

pyttsx3 — for text-to-speech

serpapi — for fetching search results from Google

threading — for non-blocking speech processing

🚀 Getting Started
🔧 Prerequisites
Make sure you have Python 3 and pip installed.

Install the required packages:

bash
Copy
Edit
pip install pyttsx3 SpeechRecognition serpapi
You'll also need PyAudio for microphone input:

On Windows: pip install pipwin && pipwin install pyaudio

On macOS: brew install portaudio && pip install pyaudio

On Linux: sudo apt-get install python3-pyaudio

🔑 SerpAPI Key
This app uses SerpAPI to perform Google searches.
Get your free API key from: https://serpapi.com/

Replace the following line in the code with your key:

python
Copy
Edit
SERPAPI_API_KEY = "your_api_key_here"
🧪 Running the App
The GUI will launch. Click "Activate agent" to start talking to Jarvis.

📁 Project Structure
bash
Copy
Edit
jarvis-voice-agent/
├── jarvis.py        # Main application file
├── README.md        # This file

⚠️ Known Issues
Background noise may affect recognition accuracy.

Slow/unstable internet may affect SerpAPI responses.

SerpAPI usage is rate-limited on free accounts.

🧩 Future Improvements
Add command-based responses (e.g., "open notepad", "what's the time")

Use OpenAI/GPT for smarter replies

Improve error handling and microphone calibration

Add wake word detection (e.g., "Hey Jarvis")

📝 License
This project is licensed under the MIT License.
See LICENSE for details.

🙋‍♂️ Author
Avnoor Singh
Feel free to connect or contribute!
