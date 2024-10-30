import whisper
model = whisper.load_model("large-v3")
result = model.transcribe("../Audio/Andrew Greiner - VP of Enterprise Architecture at BHG.mp3")
print(result["text"])