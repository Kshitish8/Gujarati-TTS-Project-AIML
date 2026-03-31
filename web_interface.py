"""
Web Interface for Gujarati Text-to-Speech using Streamlit
Run with: streamlit run web_interface.py
"""

import streamlit as st
from gujarati_tts import GujaratiTTS
import os
import tempfile

# Page configuration
st.set_page_config(
    page_title="Gujarati TTS",
    page_icon="🔊",
    layout="wide"
)

# Title and description
st.title("🔊 Gujarati Text-to-Speech Converter")
st.markdown("""
A web-based AI/ML project to convert Gujarati text into natural speech.
Using **pyttsx3** for offline text-to-speech synthesis.
""")

# Initialize session state
if 'tts' not in st.session_state:
    st.session_state.tts = GujaratiTTS()

tts = st.session_state.tts

# Sidebar with options
st.sidebar.header("⚙️ Settings")

# Speech rate
rate = st.sidebar.slider("Speech Rate (words/min)", 50, 300, 185)
tts.engine.setProperty('rate', rate)

# Volume
volume = st.sidebar.slider("Volume", 0.0, 1.0, 1.0)
tts.engine.setProperty('volume', volume)

# Main content area
tab1, tab2, tab3 = st.tabs(["🎯 Convert Text", "📚 Examples", "ℹ️ About"])

# Tab 1: Text Conversion
with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        gujarati_text = st.text_area(
            "📝 Enter Gujarati Text:",
            placeholder="નમસ્તે, આ એક ગુજરાતી ટેક્સ્ટ ટુ સ્પીચ પ્રોજેક્ટ છે।",
            height=150
        )
    
    with col2:
        st.markdown("### Actions")
        
        col_play, col_save = st.columns(2)
        
        with col_play:
            if st.button("▶️ Play Sound", use_container_width=True):
                if gujarati_text.strip():
                    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
                        temp_path = tmp.name

                    progress_placeholder = st.empty()
                    result_placeholder = st.empty()
                    
                    progress_placeholder.info("⏳ Generating audio... (max 15 seconds)")
                    
                    success = tts.text_to_speech(
                        gujarati_text,
                        output_file=temp_path,
                        play=False,
                        timeout=15
                    )
                    
                    progress_placeholder.empty()
                    
                    if success and os.path.exists(temp_path):
                        try:
                            with open(temp_path, 'rb') as f:
                                audio_bytes = f.read()
                            if audio_bytes:
                                st.audio(audio_bytes, format='audio/wav')
                                result_placeholder.success("✅ Audio ready! Click play button above.")
                            else:
                                result_placeholder.error("❌ Audio file is empty")
                        except Exception as e:
                            result_placeholder.error(f"❌ Error reading file: {str(e)}")
                    else:
                        result_placeholder.error("❌ Conversion failed or timed out. Try shorter text.")

                    try:
                        os.remove(temp_path)
                    except OSError:
                        pass
                else:
                    st.warning("⚠️ Please enter some text")
        
        with col_save:
            if st.button("💾 Save Audio", use_container_width=True):
                if gujarati_text.strip():
                    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
                        temp_path = tmp.name

                    progress_placeholder = st.empty()
                    result_placeholder = st.empty()
                    
                    progress_placeholder.info("⏳ Generating audio... (max 15 seconds)")
                    
                    success = tts.text_to_speech(
                        gujarati_text,
                        output_file=temp_path,
                        play=False,
                        timeout=15
                    )
                    
                    progress_placeholder.empty()
                    
                    if success and os.path.exists(temp_path):
                        try:
                            with open(temp_path, 'rb') as f:
                                audio_data = f.read()
                            if audio_data:
                                st.download_button(
                                    label="📥 Download WAV",
                                    data=audio_data,
                                    file_name="gujarati_audio.wav",
                                    mime="audio/wav"
                                )
                                result_placeholder.success("✅ Audio ready for download!")
                            else:
                                result_placeholder.error("❌ Audio file is empty")
                        except Exception as e:
                            result_placeholder.error(f"❌ Error: {str(e)}")
                    else:
                        result_placeholder.error("❌ Conversion failed or timed out. Try shorter text.")

                    try:
                        os.remove(temp_path)
                    except OSError:
                        pass
                else:
                    st.warning("⚠️ Please enter some text")
    
    # Statistics
    if gujarati_text:
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Characters", len(gujarati_text))
        with col2:
            st.metric("Words", len(gujarati_text.split()))
        with col3:
            estimated_duration = len(gujarati_text.split()) * 60 / rate
            st.metric("Est. Duration (sec)", f"{estimated_duration:.1f}")

