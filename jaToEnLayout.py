import placeholders as ph
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
        self.dia_dict = json.loads(dia_json) if dia_json else {}
        self.trans_dict = json.loads(trans_json) if trans_json else {}
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
    


def main(page: ft.Page):
    page.title = "TranslateIt!"

    keywords = ft.Ref[ft.TextField]()
    genBtn = ft.Ref[ft.ElevatedButton]()
    q = ft.Ref[ft.Column]()
    qTxt = ft.Ref[ft.Column]()
    userAnswer = ft.Ref[ft.TextField]()
    ansBtn = ft.Ref[ft.ElevatedButton]()
    a = ft.Ref[ft.Column]()
    aJa = ft.Ref[ft.Text]()
    aUser = ft.Ref[ft.Text]()
    aEvaluation = ft.Ref[ft.Text]()

    # dia_json = ""
    # trans_json = ""
    # dia_dict = {}
    # trans_dict = {}
    # q_dict = {}
    
    # def genDia():
    #     global dia_json,trans_json,dia_dict,trans_dict
    #     #global trans_json
    #     #global dia_dict
    #     #global trans_dict
        
    #     dia_json = ph.returnDialogue(keywords.current.value)
    #     trans_json = ph.returnJapanese(dia_json)

    #     dia_dict = json.loads(dia_json)
    #     trans_dict = json.loads(trans_json)

    #     makeQuestion()
    
    # def makeQuestion():
    #     global dia_dict,trans_dict,q_dict
    #     x = random.randint(0,len(dia_dict["dialogue"])-1)
    #     y = random.randint(0,len(dia_dict["dialogue"][x]["content"])-1)

    data = DialogueData()


    def genDia(e):
        dia_json = ph.returnDialogue(keywords.current.value)
        trans_json = ph.returnJapanese(dia_json)
        data.set(dia_json,trans_json)
        data.set_question()
        qTxt.current.clean()
        qTxt.current.controls = makeDiaText(data.q_dict["dialogue"])
        q.current.visible = True
        page.update()
        

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
                        ft.Text(speaker, width=100,text_align="CENTER"),
                        ft.Text(
                            dia[i]["content"][j],
                            weight=ft.FontWeight.BOLD if isBold else ft.FontWeight.NORMAL
                        )
                    ])
                )
        return res

    def evaluateAns(e):
        eval = ph.returnEvaluation(situation=data.q_dict["status"]["situation"],question=data.q_japanese(), correctEx=data.q_english, answer=userAnswer.current.value)
        eval_dict = json.loads(eval)
        aJa.current.value = data.q_japanese()
        aUser.current.value = userAnswer.current.value
        aEvaluation.current.value = eval_dict["evaluate"]
        a.current.visible = True
        page.update()


    page.add(
            ft.TextField(ref=keywords, label="Input keyword(s)", width=600),
            ft.ElevatedButton(ref=genBtn, text="Generate dialogue", on_click=genDia),
            ft.Column(ref=q,controls=[
                ft.Divider(),
                ft.Column(ref=qTxt),
                ft.TextField(ref=userAnswer,label="Traslate into English", width=600),
                ft.ElevatedButton(ref=ansBtn,text="Answer", on_click=evaluateAns)
            ], visible=False),
            ft.Column(ref=a,controls=[
                ft.Divider(),
                ft.Row(controls=[
                    ft.Text("問題文：", width=100,text_align="CENTER"),
                    ft.Text(ref=aJa),
                ]),
                ft.Row(controls=[
                    ft.Text("あなたの回答：", width=100,text_align="CENTER"),
                    ft.Text(ref=aUser),
                ]),
                ft.Row(controls=[
                    ft.Text("解説：", width=100,text_align="CENTER"),    
                    ft.Text(ref=aEvaluation, width=500)
                ], vertical_alignment=ft.CrossAxisAlignment.START),
            ],visible=False)
    )


ft.app(target=main)