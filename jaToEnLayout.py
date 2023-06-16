# import placeholders as ph
import chatRequest as cr
import flet as ft
import json,copy,random

class DialogueData:
    def __init__(self,dia_json="",trans_json="") -> None:
        self.dia_json = dia_json
        self.trans_json = trans_json
        self.dia_dict = json.loads(dia_json) if dia_json else {}
        self.trans_dict = json.loads(trans_json) if trans_json else {}
        self.x = 0
        self.y = 0
        self.q_dict = {}

    def set(self,dia_json,trans_json):
        self.dia_json = dia_json
        self.trans_json = trans_json
        try:
            self.dia_dict = json.loads(dia_json) if dia_json else {}
        except json.JSONDecodeError as e:
            self.dia_dict = cr.json_error_placeholder
        
        try:
            self.trans_dict = json.loads(trans_json) if trans_json else {}
        except json.JSONDecodeError as e:
            self.dia_dict = cr.json_error_placeholder
        self.x = 0
        self.y = 0
        self.q_dict = {}

    def set_question(self):
        self.x = random.randint(0,len(self.dia_dict["dialogue"])-1)
        self.y = random.randint(0,len(self.dia_dict["dialogue"][self.x]["content"])-1)
        self.q_dict = copy.deepcopy(self.dia_dict)
        self.q_dict["dialogue"][self.x]["content"][self.y] = copy.copy(self.trans_dict["dialogue"][self.x]["content"][self.y])

    def q_english(self):
        if self.q_dict and self.q_dict["dialogue"][self.x]["content"][self.y]==self.trans_dict["dialogue"][self.x]["content"][self.y]:
            return self.dia_dict["dialogue"][self.x]["content"][self.y]
        else:
            return False
    def q_japanese(self):
        if self.q_dict and self.q_dict["dialogue"][self.x]["content"][self.y]==self.trans_dict["dialogue"][self.x]["content"][self.y]:
            return self.trans_dict["dialogue"][self.x]["content"][self.y]
        else:
            return False
    


