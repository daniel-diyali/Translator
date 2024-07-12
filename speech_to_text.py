# The following program transcribes an audio file into text
from openai import OpenAI

client = OpenAI(
    api_key = "API Key"
)

audio_file = open("spanish_audio.m4a", "rb")
audio_file2 = open("japanese_audio.m4a","rb");
audio_file3 = open("french_audio.m4a","rb");

transcript = client.audio.translations.create(
    model = "whisper-1",
    file = audio_file
)

transcript2 = client.audio.translations.create(
    model = "whisper-1",
    file = audio_file2
)

transcript3 = client.audio.translations.create(
    model = "whisper-1",
    file = audio_file3
)

print("Spanish -> English: " + transcript.text)
print("Japanese -> English: " + transcript2.text)

print("French -> English: " + transcript3.text)