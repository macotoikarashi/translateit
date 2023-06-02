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
        if (not self.q_dict) and self.q_dict["dialogue"][self.x]["content"][self.y]==self.trans_dict["dialogue"][self.x]["content"][self.y]:
            return self.dia_dict["dialogue"][self.x]["content"][self.y]
        else:
            return False
    def q_japanese(self):
        if (not self.q_dict) and self.q_dict["dialogue"][self.x]["content"][self.y]==self.trans_dict["dialogue"][self.x]["content"][self.y]:
            return self.trans_dict["dialogue"][self.x]["content"][self.y]
        else:
            return False
    


def main(page: ft.Page):
    page.title = "TranslateIt!"

    keywords = ft.Ref[ft.TextField]()
    genBtn = ft.Ref[ft.ElevatedButton]()
    qTxt = ft.Ref[ft.Column]()

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
        page.update()
        

    def makeDiaText(dia):
        res = []
        for i in range(len(dia)):
            for j in range(len(dia[i]["content"])):
                if j==0:
                    speaker = dia[i]["speaker"]
                else:
                    speaker = " " * (len(dia[i]["speaker"]))
                res.append(
                    ft.Row(controls=[
                        ft.Text(speaker, width=100,text_align="CENTER"),
                        ft.Text(dia[i]["content"][j])
                        ],
                        )
                )
        return res

    page.add(
            ft.TextField(ref=keywords, label="Input keyword(s)"),
            ft.ElevatedButton(ref=genBtn, text="Generate dialogue", on_click=genDia),
            ft.Column(ref=qTxt)
    )


ft.app(target=main)