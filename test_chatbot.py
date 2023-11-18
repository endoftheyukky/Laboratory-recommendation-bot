#辞書データの作成用(スクレイピング)

from bs4 import BeautifulSoup
import requests
url = "https://nyushi.hosei.ac.jp/laboratory/faculty/1"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 研究室情報を格納するための空の辞書を作成します
lab_info_dict = {}

# 各研究室の情報を抽出します
lab_articles = soup.find_all('article')
for article in lab_articles:
    lab_name = article.find('h3').text.strip()
    lab_keywords = [keyword.text.strip() for keyword in article.find_all('li')]
    lab_info_dict[lab_name] = lab_keywords

print(lab_info_dict)

# ポイント記録用の辞書を作成
lab_points ={}
for key in lab_info_dict:
    lab_points[key] = 0#初期値0で設定
#print(lab_points)#確認

import re
l=["人工知能・機械学習"]
word = "人工知能"
for item in l:
    #if "人工知能" in item:
    if item.find(word):
        print(l)
        break
print("人工知能" in l[0])

l=["画像処理"]
if "画像" in l:
    print(l)
print("画像" in l[0])
#==============================================
# 手動で作成した辞書データ

# 教授のデータ
lab_professor_dict ={
    # CSの教授
    "相島 健助":["数値計算研究室", "CF", "CS", "男性", "日本人"],
    "赤石 美奈":["情報編纂研究室", "IS", "CS", "女性", "日本人"],
    "尾花 賢":["情報セキュリティ研究室", "CF", "CS", "男性", "日本人"],
    "佐々木 晃":["プログラミング言語研究室", "IS", "CS", "男性", "日本人"],
    "佐藤 裕二":["知的進化システム研究室", "CF", "CS", "男性", "日本人"],
    "首藤 裕一":["アルゴリズム設計論研究室", "CF", "CS", "男性", "日本人"],
    "日高 宗一郎":["基盤ソフトウェア研究室", "IS", "CS", "男性", "日本人"],
    "廣津 登志夫":["分散システム研究室", "CF", "CS", "男性", "日本人"],
    "黄 潤和":["人工知能研究室", "IS", "CS", "女性"],
    "李 亜民":["コンピュータアーキテクチャ研究室", "IS", "CS", "男性"],
    # DMの教授
    "伊藤 克亘":["音・言語メディア研究室", "MS", "DM", "男性", "日本人"],
    "小池 崇文":["実世界指向メディア研究室", "MS", "DM", "男性", "日本人"],
    "小西 克巳":["高次元データモデリング研究室", "MS", "DM", "男性", "日本人"],
    "佐藤 周平":["コンピュータグラフィックス研究室", "MS", "DM", "男性", "日本人"],
    "善甫 康成":["計算物理研究室", "MS", "DM", "男性", "日本人"],
    "高村 誠之":["メディア情報処理研究室", "MS", "DM", "男性", "日本人"],
    "花泉 弘":["多次元画像処理研究室", "MS", "DM", "男性", "日本人"],
    "藤田 悟":["サービスシステム研究室", "CF", "DM", "男性", "日本人"],#IS入れる?
    "細部 博史":["ユーザインタフェース研究室", "IS", "DM", "男性", "日本人"],
    "馬 建華":["ユビキタスコンピューティング研究室", "IS", "DM", "男性"],
    "雪田 修一":["推論の可視化研究室", "IS", "DM", "男性", "日本人"]
    }

#==============================================
# 作成した関数など
import re

# 略語を置き換えする関数(例 CG→コンピュータグラフィックス)
def put(text):
    #置き換え用辞書
    replacements = {
        "CG":"コンピュータグラフィックス",
        "UI":"ユーザインタフェース",
        "AI":"人工知能",
        "VR":"仮想現実",
        "AR":"拡張現実",
        "HCI":"ヒューマンコンピュータインタラクション",
        "OS":"オペレーティングシステム",
        "ディジタルメディア":"DM",
        "コンピュータ科学":"CS",
        }
    #print('({})'.format('|'.join(map(re.escape, replacements.keys()))))# 確認用
    return re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))),
                  lambda m: replacements[m.group()], text)


# 任意の言葉が任意の辞書に含まれているか確認して加算する関数(研究室情報の辞書用)
def serch(word, dictionary, add):
    word = put(word)# 略語は置き換え
    for key in dictionary:
        serch_list = dictionary[key]#辞書のキーに対応するリストを取り出す
        for item in serch_list:
            #print(item)
            if word in item:#リストに言葉が含まれていたら
                #print(item)
                lab_points[key] += add #ポイントを1加算する
                # break#ポイントの加算上限を1に設定(1加算したら終了する)
                return True
    return False


# 任意の言葉が任意の辞書に含まれているか確認して加算する関数(各教授の辞書用)
def serch_info(word, dictionary, add):
    word = put(word)# 略語は置き換え
    for key in dictionary:
        serch_list = dictionary[key]#辞書のキーに対応するリストを取り出す
        for item in serch_list:
            if word in item:#リストに言葉が含まれていたら
                # dictionary[key][0] は教授に対応する研究室名
                # print(dictionary[key][0])
                lab_points[(dictionary[key][0])] += add
                # 教授の名前から検索をかけてポイントを加算する
                break


    
