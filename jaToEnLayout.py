import placeholders as ph
import flet as ft
import json,copy

def main(page: ft.Page):
    page.title = "TranslateIt!"

    keywords = ft.Ref[ft.TextField]()
    genBtn = ft.Ref[ft.ElevatedButton]()

    dia_dict = {}
    trans_dict = {}
    q_dict = {}
    
    def genDia():
        dia_json = ph.returnDialogue(keywords.current.value)
        trans_json = ph.returnJapanese(dia_json)

        global dia_dict
        global trans_dict
        dia_dict = json.loads(dia_json)
        trans_dict = json.loads(trans_json)

        makeQuestion()
    
    def makeQuestion():
        global dia_dict
        global trans_dict
        global q_dict

        




    page.add(
            ft.TextField(ref=keywords, label="Input keyword(s)"),
            ft.ElevatedButton(ref=genBtn, text="Generate dialogue", on_click=genDia)
    )


ft.app(target=main)