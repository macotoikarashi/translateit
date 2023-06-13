import asyncio

async def returnDialogue(keywords="Ghost,High school"):
    await asyncio.sleep(10)
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

async def returnJapanese(jsontext="..."):
    await asyncio.sleep(5)
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

async def returnEvaluation(situation="..",question="...", correctEx="....", answer="....."):
    await asyncio.sleep(8)
    return """
{
  "isgood": true,
  "evaluate": "あなたの翻訳は正しいです。この文脈では、「Do you remember the haunted house that used to be at Oak Street?」という表現が適切です。EmilyとBenは高校の友人であり、5年ぶりに再会した状況です。そのため、相手がオークストリートにあったお化け屋敷を覚えているかどうかを尋ねるのが適切です。あなたの翻訳と正解例との違いは微妙ですが、ニュアンス的にはほとんど変わりません。素晴らしい翻訳ですね!"
}
    """

if __name__=="__main__":
    print(returnDialogue())
    print(returnJapanese())
    print(returnEvaluation())