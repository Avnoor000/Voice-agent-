import speech_recognition as sr
import pyttsx3
from serpapi import GoogleSearch


# API KEY
SERPAPI_API_KEY = "73b0c2f03971d060036b93d93b73782e26147a069385878f3dad989ca596dee0" 

# --- Initialize Text-to-Speech ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Male  voice

# Speak function
def speak(text):
    print("Jarvis:", text)
    engine.say(text) # reads text
    engine.runAndWait() # waits for the speech to finish

# Use SerpAPI for Google Search 
def google_search(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }
    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        if "answer_box" in results: # returns the direct answer given
            answer = results["answer_box"].get("answer") or results["answer_box"].get("snippet")
            if answer:
                return answer

        if "organic_results" in results and len(results["organic_results"]) > 0: # retruns a the summary of the fisrt link 
            snippet = results["organic_results"][0].get("snippet")
            if snippet and len(snippet.split()) > 6:  # crude check to ensure it's valid (removes somewords to ensure incomplete sentences)
                return snippet

    except Exception as e:
        return f"An error occurred while searching: {e}"

    return ""

#  Get audio from microphone 
def get_audio(prompt=None):
    recognizer = sr.Recognizer() 
    with sr.Microphone() as source:
        if prompt:
            speak(prompt)  
        # Adjusts for background noise to improve recognition accuracy
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            print("Listening...")  # Indicates the system is actively listening           
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10) # Listens for input with a max wait time of 5 seconds and a phrase limit of 10 seconds        
            text = recognizer.recognize_google(audio) # Converts speech to text using Google's speech recognition API 
            print("You said:", text)  # Displays the recognized speech
            return text.lower()  # Returns the text in lowercase for uniformity

        except sr.WaitTimeoutError:  
            speak("I didn't hear anything.")  
        except sr.UnknownValueError:  
            speak("Sorry, I didn't understand that.")  
        except sr.RequestError:  
            speak("Speech service is not available.")  
        except Exception as e:  
            speak(f"Error: {e}")  

    return "" 

# --- Main loop ---
def run_voice_assistant():
    speak("Jarvis is now online. You can ask your question.")
    while True:
        question = get_audio("What would you like to know?")
        if "exit" in question or "stop" in question:
            speak("Goodbye!")
            break
        if question.strip():
            answer = google_search(question)
            if answer:
                speak(answer)
            else:
                print("No valid answer found.")
        else:
            speak("I didn't catch your question.")
#run_voice_assistant()