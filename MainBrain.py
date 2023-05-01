import openai
import pyttsx3
import speech_recognition as sr
#import time

#importar chave de API open AI

openai.api_key = "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"

#inicializar TTS
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Ferrou meu amigo vamo pula esses erro muito loco!")

#gerar resposta
def generate_response(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt=prompt,
        max_tokens = 4000,
        n=1,
        stop=None,
        temperature = 0.5

        

    )
    return response["choices"][0]["text"]

#transformar resposta em fala
def speak_text(text):
    engine.say(text)

def main():
    #esperar para falar jarvis e detectar voz
    print("Fale Jarvis para fazer sua pergunta!")
    with sr.Microphone() as source:
        recognizer= sr.Recognizer()
        audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if transcription.lower() ==  "jarvis":
                #gravar audio
                filename = "input.wav"
                print("fala ai doido")
                with sr.Microphone() as source:
                    recognizer=sr.Recognizer()
                    source.pause_treshold = 1
                    audio = recognizer.listen(source, phrase_time_limit= None, timeout= None)
                    with open(filename, "wb") as f:
                        f.write(audio.get_wav_data())
                #transformar audio em texto
                text= transcribe_audio_to_text(filename)
                if text:
                    print(f"Você falou: {text}")

                    #gerar resposta usando GPT-3
                    response = generate_response(text)
                    print (f"Jarvis:{response}")

                    #transformar texto em fala
                    speak_text(response)
        except Exception as e:
            print("Ferrou agora deu erro que capotou o meu corsa, aqui ó {}".format(e))

if __name__=="_main_":
    main()