# Tab 2: Examples
with tab2:
    st.header("📚 Example Gujarati Texts")
    
    examples = {
        "Greeting": "નમસ્તે, આપ કેમ છો?",
        "About AI": "આર્ટિફિશિયલ ઇંટેલિજન્સ ભવિષ્યનું ભાષા છે।",
        "Language": "ગુજરાતી આપણી સુંદર ભાષા છે।",
        "Education": "શિક્ષા એ જીવનનો આધાર છે।",
        "Technology": "તકનોલોજી આપણા જીવનને બદલી રહી છે।"
    }
    
    for title, text in examples.items():
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.write(f"**{title}:** {text}")
        
        with col2:
            if st.button("🔊", key=f"play_{title}"):
                with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
                    temp_path = tmp.name

                progress_placeholder = st.empty()
                result_placeholder = st.empty()
                
                progress_placeholder.info("⏳ Converting (max 15s)...")
                
                success = tts.text_to_speech(text, output_file=temp_path, play=False, timeout=15)
                
                progress_placeholder.empty()
                
                if success and os.path.exists(temp_path):
                    try:
                        with open(temp_path, 'rb') as f:
                            audio_data = f.read()
                        if audio_data:
                            st.audio(audio_data, format='audio/wav')
                            result_placeholder.success("✅ Ready!")
                        else:
                            result_placeholder.error("❌ Empty file")
                    except Exception as e:
                        result_placeholder.error(f"❌ {str(e)}")
                else:
                    result_placeholder.error("❌ Failed")

                try:
                    os.remove(temp_path)
                except OSError:
                    pass

# Tab 3: About
with tab3:
    st.header("ℹ️ Project Information")
    
    st.markdown("""
    ### Overview
    This is an AI/ML project for the subjects:
    - Artificial Intelligence
    - Machine Learning
    - Natural Language Processing
    
    ### Technology Stack
    - **Language**: Python 3.8+
    - **TTS Engine**: pyttsx3 (offline synthesis)
    - **Framework**: Streamlit (web interface)
    - **Target Language**: Gujarati (ગુજરાતી)
    
    ### Features
    ✅ Real-time text-to-speech conversion  
    ✅ Adjustable speech rate and volume  
    ✅ Audio file download capability  
    ✅ Support for Gujarati Unicode text  
    ✅ Batch processing capability  
    ✅ No API keys required (offline processing)  
    
    ### How It Works
    1. Text is input by the user in Gujarati
    2. pyttsx3 engine converts text to phonetic representation
    3. System TTS synthesizes audio from phonetics
    4. Audio is played or saved as a file
    
    ### Getting Started
    ```bash
    # Install dependencies
    pip install -r requirements.txt
    
    # Run web interface
    streamlit run web_interface.py
    
    # Or run CLI
    python gujarati_tts.py
    ```
    
    ### Project Structure
    - `gujarati_tts.py` - Main TTS converter class
    - `test_gujarati_tts.py` - Unit tests
    - `web_interface.py` - Streamlit web app
    - `requirements.txt` - Dependencies
    - `README.md` - Full documentation
    
    ---
    **Submitted for AI/ML Subject**
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center'>"
    "<p>🔊 Gujarati Text-to-Speech Converter | AI/ML Project</p>"
    "</div>",
    unsafe_allow_html=True
)   