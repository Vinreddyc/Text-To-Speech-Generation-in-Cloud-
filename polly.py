import boto3
from pprint import pprint

polly = boto3.client('polly', region_name="us-east-1")
s3 = boto3.resource('s3')
BUCKET = "s3-gradproject-bucket"

def generate_audio_ssml(text):
    response = polly.synthesize_speech(Engine='neural', Text=text, TextType='ssml', VoiceId='Joanna', OutputFormat='mp3')
    body = response['AudioStream'].read()
    file_name = 'voice.mp3'
    with open(file_name,'wb') as file:
        file.write(body)
        file.close()
    for inst in s3.buckets.all():
        pprint(inst)
    s3.Bucket(BUCKET).upload_file(file_name, file_name)

if __name__ == "__main__":


    #generate_audio_ssml('<speak> This is my example 1. <break time="1s"/> He was caught up in the game.<break time="1s"/> In the middle of the 10/3/2014 <sub alias="World Wide Web Consortium">W3C</sub> meeting, he shouted, "Nice job!" quite loudly. When his boss stared at him, he repeated <amazon:effect name="whispered">"Nice job,"</amazon:effect> in a whisper. <break time="1s"/> End of example 1.</speak>')

    # Please test these for different SSML tags

    generate_audio_ssml('<speak> This is my example 2. I can speak in cardinals. Your number is <say-as interpret-as="cardinal">10</say-as>. Or I can speak in ordinals. You are <say-as interpret-as="ordinal">10</say-as> in line. Or I can even speak in digits. The digits for ten are <say-as interpret-as="characters">10</say-as>. </speak>')
    #generate_audio_ssml('<speak> <prosody rate="x-slow"><prosody volume="loud">This is my example 3.</prosody></prosody> Here are <say-as interpret-as="characters">SSML</say-as> samples. I can also substitute phrases, like the <sub alias="World Wide Web Consortium">W3C</sub>. Finally, I can speak a paragraph with two sentences. <p><s>This is sentence one.</s><s>This is sentence two.</s></p></speak>')