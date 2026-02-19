import speech_recognition as sr
import streamlit as st

def capture_speech():
    """
    Captures audio and converts it to text.
    Handles cloud-specific errors where hardware access may be restricted.
    """
    recognizer = sr.Recognizer()
    
    # 1. Configuration: Wait 2 seconds after speech ends before stopping
    recognizer.pause_threshold = 2.0 
    
    try:
        # 2. Accessing the microphone (This requires browser permission on the live site)
        with sr.Microphone() as source:
            st.toast("🎤 Listening... Speak your answer now!")
            
            # Reduce background noise interference
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # Record audio for up to 30 seconds
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
            
            # 3. Convert captured audio to text via Google Web Speech API
            text = recognizer.recognize_google(audio)
            return text
            
    except Exception as e:
        # Fallback error for cloud environments like Render
        st.error("Microphone access is limited on this cloud server.")
        st.info("Tip: If the mic doesn't start, please switch to 'Keyboard' mode in the sidebar.")
        return ""