import os
from google.cloud import translate

credential_path = "agile-timing-377213-220487b64b90.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def detect_language(content, project_id="agile-timing-377213"):
    """Detecting the language of a text string."""

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    response = client.detect_language(
        content= content,
        parent=parent,
        mime_type="text/plain"
    )

    for language in response.languages:
        if(language.language_code == 'ko' or language.language_code == 'en'):
            if(language.language_code == 'ko'):
                translate_text_with_model("en", content)
            elif (language.language_code == 'en'):
                translate_text_with_model("ko", content)
        else:
            print("한글이나 영어만 입력하세요")
            continue

# 번역
def translate_text_with_model(target, text, model="nmt"):

    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target, model=model)
    print(result)

    #print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    #print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))




content = input("번역할 문자열 입력: ")
detect_language(content)