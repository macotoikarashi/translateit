import asyncio,random
import openai

def returnDialogue(keywords,key):
    openai.api_key = key

    content = """
        ##task##
According to following keywords,brainstorm and set status situation and characters,then output a 200 words English dialogue between two people in the flavor of a Netflix drama script.
Output must be JSON format including "dialogue" and "status" key.
Items of "dialogue" key must include "speaker" and "content" key.Value of "content" key must be an array.Store one sentence per element in that array.
"status" key must include "situation" and "charasters".All elements in "characters" must include "name" and "description".

##keywords##
{}

##output##
    """.format(keywords)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role":"user",
                "content":content,
            }],
            temperature=1.0,
        )

        return {"response":response,"error":None}
    except openai.error.OpenAIError as e:
        return {"response":None,"error":e}



def returnJapanese(jsontext,key):
    openai.api_key = key

    content = """
        ##task##
You are Japanese popular scenario writer.According to value of status within following input JSON data,please translate all "content" values into Japanese.All values without "content" must not be translated.Output must be JSON format and include only "dialogue" key."dialogue" key must have same structure as input.

##input##
{}

##output##
    """.format(jsontext)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role":"user",
                "content":content,
            }],
            temperature=1.0,
        )

        return {"response":response,"error":None}
    except openai.error.OpenAIError as e:
        return {"response":None,"error":e}



def returnEvaluation(situation,question, correctEx, answer,key):
    openai.api_key = key

    content = """
        ##task##
You are an experienced and friendly English teachers.
I am trying to translate Japanese sentence into English.Please evaluate and explain my translation.In addition to that, please explain the nuances between my translation and the correct answer example, if they are not an exact match.
Your output must be JSON format including "isgood" and "evaluate" keys."isgood" must be boolian that represents if my translation is good or not."evaluate" must be text of your evaluation and elplaining.The text of "evaluate" must be Japanese.

##Situation of the dialogue##
{}
##Japanese sentence##
{}
##Correct answer example##
{}
##My translation##
{}

##output##
    """.format(situation,question, correctEx, answer)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role":"user",
                "content":content,
            }],
            temperature=1.0,
        )

        return {"response":response,"error":None}
    except openai.error.OpenAIError as e:
        return {"response":None,"error":e}


