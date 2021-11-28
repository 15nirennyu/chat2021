#お砂場
import requests
import re
import datetime
today = str((datetime.date.today())).replace("-","")
def aisyou(a,b):
  return(abs(4-abs(a-b)))
def soulnumber(pon):
  ponst = str(pon)
  while True:
    ponsou = int(0)
    for x in range(len(ponst)):
      ponsou += int(ponst[x])
    if ponsou < 10:
      break
    ponst = str(ponsou)
  return ponsou
def kyounoaisyou():
  jibun = re.sub("\D","",input("自分の生年月日を入力してね"))
  jibunname = str(input("自分の名前を入力してね"))
  aite = re.sub("\D","",input("占いたい相手の生年月日を入力してね"))
  aitename = str((input("相手の名前を入力してね")))
  score = int(jibun+aite+today)%9#判別用なので表示には使わない
  print("今日の{}さんと{}さんの相性は{}点です".format(jibunname,aitename,score*5+60))
def kyounounsei():
  jibun = re.sub("\D","",input("自分の生年月日を入力してね"))
  jibunname = str(input("自分の名前を入力してね"))
  jibunun = soulnumber(jibun)
  todayun = soulnumber(today)
  score = aisyou(jibunun,todayun)
  kitisouko = ("アルティメット大吉","ウルトラ大吉","ハイパー大吉","スーパー大吉","大吉")
  print("今日の{}さんの運勢は{}です".format(jibunname,kitisouko[score]))
#-------------------------------------------------------ここまで準備
print("これから占いをするよ\n今日の相性占いがしたかったら相性占い\n今日の運勢占いがしたかったら今日の占いって入力してね")
nyuryoku = input()
if nyuryoku == "a":#これは相性
  kyounoaisyou()
elif nyuryoku == "b":
  kyounounsei()
r = requests.get("https://opentdb.com/api.php?amount=1&category=27&difficulty=medium&type=boolean")
data = r.json()
print("今日のトリビア")
print(data['results'][0]["question"],"\n",data['results'][0]["correct_answer"])
