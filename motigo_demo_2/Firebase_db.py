import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(r"D:\Motigo\firebase\agile-timing-377213-firebase-adminsdk-y2ns8-785af00be8.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://agile-timing-377213-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

dir = db.reference() # 기본 위치 지정
dir.update({'자동차': ['기아','현대','벤츠']})

dir = db.reference('이동수단/기차')
dir.update({'1번':'ktx'})
dir.update({'2번':'무궁화'})