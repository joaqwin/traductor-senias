import boto3
from playsound import playsound
import sys

tts = sys.argv[1]

polly = boto3.client("polly",
                     region_name="us-east-2",
                     aws_access_key_id='AKIA2RIRYNED3VDS5BJR',
                     aws_secret_access_key='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')

text = "<speak><emphasis>{}</emphasis></speak>".format(tts)

response = polly.synthesize_speech(
    Text=text,
    OutputFormat='ogg_vorbis',
    VoiceId='Enrique',
    TextType='ssml',
    #SpeechMarkTypes=["ssml"]
)

audio = response['AudioStream'].read()
with open("helloworld.mp3", "wb") as file:
    file.write(audio)

playsound("helloworld.mp3")