def randomKeywords(n):
    kws = ['Impala', '天井', 'Yodel', 'カーペット', '鳥籠', 'ラップトップ', 'Grapes', '雨具', 'イチゴ', '紅茶', 'Jungle', 'バスタオル', 'Sloth', '虹', 'コーヒー', '鉄', 'Panda', 'Kilogram', 'Maracas', 'バラ', '扉', 'ココア', 'Yucca', '日差し', 'Asteroid', '電話', 'ノート', '火花', '森林', 'Zinnia', 'Walrus', 'スプーン', 'アイスクリーム', '花火', 'キャンプ', 'レモン', 'Waffle', '春', '飛行船', 'ファイル', 'Ultraviolet', 'Orchid', 'Weasel', 'シューズ', 'クレヨン', '時間', '天使', 'Zodiac', 'Molecule', 'Eggplant', 'Kettle', '足跡', '海岸線', 'Watermelon', 'Coconut', 'Unicorn', 'Juggler', '本棚', 'Pineapple', 'Butterfly', 'Raspberry', 'リース', 'Quilt', 'Galaxy', 'サラダ', '椅子', 'ネックレス', 'ハンガー', 'バスケット', 'Otter', '霧', '水滴', 'ナッツ', 'Lion', 'Ninja', '冷蔵庫', '壷', '塔', '朝日', 'エコー', 'ブランコ', 'メモ', 'Elephant', 'Kiwi', 'Goose', 'パンダ', '鳥', 'Volcano', 'ヘリコプター', 'フォーク', 'イルカ', 'スプレー', 'アンテナ', 'Ostrich', 'Beetle', 'Leopard', 'Kettlebell', 'ベッド', 'Tambourine', '台所', 'リボン', 'Kangaroo', 'Ocelot', 'ポット', '皿', 'Hawk', 'Mitten', '貝殻', 'Jumper', 'Tuna', 'Gecko', 'ベーグル', '砂糖', 'バレンタイン', 'メロディ', 'Jacket', 'Iguana', 'テーブル', 'Lemon', 'Yew', 'Yo-yo', '塀', 'コミック', 'Uranus', 'Balloon', 'Lighthouse', 'ハイビスカス', 'ピザ', 'ソファ', 'Yacht', 'Koala', 'スパゲティ', 'トレッドミル', '錠前', 'Zeppelin', 'Lynx', 'Urchin', 'シャンプー', 'Rainbow', '夏', 'Cherry', 'Pomegranate', 'スパイス', 'ユニコーン', 'Iceberg', 'シロップ', 'ワイン', '飛行機', 'デッキ', 'Shark', '家族', '風見鶏', '雲', 'Zephyr', '新聞', '鉛筆', '栗', '石像', '雪', 'Lamp', '遊園地', 'Banjo', 'Hedgehog', '森', 'ライオン', 'Vulture', 'Donkey', 'イヤリング', 'Goldfish', 'クリスマス', 'Rooster', '燭台', '蝶', 'Robot', '網戸', '海', 'Zucchini', 'Lychee', 'Velociraptor', 'Zoo', 'ハンバーガー', 'Island', 'Apple', 'ビスケット', 'Hummingbird', '妖精', 'Raven', '風', 'Yam', 'Squirrel', 'Rose', '雪だるま', 'Orange', 'ベンチ', 'Carrot', 'Ice', 'エレベーター', 'Jasmine', 'Parrot', 'パスポート', 'Toucan', 'Violin', '水晶球', 'Lark', 'Cello', '花', 'ブロッコリー', 'ハイキング', 'Raccoon', 'Icicle', 'オリーブオイル', '昼寝', 'トランペット', '靴下', 'Turtle', 'Guava', 'Antelope', 'ドアノブ', '指', '雪景色', '絨毯', 'ドレッシング', 'Jalapeno', 'Dolphin', 'テーブルクロス', '塩', 'Racoon', 'Spaceship', 'サングラス', '蛍', '桟橋', 'おもちゃ', 'Bison', 'アワビ', 'Quasar', 'ボート', 'Satellite', 'クッキー', 'Blueberry', 'ピクニック', 'ピアノ', '八角', 'レンガ', '蝋燭', 'ハンモック', '蛍光灯', 'ウェーブ', 'Olive', '日傘', 'Lemur', 'Heron', '砂漠', 'Rabbit', 'Xylophone', '部屋', '犬', 'Nun', 'Lizard', 'Jazz', 'ボールペン', 'ガーデン', 'Lemonade', '野球', 'Rocket', 'Orangutan', 'Noodle', 'リモコン', '寝具', '火山', '梨', 'Tangerine', 'Kumquat', 'Lilac', 'Cactus', 'ヨーグルト', 'キノコ', '遊び場', 'Yak', '絆創膏', 'Mango', 'ひまわり', 'ガラス', 'Licorice', '月面', 'Strawberry', 'Ox', 'ゴミ箱', 'Tulip', 'Tricycle', '音符', 'ビーチボール', '茶碗', '花瓶', 'Ukulele', 'ピラミッド', 'バレーボール', 'Octopus', '冬', '火', 'Mandolin', 'パンプキン', 'ハロウィン', 'プラスチック', 'ペンダント', 'ソーダ', 'Tiger', '窓', 'Walnut', 'バタフライノット', '川', 'Lantern', 'Hyena', '猫', 'Telescope', 'Lute', '雪原', 'トンネル', '廊下', '風船', '蛸', 'スクリュー', 'Moth', 'Ladder', '天窓', '水玉', 'Pillow', '音楽', 'Giraffe', 'タクシー', 'Nectarine', 'ビーチ', 'Flamingo', 'アクアリウム', '星座', 'Zebra', 'Penguin', 'ボール', 'Hippopotamus', 'Circus', 'Gorilla', 'シャワー', 'Gazelle', '夕焼け', 'レコード', 'インク', 'スケートボード', 'Yoga', 'Harmonica', '冬眠', 'ベル', '赤ちゃん', '電球', '鏡', '泥棒', 'ペン', 'Oyster', '紙飛行機', 'リンゴ', '魚', 'Nebula', 'Ogre', 'Jigsaw', 'Nimbus', 'マグネット', '雲海', 'Lobster', 'Banana', '魔法使い', 'Vase', 'Venus', '紙', 'Vanilla', 'カップ', 'Rattlesnake', 'Kitten', 'Hippo', 'Viking', '石鹸', '扇風機', '歯ブラシ', 'Wolf', 'シャベル', 'Topaz', 'ハチ', 'ブラシ', '宝石', 'Binoculars', 'Eagle', 'ビーズ', 'Accordion', 'Dinosaur', 'フェンス', 'キツネ', 'パン', 'ティーポット', 'ドラム', 'サンドイッチ', 'ギター', 'Umbrella', 'トースト', 'ピアス', 'コート', 'Yeti', 'コイン', 'ダンボール', 'Iris', 'チーズ', 'Jellyfish', 'Grapefruit', 'Saxophone', '鍵', '帽子', 'Peach', 'Jade', 'Vampire', '雨', 'Osprey', '帯', 'Narwhal', 'Guitar', 'エプロン', '煙突', 'ハンドル', '葉', '蝶々', 'Yardstick', '星', 'タオル', 'Navigator', '木', 'Rhinoceros']
    rndkws = random.sample(kws,n)
    return rndkws

json_error_placeholder = {
    "dialogue":[
        {
            "speaker": "作者",
            "content": [
                "APIとの連携エラーです。",
                "申し訳ありませんが、リトライしてみてください。"
            ]
        }
    ],
    "status":{
        "situation": "Which is wrong,me or chatGPT API?",
    "characters": [
      {
        "name": "作者",
        "description": "developer of this app"
      },
      {
        "name": "chatGPT",
        "description": "I love it"
      }
    ]
    }
}