"""
Web Interface for Gujarati Text-to-Speech using Streamlit
Run with: streamlit run app.py
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

import streamlit as st

from gujarati_tts import GujaratiTTS


def launch_streamlit_app():
    """Start the app through the Streamlit runtime when launched directly."""
    project_root = Path(__file__).resolve().parent
    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(project_root / "app.py"),
        "--server.headless",
        "true",
        "--server.port",
        "8501",
    ]
    try:
        subprocess.run(cmd, cwd=str(project_root), check=False)
    except Exception as exc:
        print(f"[ERROR] Failed to start Streamlit: {exc}")


if __name__ == "__main__" and "streamlit" not in sys.modules:
    launch_streamlit_app()
    raise SystemExit(0)


# Page configuration
st.set_page_config(page_title="Gujarati TTS", page_icon="🔊", layout="wide")

# Initialize TTS Engine
@st.cache_resource
def get_tts_engine():
    return GujaratiTTS(allow_online_fallback=True)

tts = get_tts_engine()

# Header
st.title("🔊 Gujarati Text-to-Speech Converter")
st.markdown("An AI/ML project to convert Gujarati text into natural speech using Neural Text-to-Speech synthesis.")

# Main Layout
tab1, tab2, tab3 = st.tabs(["🎯 Convert Text", "📚 Examples", "ℹ️ About"])

# TAB 1: Convert Text
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        gujarati_text = st.text_area(
            "📝 Enter Gujarati Text:",
            placeholder="નમસ્તે, આ એક ગુજરાતી ટેક્સ્ટ ટુ સ્પીચ પ્રોજેક્ટ છે।",
            height=200
        )
    
    with col2:
        st.markdown("### Actions")
        if st.button("▶️ Generate & Play Audio", use_container_width=True, type="primary"):
            if gujarati_text.strip():
                with st.spinner("Generating Neural Audio..."):
                    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
                    temp_path = temp_file.name
                    temp_file.close()

                    success = tts.text_to_speech(gujarati_text, output_file=temp_path)

                    if success:
                        st.success("✅ Audio generated successfully!")
                        with open(temp_path, "rb") as audio_file:
                            audio_bytes = audio_file.read()
                            st.audio(audio_bytes, format="audio/mpeg")

                        st.download_button(
                            label="📥 Download Audio File",
                            data=audio_bytes,
                            file_name="gujarati_speech.mp3",
                            mime="audio/mpeg",
                            use_container_width=True,
                        )

                        try:
                            os.unlink(temp_path)
                        except OSError:
                            pass
                    else:
                        st.error("❌ Failed to generate audio. Please check your internet connection.")
            else:
                st.warning("⚠️ Please enter some Gujarati text first.")

    # Show live statistics
    if gujarati_text:
        st.markdown("---")
        st.markdown("**Text Statistics:**")
        stat_col1, stat_col2 = st.columns(2)
        stat_col1.metric("Character Count", len(gujarati_text))
        stat_col2.metric("Word Count", len(gujarati_text.split()))

# TAB 2: Examples
with tab2:
    st.header("📚 Example Gujarati Phrases")
    examples = {
        "Greeting": "નમસ્તે, આપ કેમ છો?",
        "About AI": "આર્ટિફિશિયલ ઇંટેલિજન્સ ભવિષ્યનું ભાષા છે।",
        "Language": "ગુજરાતી આપણી સુંદર ભાષા છે।",
        "Technology": "તકનોલોજી આપણા જીવનને બદલી રહી છે।"
    }
    
    for title, text in examples.items():
        st.markdown(f"**{title}:** {text}")

# TAB 3: About
with tab3:
    st.header("ℹ️ Project Information")
    st.markdown("""
    ### AI/ML Mini Project
    This project demonstrates Natural Language Processing (NLP) and Speech Synthesis fundamentals by converting native Gujarati Unicode text into natural-sounding audio waveforms.
    
    **Concepts Demonstrated:**
    * Text tokenization and Unicode parsing
    * Neural Text-to-Speech (TTS) Synthesis
    * Web Application Development using Streamlit
    """)