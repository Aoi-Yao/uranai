import time
import random
import IPython
from google.colab import output
import re


n = 0 
def chat(text, **kw):  #チャット用の関数（ここを書き換える）
  global n
  n += 1
  return 'ほ' * n

# アイコンの指定
BOT_ICON = 'https://3.bp.blogspot.com/-XmtjDKJI8ts/UQuSU6Bc1FI/AAAAAAAALvM/OQNrmsrzyf4/s1600/shoes_38.png'
YOUR_ICON = 'https://1.bp.blogspot.com/-R7bnEXGATis/VnE4Gjay2zI/AAAAAAAA19A/z_jja1C7kRY/s800/pose_kyosyu_girl.png'

def run_chat(chat = chat, start='よかったらまーちの相性占いやってみない？', **kw):

  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', 'まーち')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''
      <style>
        /* 全体 */
        .sb-box {
            position: relative;
            overflow: hidden;
        }

        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }

        /* アイコン画像（左） */
        .icon-img-left {
            left: 0;
        }

        /* アイコン画像（右） */
        .icon-img-right {
            right: 0;
        }

        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
            border: 2px solid #eee;
        }

        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: #385;
            font-size: 12px;
        }

        /* アイコンネーム（左） */
        .icon-name-left {
            left: 0;
        }

        /* アイコンネーム（右） */
        .icon-name-right {
            right: 0;
        }

        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }

        .sb-side-right {
            float: right;
        }

        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 2px solid #eee;
            border-radius: 6px;
            background: #eee;
            color: #333;
            font-size: 15px;
            line-height: 1.7;
            padding: 18px;
        }

        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }

        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }

        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }

        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            border-width: 7px 10px 7px 0;
            border-color: transparent #eee transparent transparent;
        }

        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }

        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent #eee;
        }

        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }

        /* 767px（iPad）以下 */

        @media (max-width: 767px) {

            .icon-img {
                width: 60px;
                height: 60px;
            }

            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 12px;
            }

            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }

            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }

            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: #7fc;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: #eee;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)




def birth(x): #誕生日情報の抽出
  pattern = r'\d\d\d\d/(\d\d?)/(\d\d?)|昭和|平成|令和\d\d?/(\d\d?)/(\d\d?)|\d\d\d\d年(\d\d?)月(\d\d?)日|(\d\d?)/(\d\d?)|(\d\d?)月(\d\d?)日|昭和|平成|令和\d\d?年(\d\d?)月(\d\d?)日|(\d\d?)(\d\d?)|(\d\d?)／(\d\d?)|\d\d\d\d-(\d\d?)-(\d\d?)|(\d\d?)-(\d\d?)|\d\d\d\d(\d\d?)(\d\d?)'
  pattern = re.compile(pattern)
  result_1 = pattern.findall(x)
  result_1 = list(result_1[0])
  result_1 = [i for i in result_1 if i]
  return result_1

def seiza(x): #星座判定
  zod = [["山羊座",12,22],["水瓶座",1,20],["魚座",2,19],["牡羊座",3,21],["牡牛座",4,20],["双子座",5,21],["蟹座",6,22],["獅子座",7,23],["乙女座",8,23],["天秤座",9,23],["蠍座",10,24],["射手座",11,23]]
  for i in range(len(zod)):
    if zod[i][1] == int(x[0]):
      if zod[i][2] <= int(x[1]):
        zod_x = zod[i][0]
        zod_n = i
        break
      else:
        zod_x = zod[i-1][0]
        zod_n = i-1
        break
  return [zod_x,zod_n]

def aishou_friend(w,x,y,z): #友達との相性判定
  a = abs(x[1]-y[1])%4

  if a == 0:
    return x[0]+'の'+w+'と、'+y[0]+'の友達'+z+'さんの相性は最高だよ!!'

  elif a == 1:
    return x[0]+'の'+w+'と、'+y[0]+'の友達'+z+'さんの相性はまあまあかな・・'

  elif a == 2:
    return x[0]+'の'+w+'と、'+y[0]+'の友達'+z+'さんの相性はすごくいいよ!'

  else:
    return x[0]+'の'+w+'と、'+y[0]+'の友達'+z+'さんの相性はかなりいいよ!'

