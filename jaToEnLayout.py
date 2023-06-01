import placeholders as ph
import flet as ft

def main(page: ft.Page):
    page.title = "TranslateIt!"

    keywords = ft.Ref[ft.TextField]()
    genBtn = ft.Ref[ft.ElevatedButton]()
    

    page.add(
            ft.TextField(ref=keywords, label="Input keword(s)"),
            ft.ElevatedButton(ref=genBtn, text="Generate dialogue")
    )


ft.app(target=main)