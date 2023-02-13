def star(n):
    z=1
    while z <= n: # 1부터 5까지
        a=0
        while a<z: # 0부터 z까지
            print("*", end=" ")
            a += 1
        print()
        z += 1

def csum(n):
    sum=0
    for num in range(n+1):
        sum += num
    return sum

def sum(g,f):
    return g+f

print("~4= ",csum(4))
star(3)
print(sum(1,2))


def score(name, *score, **option):
    print(name)
    sum=0
    for s in score:
        sum += s
    print("총점: ", sum)
    if (option['avg'] == True):
        print("평점:", sum/ len(score))

score("백송이",44,53,22,avg=True)
score("백하늘",77,43,32,avg=False)

# isdecimal = 사용자가 입력한 인수가 숫자인지 조사
'''
height = input("키를 입력하세요")
if height.isdecimal():
    print("당신의 키는", height, "cm 입니다.")
else:
    print("숫자 입력 해주세요")
'''

# lower = 영문자 -> 소문자로 변경
s = "HELLO MyFriend"
print(s.lower()) #모두 소문자로
print(s.upper()) #모두 대문자로
print(s.swapcase()) #입력과 반대
print(s.capitalize()) #첫글자만 대문자
print(s.title()) #단어 단락 시작만 대문자

# 공백 자르기 strip
s= "   an gel  "
print(s+"님")
print(s.lstrip()+"님") # 왼쪽 공백만 삭제
print(s.rstrip()+"님") # 오른쪽 공백만 삭제
print(s.strip()+"님") # 양 사이드 공백 삭제

# 문자열 분해 split -> 구분자를 기준으로 문자열을 쪼개 리스트에 저장(기본값: 공백)
s="짜장-짬뽕-라조기"
print(s.split("-"))

# 문자행 나누기 splitlines
t="""강나루 건너서\n 
밀밭 길을 \n\n구름에 달 가듯이\n가는 나그네\n길은 외줄기\n남도 삼백리\n\n술 익는 마을마다\n타는 저녁놀"""
poet=t.splitlines()
for line in poet:
    print(poet)
    
# 문자열 속 각 문자마다 구분자 join
s="99"
print(s.join("비둘기"))

# 문자열 정렬 just, center
m="안녕"
print(m.ljust(10))
print(m.rjust(10))
print(m.center(10))

# 포맷팅
p=500
print("궁금하면 %d원!" % p)

# 리스트 편집
nums = [0,1,2,3,4]
nums[1:3] = [5,6,7] # 1,2 => 5,6,7
print(nums) # [0, 5, 6, 7, 3, 4]
nums[2:3] = [8,9,10,11] # 6 => 8,9,10,11
print(nums) # [0, 5, 8, 9, 10, 11, 7, 3, 4]
nums[1:3] = [] # 5,8 => 삭제
print(nums) # [0, 9, 10, 11, 7, 3, 4]

print("-" * 10)

# 이중리스트, 2차원 배열
lol= [[1,2,3],[4,5],[6,7,8]]
print(lol[0]) # 0번 인덱스의 리스트
print(lol[2][1]) # 2번 인덱스 리스트의 1번 인덱스의 값

for sub in lol: # 리스트 인덱스
    for item in sub: # 리스트 속 값의 인덱스
        print(item, end =' ') # 전부 출력, 구분자 공백
    print() # 리스트 별 개행

print("-" * 10)

# 리스트 컴프리핸션
nums = [n for n in range(1,11)]
print(nums)
for i in nums:
    print(i, end = " ")
print()

nums = [n*2 for n in range(1,11) if n % 4 == 0]
print(nums)
for i in nums:
    print(i, end = " ")
print()

# 리스트 편집
nums = [1,2,3,4]
nums.append(5)
print(nums)
nums.insert(1,33)
print(nums)
nums[1:1] = [44,55] # 1번 인덱스 앞에 추가
print(nums)
nums[3] = [66,77] # 리스트 대입, 리스트는 중첩이 가능, 중첩된 리스트는 하나의 인덱스번호로 묶여진다
print(nums)

nums2=[6,7]
nums.extend(nums2) # 리스트 1 + 리스트 2 추가
print(nums)
print(nums2)

nums.remove(7) # 요청 받은 인수(리스트값) 삭제 => num1 리스트에서 7 삭제
print(nums)
del(nums[0]) # 인덱스 번호대로 삭제
print(nums)
print(nums.pop(0)) # 인덱스 번호대로 요소 삭제
# 리스트 검색
numb=nums.index(55)
print("55는 " + str(numb) + "번째 입니다")