def aishou_love(w,x,y,z): #好きな人との相性判定
  a = abs(x[1]-y[1])%4

  if a == 0:
    return x[0]+'の'+w+'と、'+y[0]+'の好きな人'+z+'さんの相性は最高だよ!!'

  elif a == 1:
    return x[0]+'の'+w+'と、'+y[0]+'の好きな人'+z+'さんの相性はまあまあかな・・'

  elif a == 2:
    return x[0]+'の'+w+'と、'+y[0]+'の好きな人'+z+'さんの相性はすごくいいよ!'

  else:
    return x[0]+'の'+w+'と、'+y[0]+'の好きな人'+z+'さんの相性はかなりいいよ!'

def hantei_1(x): #関係の入力を判定
  y = ['友達','ともだち','friend']
  for i in range(len(y)):
    if y[i] in x:
      a = 0
      break
    else:
      a = 1
  return a

def hantei_2(x): #相手の返答を判定（肯定）
  y = ['はい','Yes','うん','yes','Y','y']
  for i in range(len(y)):
    if y[i] in x:
      z = 0
      break
    else:
      z = 1
  return z
  
  
  
  
  # フレーム 状態をもつ辞書
# 'name1', 'birthday1', 'asking','name2', 'birthday2','relationship','again'
frame = {}

def uranai(input_text):
  global frame # 外部の状態を参照する
  if 'asking' in frame:  # asking から更新する
    frame[frame['asking']] = input_text
    del frame['asking']

  if 'name1' not in frame:
    frame['asking'] = 'name1' # 名前をたずねる  
    return 'あなたの名前を教えてほしいな'

  if 'name1' in frame and 'birthday1' not in frame:
    frame['asking'] = 'birthday1' # 誕生日をたずねる    
    return frame['name1']+'の誕生日はいつ？数字は半角で入力してね'

  if 'birthday1' in frame and 'name2' not in frame:
    frame['asking'] = 'name2' #相手の名前を尋ねる
    return '占いたい相手の名前は？'

  if 'name2' in frame and 'birthday2' not in frame:
    frame['asking'] = 'birthday2' #相手の誕生日を尋ねる
    return '相手の'+frame['name2']+'さんの誕生日はいつ？数字は半角で入力してね'

  if 'birthday2' in frame and 'relationship' not in frame:
    frame['asking'] = 'relationship' #相手との関係を尋ねる
    return frame['name1']+'にとって相手の'+frame['name2']+'さんはどんなひと？？友達？それとも好きな人？'

##占い実行開始

  if 'name1' in frame and 'birthday1' in frame and 'name2' in frame and 'birthday2' in frame and 'relationship' in frame and 'again' not in frame:

    a = hantei_1(frame['relationship'])
    
    if a == 0:
      x = seiza(birth(frame['birthday1']))
      y = seiza(birth(frame['birthday2']))
      frame['asking'] = 'again'
      return aishou_friend(frame['name1'],x,y,frame['name2'])+'もう一度占いたい？？'

    else:
      x = seiza(birth(frame['birthday1']))
      y = seiza(birth(frame['birthday2']))
      frame['asking'] = 'again'
      return aishou_love(frame['name1'],x,y,frame['name2'])+'もう一度占いたい？？'


  if 'name1' in frame and 'birthday1' in frame and 'name2' in frame and 'birthday2' in frame and 'relationship' in frame and 'again' in frame:
    b = hantei_2(frame['again'])
    if b == 0:
      del frame['name2']
      del frame['birthday2']
      del frame['relationship']
      del frame['again']
      return 'わかった、ありがとう！もう一回占うね、相手の情報を入力してね'
    
    else:
      return 'わかった、ありがとう！またね～'

    return output_text

def start():
  run_chat(chat=uranai)
