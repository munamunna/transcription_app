


import gradio as gr
import openai

openai.api_key = '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'

def transcribe(audio):
    print(audio)
    audio_file = open(audio, "rb")
    transcript = openai.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print(transcript)
    return transcript.text

ui = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(sources="microphone", type="filepath"),
    outputs="text"
)

ui.launch()



