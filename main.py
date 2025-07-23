from tkinter import *
import threading
import speech_recognition as sr
import pyttsx3
from serpapi import GoogleSearch

# --- SERP API Key ---
SERPAPI_API_KEY = "73b0c2f03971d060036b93d93b73782e26147a069385878f3dad989ca596dee0"  # Replace with your actual key

# --- Initialize Text-to-Speech ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def google_search(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }
    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        if "answer_box" in results:
            answer = results["answer_box"].get("answer") or results["answer_box"].get("snippet")
            if answer:
                return answer

        if "organic_results" in results and len(results["organic_results"]) > 0:
            snippet = results["organic_results"][0].get("snippet")
            if snippet and len(snippet.split()) > 6:
                return snippet

    except Exception as e:
        return f"An error occurred: {e}"

    return "Sorry, I couldn't find anything."

def get_audio(prompt=None):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if prompt:
            speak(prompt)
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.WaitTimeoutError:
            return "I didn't hear anything."
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "Speech service is not available."
        except Exception as e:
            return f"Error: {e}"

class Agent:
    def __init__(self, root):
        self.root = root
        self.root.configure(background='orange')
        self.agent_frame = self.create_frame('grey')
        self.create_widgets()
        self.display_widgets()

    def create_frame(self, color):
        return Frame(self.root, bg=color)

    def create_widgets(self):
        self.labels = {
            'userprompt_label': Label(self.agent_frame, text='You said:', bg='grey', fg='light blue'),
            'answerprompt_label': Label(self.agent_frame, text='', bg='grey', fg='light blue'),
            'agent_label': Label(self.agent_frame, text='Jarvis says:', bg='grey', fg='light blue'),
            'agentsprompt_label': Label(self.agent_frame, text='', bg='grey', fg='light blue')
        }

        self.button = {
            'agent': Button(self.agent_frame, text='Activate agent', bg='grey', fg='light blue',
                            width=15, height=1, command=self.activate_voice_thread)
        }

    def display_widgets(self):
        self.agent_frame.grid(row=0, column=0, padx=80, pady=80)
        self.labels['userprompt_label'].grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.labels['answerprompt_label'].grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.labels['agent_label'].grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.labels['agentsprompt_label'].grid(row=3, column=0, sticky='w', padx=10, pady=5)
        self.button['agent'].grid(row=4, column=0, padx=10, pady=10)

    def activate_voice_thread(self):
        threading.Thread(target=self.activate_voice).start()

    def activate_voice(self):
        speak("Jarvis is listening.")
        user_input = get_audio("Ask me something.")
        self.labels['answerprompt_label'].config(text=user_input)

        if "exit" in user_input or "stop" in user_input:
            speak("Goodbye!")
            self.labels['agentsprompt_label'].config(text="Jarvis shutting down.")
        elif user_input.strip():
            response = google_search(user_input)
            speak(response)
            self.labels['agentsprompt_label'].config(text=response)
        else:
            speak("I didn't catch that.")
            self.labels['agentsprompt_label'].config(text="No valid input.")

if __name__ == '__main__':
    master = Tk()
    master.title("Jarvis Voice Agent")
    run = Agent(master)
    master.mainloop()