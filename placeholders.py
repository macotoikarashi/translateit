def returnDialogue(keywords="Ghost,High school"):
    return """
    {
  "dialogue": [
    {
      "speaker": "Emily",
      "content": [
        "I can't believe it's been five years since high school.",
        "Do you remember that haunted house on Oak Street?"
      ]
    },
    {
      "speaker": "Ben",
      "content": [
        "Of course I do. The one they said was haunted by a ghost.",
        "But come on, it was just an urban legend, right?"
      ]
    },
    {
      "speaker": "Emily",
      "content": [
        "I'm not so sure anymore. I went back there last night.",
        "I saw something... someone."
      ]
    },
    {
      "speaker": "Ben",
      "content": [
        "Wait, are you serious? What did you see?",
        "Tell me everything."
      ]
    },
    {
      "speaker": "Emily",
      "content": [
        "It was a ghost, Ben. I know it sounds crazy,",
        "but I saw a transparent figure walking through the walls."
      ]
    },
    {
      "speaker": "Ben",
      "content": [
        "This is insane. We have to investigate this together.",
        "If there's really a ghost, we need to find out who it is."
      ]
    }
  ],
  "status": {
    "situation": "Emily and Ben, former high school friends, reunite after five years.",
    "characters": [
      {
        "name": "Emily",
        "description": "A curious and adventurous young woman who believes in the supernatural."
      },
      {
        "name": "Ben",
        "description": "A skeptical and logical guy who relies on facts and evidence."
      }
    ]
  }
}
    """

def returnJapanese(jsontext="..."):
    return """
    {
"dialogue": [
{
"speaker": "Emily",
"content": [
"高校から5年経つなんて信じられないわ。",
"オークストリートにあったあのお化け屋敷覚えてる？"
]
},
{
"speaker": "Ben",
"content": [
"もちろん覚えてるよ。幽霊が出るって言われてたあの場所だろ？",
"でもさ、それって都市伝説だろ？"
]
},
{
"speaker": "Emily",
"content": [
"もうよくわからないわ。昨晩、そこに戻ってきたの。",
"何かを見たの…誰かを。"
]
},
{
"speaker": "Ben",
"content": [
"待って、マジで？何を見たの？",
"全部教えてよ。"
]
},
{
"speaker": "Emily",
"content": [
"幽霊だったわ、Ben。信じられないかもしれないけど、",
"壁を通り抜けて歩いている透明な姿を見たの。"
]
},
{
"speaker": "Ben",
"content": [
"これは狂気だ。一緒に調査しなければならない。",
"もし本当に幽霊がいるなら、その正体を突き止めないといけない。"
]
}
]
}
    """

def returnEvaluation(question="...", correctEx="....", answer="....."):
    return """
        Your translation is almost correct, but there is a slight difference in nuance. Let me explain it in Japanese.

あなたの翻訳はほとんど正しいですが、微妙なニュアンスの違いがあります。以下、日本語で説明します。

「Do you remember that haunted house on Oak Street?」
（オークストリートにあったあのお化け屋敷覚えてる？）

この文は、相手に「オークストリートにあるあのお化け屋敷を覚えているか」と尋ねる表現です。相手が直近にオークストリートに行ったり、そのお化け屋敷を体験したことがあるかどうかを尋ねています。

「Do you remember the haunted house that used to be at Oak Street?」
（オークストリートに以前あったお化け屋敷を覚えていますか？）

一方、あなたの翻訳は「オークストリートに以前あったお化け屋敷を覚えているか」と尋ねています。こちらは相手が過去にオークストリートにあったお化け屋敷を経験したことや、それが現在も存在しているかどうかを尋ねる表現です。

したがって、もし相手がオークストリートに行ったことがなく、お化け屋敷が現在もあるかどうかは知らない場合、あなたの翻訳だと少し意味が異なってしまいます。

正解の翻訳は「Do you remember that haunted house on Oak Street?」です。
    """

if __name__=="__main__":
    print(returnDialogue())
    print(returnJapanese())
    print(returnEvaluation())