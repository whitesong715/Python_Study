from googletrans import Translator # api 임포트

tr = Translator() # Translator() api 객체를 tr에 삽입

str=input("영어로 번역할 한국어를 입력해주세요: ")
str2=input("한국어로 번역할 영어를 입력해주세요: ")

result1= tr.translate(str, dest='en')
result2= tr.translate(str2, dest='ko')

print("한 -> 영 번역결과: ", result1.text)
print("영 -> 한 번역결과: ", result2.text)