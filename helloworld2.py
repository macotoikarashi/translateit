"""
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
ターミナルで上記を実行することで、現在のPowerShellプロセスに対してのみ、スクリプト実行ポリシーが「Unrestricted」（無制限）に設定されます。
これをやってから
venv\Scripts\activate
すると上手くいきます
"""
"""
helloworld.pyを、Refを使ってリファクタリング
"""

import flet as ft
import time

def main(page: ft.Page):
    page.title = "helloworld2.py"
    

    t = ft.Ref[ft.Text]()
    t2 = ft.Ref[ft.Text]()


    def name_pushed(e):
        if field_name.current.value:
            pushed_names.current.controls.append(ft.Text(field_name.current.value))
            field_name.current.value=""
            page.update()
        field_name.current.focus()
        
    def sw_visible(e):
        row_form.current.visible = cbox.current.value
        page.update()
    
    field_name = ft.Ref[ft.TextField]()
    button_name = ft.Ref[ft.ElevatedButton]()
    row_form = ft.Ref[ft.Row]()
    cbox = ft.Ref[ft.Checkbox]()
    pushed_names = ft.Ref[ft.Column]()
 
    page.add(
        ft.Row(ref=row_form, controls=[
            ft.TextField(ref=field_name, label="Somebody's name", on_submit=name_pushed),
            ft.ElevatedButton(ref=button_name, text="Say my name!", on_click=name_pushed)
        ]),
        ft.Checkbox(ref=cbox, label="Visible", value=True, on_change=sw_visible),
        ft.Column(ref=pushed_names)
    )


    t3 = ft.Ref[ft.Text]()


    page.add(
        ft.Text(ref=t, value="Hello,World!", color="green"),
        ft.Text(ref=t2, value="This is me!", color="red"),
        ft.Text(ref=t3)
    ) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(10):
        t3.current.value = f"Step {i}"
        page.update()
        time.sleep(1)

    page.add(
        ft.Row(controls=[
            ft.Text("I want"),
            ft.Text("to play"),
            ft.Text("the guitar")
        ])
    )

    lines = ft.Ref[ft.Column]()
    page.add(ft.Column(ref=lines))
    for i in range(10+1):
        lines.current.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            lines.current.controls.pop(0)
        page.update()
        time.sleep(0.5)


# open in a native OS window
ft.app(target=main)
# open in a new browser window
# ft.app(target=main, view=ft.WEB_BROWSER)