# 리스트 in, not in
"""
ans = input("결제하시겠습니까?")
if ans in ['y','yes','Y', '예']:
    print("결제완료")
else:
    print("결제취소")
"""

# 리스트 정렬
nums2.sort() # 오름차순
print(nums2)
nums2.reverse() # 순서 반대로 뒤집기
print(nums2)
nums2.reverse() # 다시 반대로 뒤집기
print(nums2)
nums2.sort(reverse=True) # 내림차순으로 재정렬
print(nums2)

# 리스트 key인수 편집
country=["america", "CHINA", "korea"]
country.sort()
print(country)
country.sort(key=str.lower) # 전부 소문자로 변경 후 정렬, 하지만 값 자체가 변경되진 않는다. 정렬 시에만 소문자 변환
print(country)

# sorted
score = [100,67,89,90]
score2 = sorted(score) # sort 안먹힘
print(score)
print(score2)

# 튜플 값 교환(swap)
a,b = 12, 34
print(a,b)
a,b = b,a
print(a,b)

# 튜플 사용법
import time

def gettime():
     now = time.localtime()
     return now.tm_hour, now.tm_min

hour, min = gettime()
print("지금은 %d시 %d분 입니다." % (hour,min))

print('-'*10)
#딕셔너리 구조
dic = {'이름':'송이', '성씨':'백', '직장':'모코코'}
print(dic['직장'])
print(dic['이름'])
print('{}의 직장은 {}'.format(dic['이름'],dic['직장']))
print()

# 존재하지 않는 키 검색 시 오류처리
# dics = input('검색할 키를 입력해주세요: ')
# print(dic.get(dics,'검색 실패. 다른 값을 입력해주세요'))

#키 존재 유무 확인
dics = input('사전 검색: ')
if dics in dic:
    print('사전에 있는 단어, {}'.format(dic[dics])) # 사전에 존재 시 결과 출력
else:
    print('사전에 없는 단어')
print()
    
# 사전 값 수정
dic['이름'] = '백송이' # 존재하는 키라면 값 업데이트
dic['부서'] = '미정' # 존재하지 않는 키의 경우 추가
print(dic)
del dic['부서'] # 키 삭제
print(dic)
dic.clear() # 사전 모든 값 삭제
print(dic)
print()

# 요소 출력
dic = {'이름':'송이', '성씨':'백', '직장':'모코코'}
print(dic.keys()) # 키만 출력
print(dic.values()) # 값만 출력
print(dic.items()) # (키,값) 출력
print()

# 사전 리스트화
keylist = dic.keys()
for key in keylist:
    print(key)
print()

# 사전 병합
dic2 = {'엄마':'이연주','아빠':'백경환','언니':'백하늘'}
dic.update(dic2)
print(dic)
print(dic2)

# 2차원 리스트 -> 딕셔너리
li = [['장미','코스모스'],['나무','소나무'],['들꽃','민들레']]
dic = dict(li)
print(li)
print(dic)

# 딕셔너리 활용
song = """I do the same thing, I told you that I never would
I told you I changed, even when I knew I never could
I know that I can't find nobody else as good as you
I need you to stay, need you to stay, yeah"""

al = dict() # 알파벳을 담을 사전 선언
for c in song: # song 변수 동안
    if c.isalpha() == False: # 알파벳이 아니라면
        continue # 건너뛴다
    c = c.lower() # 알파벳 c를 소문자화 한다
    if c not in al: # al 딕셔너리에 알파벳 c가 없다면
        al[c] = 1   #c:1 형태로 추가한다
    else:
        al[c] += 1 # 반대로 있을경우, 1을 더해준다

print(al) # 키 순서 상관없이 출력
# 알파벳대로 키 정렬 -> 출력된 al 정렬
key = list(al.keys()) # 사전의 키 리스트만 뽑아 변수 저장
key.sort() # 그걸 정렬
for c in key: # 키 리스트 동안
    num = al[c] # 알파벳 c의 딕셔너리 값을 저장
    print('{} : {}'.format(c,num)) # 정렬된 출력 확인

# 알파벳대로 키 정렬2 -> a-z까지의 빈도수 알기
for cd in range(ord('a'), ord('z')+1): # 'a'의 아스키코드 값 65 ~ z까지
    c = chr(cd) # 변경한 아스키 코드를 다시 알파벳으로 변경
    num = al.get(c,0) # 키 c의 값을 가져와 num에 넣기 단, 없을 경우 0에 넣을것
    print(c, "=>", num) # 출력