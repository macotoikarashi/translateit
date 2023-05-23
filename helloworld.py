"""
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
ターミナルで上記を実行することで、現在のPowerShellプロセスに対してのみ、スクリプト実行ポリシーが「Unrestricted」（無制限）に設定されます。
これをやってから
venv\Scripts\activate
すると上手くいきます
"""


import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text(value="Hello,World!", color="green")
    t2 = ft.Text(value="This is me!", color="red")

    def name_pushed(e):
        if field_name.value:
            pushed_names.controls.append(ft.Text(field_name.value))
            field_name.value=""
            page.update()
        field_name.focus()
        
    def sw_visible(e):
        row_form.visible = cbox.value
        page.update()
    
    field_name = ft.TextField(label="Somebody's name", on_submit=name_pushed)
    button_name = ft.ElevatedButton(text="Say my name!", on_click=name_pushed)
    row_form = ft.Row(controls=[
            field_name,
            button_name,
        ])
    cbox = ft.Checkbox(label="Visible", value=True, on_change=sw_visible)
    pushed_names = ft.Column()
 
    page.add(row_form, cbox, pushed_names)
    # page.add(cbox)
    # page.add(pushed_names)


    t3 = ft.Text()

    # page.controls.append(t)
    # page.controls.append(t2)
    page.add(t, t2, t3) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(10):
        t3.value = f"Step {i}"
        page.update()
        time.sleep(1)

    page.add(
        ft.Row(controls=[
            ft.Text("I want"),
            ft.Text("to play"),
            ft.Text("the guitar")
        ])
    )

    lines = ft.Column()
    page.add(lines)
    for i in range(10+1):
        lines.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            lines.controls.pop(0)
        page.update()
        time.sleep(0.5)


# open in a native OS window
ft.app(target=main)
# open in a new browser window
# ft.app(target=main, view=ft.WEB_BROWSER)