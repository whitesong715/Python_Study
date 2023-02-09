import os
from google.cloud import translate

credential_path = r"D:\Motigo\agile-timing-377213-220487b64b90.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


# cloud 번역 지원 언어 출력
def get_supported_languages(project_id="agile-timing-377213"):
    """Getting a list of supported language codes."""

    client = translate.TranslationServiceClient()

    parent = f"projects/{project_id}"

    # Supported language codes: https://cloud.google.com/translate/docs/languages
    response = client.get_supported_languages(parent=parent)

    # List language codes of supported languages.
    print("Supported Languages:")
    for language in response.languages:
        print('{}: {}'.format(language.display_name, language.language_code))


def translate_text_with_model(target, text, model="nmt"):
    """Translates text into the target language.

    Make sure your project is allowlisted.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target, model=model)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


#get_supported_languages()

target= "ko"
text = input("번역할 내용 입력: ")
translate_text_with_model(target, text)

target= "en"
text = "안녕하세요"
translate_text_with_model(target, text)