async def main(page: ft.Page):
    page.title = "TranslateIt!"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    apikey = ft.Ref[ft.TextField]()
    keywords = ft.Ref[ft.TextField]()
    genBtn = ft.Ref[ft.ElevatedButton]()
    q_loading = ft.Ref[ft.Row]()
    q = ft.Ref[ft.Column]()
    qTxt = ft.Ref[ft.Column]()
    userAnswer = ft.Ref[ft.TextField]()
    ansBtn = ft.Ref[ft.ElevatedButton]()
    a_loading = ft.Ref[ft.Row]()
    a = ft.Ref[ft.Column]()
    aJa = ft.Ref[ft.Text]()
    aUser = ft.Ref[ft.Text]()
    correctEx = ft.Ref[ft.Text]()
    aEvaluation = ft.Ref[ft.Text]()

    data = DialogueData()


    loadingBar = ft.Column(controls=[
        ft.Text("Now Processing...", style="headlineSmall"),
        ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
    ], width=600,horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def disableWhenLoading(sw=True):
        keywords.current.disabled = sw
        genBtn.current.disabled = sw
        userAnswer.current.disabled = sw
        ansBtn.current.disabled = sw if sw else not userAnswer.current.value

    async def resetWhenError():
        # for Errors at generating Question
        disableWhenLoading(False)
        q_loading.current.visible = False
        q.current.visible = False
        a_loading.current.visible = False
        a.current.visible = False
        keywords.current.value = ""
        qTxt.current.controls = []
        userAnswer.current.value = ""
        aJa.current.value = ""
        aUser.current.value = ""
        correctEx.current.value = ""
        aEvaluation.current.value = ""
        page.dialog = ft.AlertDialog(
            title=ft.Text("APIエラーのため、リセットしました"), on_dismiss=lambda e: print("Dialog dismissed!"),
            open=True
        )
        await page.update_async()

    async def retryWhenError():
        # for Errors at generating Evaluation
        disableWhenLoading(False)
        a_loading.current.visible = False
        a.current.visible = False
        aJa.current.value = ""
        aUser.current.value = ""
        correctEx.current.value = ""
        aEvaluation.current.value = ""
        page.dialog = ft.AlertDialog(
            title=ft.Text("APIエラー リトライしてみてください"), on_dismiss=lambda e: print("Dialog dismissed!"),
            open=True
        )
        await page.update_async()


    

    async def genDia(e):
        if not keywords.current.value:
            # keywords.current.value = ",".join(ph.randomKeywords(3))
            keywords.current.value = ",".join(cr.randomKeywords(3))
        
        disableWhenLoading()
        qTxt.current.controls = []
        q_loading.current.visible = True
        q.current.visible = False
        a.current.visible = False
        userAnswer.current.value = ""
        await page.update_async()
        await page.scroll_to_async(offset=-1.0, duration=300)

        # dia_json = await ph.returnDialogue(keywords.current.value)
        dia_obj = cr.returnDialogue(keywords.current.value, apikey.current.value)
        if dia_obj["error"]:
            await resetWhenError()
            return False
        print("dia:\n",dia_obj["response"])
        dia_json = dia_obj["response"].choices[0].message.content
        # trans_json = await ph.returnJapanese(dia_json)
        trans_obj = cr.returnJapanese(dia_json, apikey.current.value)
        if trans_obj["error"]:
            await resetWhenError()
            return False
        print("trans:\n",trans_obj["response"])
        trans_json = trans_obj["response"].choices[0].message.content
        data.set(dia_json,trans_json)
        data.set_question()
        qTxt.current.controls = makeDiaText(data.q_dict["dialogue"])
        disableWhenLoading(False)
        q_loading.current.visible = False
        q.current.visible = True
        await page.update_async()
        await page.scroll_to_async(offset=-1.0, duration=300)        

    def makeDiaText(dia):
        res = []
        for i in range(len(dia)):
            for j in range(len(dia[i]["content"])):
                if j==0:
                    speaker = dia[i]["speaker"]
                else:
                    speaker = " " * (len(dia[i]["speaker"]))
                if i==data.x and j==data.y:
                    isBold = True
                else:
                    isBold = False
                res.append(
                    ft.Row(controls=[
                        ft.Text(speaker, width=100,text_align="CENTER", selectable=True),
                        ft.Text(
                            dia[i]["content"][j],
                            width=500,
                            weight=ft.FontWeight.BOLD if isBold else ft.FontWeight.NORMAL,
                            selectable=True
                        )
                    ])
                )
        return res

    async def evaluateAns(e):
        disableWhenLoading()
        a_loading.current.visible = True
        a.current.visible = False
        await page.update_async()
        await page.scroll_to_async(offset=-1.0, duration=300)

        eval_obj = cr.returnEvaluation(situation=data.q_dict["status"]["situation"],question=data.q_japanese(), correctEx=data.q_english, answer=userAnswer.current.value, key=apikey.current.value)
        if eval_obj["error"]:
            await retryWhenError()
            return False
        print("eval:\n",eval_obj["response"])
        eval = eval_obj["response"].choices[0].message.content
        try:
            eval_dict = json.loads(eval)
            aJa.current.value = data.q_japanese()
            aUser.current.value = userAnswer.current.value
            aUser.current.color = "green" if eval_dict["isgood"] else "red"
            correctEx.current.value = data.dia_dict["dialogue"][data.x]["content"][data.y]
            aEvaluation.current.value = eval_dict["evaluate"]
            disableWhenLoading(False)
            a_loading.current.visible = False
            a.current.visible = True
            await page.update_async()
            await page.scroll_to_async(offset=-1.0, duration=300)
        except json.JSONDecodeError as e:
            await retryWhenError()

    async def controlGenBtn(e):
        genBtn.current.disabled = not apikey.current.value
        await page.update_async()

    async def controlAnsBtn(e):
        ansBtn.current.disabled = not userAnswer.current.value
        await page.update_async()

    await page.add_async(
        ft.Column(controls=[
            ft.Container(
                content=ft.Text(""),
                height=50,
            ),
            ft.Text("ひとこと英訳問題を、AIが出題してくれます。Let's try!",style=ft.TextThemeStyle.TITLE_LARGE),
            ft.TextField(ref=apikey, label="OpenAI API keyを入力", width=600, password=True, on_change=controlGenBtn),
            ft.TextField(ref=keywords, label="Input keyword(s)/キーワードを入力", width=600),
            ft.ElevatedButton(ref=genBtn, text="問題を作成", on_click=genDia, disabled=True),
            ft.Row(ref=q_loading,controls=[loadingBar], visible=False),
            ft.Column(ref=q,controls=[
                ft.Divider(),
                ft.Text("下記の会話文の、太字の日本語を英訳してください。",style=ft.TextThemeStyle.TITLE_MEDIUM),
                ft.Column(ref=qTxt),
                ft.TextField(ref=userAnswer,label="太字を英文に翻訳してください", width=600, on_change=controlAnsBtn),
                ft.ElevatedButton(ref=ansBtn,text="回答する", on_click=evaluateAns, disabled=True)
            ], visible=False),
            ft.Row(ref=a_loading,controls=[loadingBar], visible=False),
            ft.Column(ref=a,controls=[
                ft.Divider(),
                ft.Text("AIによる解説です。",style=ft.TextThemeStyle.TITLE_MEDIUM),
                ft.Text("※解説はLLMによる自動生成です。正確性・精度は保証されておりません。あしからず。",style=ft.TextThemeStyle.LABEL_SMALL),
                ft.Row(controls=[
                    ft.Text("問題の文：", width=100,text_align="LEFT"),
                    ft.Text(ref=aJa, width=500, selectable=True),
                ]),
                ft.Row(controls=[
                    ft.Text("あなたの回答：", width=100,text_align="LEFT"),
                    ft.Text(ref=aUser, width=500, selectable=True),
                ]),
                ft.Row(controls=[
                    ft.Text("正解例：", width=100,text_align="LEFT"),
                    ft.Text(ref=correctEx, width=500, selectable=True),
                ]),
                ft.Row(controls=[
                    ft.Text("解説：", width=100,text_align="LEFT"),    
                    ft.Text(ref=aEvaluation, width=500, selectable=True)
                ], vertical_alignment=ft.CrossAxisAlignment.START),
            ],visible=False),
            ft.Container(
                content=ft.Text(""),
                height=50,
            )
        ],width=600)
    )


ft.app(target=main)