# 最終的な結果を文章で返す関数
def result_text():
    # ↓ポイントが最大の研究室のリスト(複数個でも対応可)
    result_lab = [kv[0] for kv in lab_points.items() if kv[1] == max(lab_points.values())]
    #result_lab = ["数値計算研究室","音・言語メディア研究室"] # テスト用の値
    result_professor =[] # 研究室に対応する教授の名前
    text = ""
    for lab_name in result_lab:
        for key in lab_professor_dict:
            serch_list = lab_professor_dict[key]#辞書のキーに対応するリストを取り出す
            for n in serch_list:
                if lab_name in serch_list:# リストに言葉が含まれていたら
                    result_professor.append(key) # リストに教授の名前を追加
                    break
    for x in range(len(result_lab)):
        text += result_lab[x] + "(" + result_professor[x] + " 教授)。"
    text = text[:len(text)-1] #最後尾を削除する
    # text = text[:len(text)-2] #最後尾を削除する
    text = "あなたにおすすめの研究室は。" + str(text) + "です。" + "リセットしますか？リセットする場合は何か入力してください。"
    return text

def reset():
    global lab_points
    lab_points = {}
    for key in lab_info_dict:
        lab_points[key] = 0#初期値0で設定
    return lab_points

    
# 関数のテスト用(動作確認済)
#serch("画像", lab_info_dict)
#print(lab_points)

#word = put("画像に興味があります")# →画像に興味があります
#print(word)
#word2 = put("CGに興味があります")# →コンピュータグラフィックスに興味があります
#print(word2)


#for x in range(2):
    #lab_points['数値計算研究室'] += 1
#print(lab_points)

#print(result_text())

# テスト用
#serch_info("MS", lab_professor_dict)
#print(lab_points)

#==============================================
# チャットボット本体

from chatbotweb.chat_server import ChatServer
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter


class MyChatClass():
    BOT_NAME = "A-BOT"
    html = None
    
    def __init__(self):
        self.analyzer = Analyzer(token_filters=[POSKeepFilter(['名詞'])])

class UserClass():
    def __init__(self, chat_obj):
        self.chat_obj = chat_obj
    
    def init_function(self,query_params):
        self.step = 0
        return "あなたにおすすめの研究室を推定します。あなたは何年生ですか？"
    

    def callback_method(self,text,response):
        #設問1 学年について
        if ("1" in text) and (self.step == 0):
            self.step += 1
            return "どのコースを希望していますか？。希望のコースが決まっていない場合は学科を入力してください。",True

        if (("2" in text) or ("3" in text)) and (self.step == 0):
            self.step += 1
            return "どのコースに所属していますか?",True

        #設問2 コースについて
        if ("MS" in put(text)) and (self.step == 1):
            self.step += 1
            serch_info("MS", lab_professor_dict, 1)
            print(lab_professor_dict)
            return "興味のある分野をお答えください。",True

        if ("IS" in put(text)) and (self.step == 1):
            self.step += 1
            serch_info("IS", lab_professor_dict, 1)
            print(lab_professor_dict)
            return "興味のある分野をお答えください。",True

        if ("CF" in put(text)) and (self.step == 1):
            self.step += 1
            serch_info("CF", lab_professor_dict, 1)
            print(lab_professor_dict)
            return "興味のある分野をお答えください。",True

        if ("CS" in put(text)) and (self.step == 1):
            self.step += 1
            serch_info("CS", lab_professor_dict, 1)
            print(lab_professor_dict)
            return "興味のある分野をお答えください。",True

        if ("DM" in put(text)) and (self.step == 1):
            self.step += 1
            serch_info("DM", lab_professor_dict, 1)
            print(lab_professor_dict)
            #return result_text(), False
            return "興味のある分野をお答えください。",True

        #設問3 興味のある分野
        if self.step == 2:
            # 形態素解析かけて名詞を取り出す(複数名詞が含まれている場合に対応)
            nouns = [ token.base_form for token in self.chat_obj.analyzer.analyze(text)]# 取り出した名詞をリストに保存
            #print(nouns)
            before_lab_points = lab_points.copy()# ポイントを保存
            for n in nouns:
                serch(n, lab_info_dict, 1)
            print(lab_points)
            if lab_points != before_lab_points:# ポイントが変化しなかったら
                 self.step += 1
                 return "教授は男性が良いですか?女性が良いですか?", True
            else:
                return "他には？？？？？", True
            #return result_text(), False #結果表示用

        #設問4
        if self.step == 3:
            self.step += 1
            # 形態素解析かけて名詞を取り出す(複数名詞が含まれている場合に対応)
            nouns = [ token.base_form for token in self.chat_obj.analyzer.analyze(text)]# 取り出した名詞をリストに保存
            #print(nouns)
            for n in nouns:
                serch_info(n, lab_professor_dict, 1)
            print(lab_points)
            return result_text(), True #結果表示用
        
        if self.step == 4:
            print("リセットします。")
            reset()
            print("リセットされました。")
            print(lab_points)

            self.step = 0
            return "あなたにおすすめの研究室を推定します。あなたは何年生ですか？", True

        return "もう一度入力してください", True # 入力に不備があった場合
        

        #nouns = [ token.base_form for token in self.chat_obj.analyzer.analyze(text)]
        #if len(nouns) != 0:
            #return "含まれている名詞は、"+str(nouns)+"ですね", True
        #return "名詞が含まれていません", True

if __name__ == '__main__':
    address = "0.0.0.0"
    port = 31029
    chat_server = ChatServer(MyChatClass,UserClass)
    chat_server.start(address,port)