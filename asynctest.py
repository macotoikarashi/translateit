import flet as ft
import asyncio

async def main(page: ft.Page):
    await page.add_async(ft.Text("Hello,async world!"))

    def page_resize(e):
        print("New page size:", page.window_width, page.window_height)

    page.on_resize = page_resize


    texts = ft.Column()

    async def button_click(e):
        n = len(texts.controls)
        texts.controls.append(ft.Text("Now loading..."))
        await page.update_async()
        await asyncio.sleep(5)
        texts.controls[n].value = "Loaded!"
        await page.update_async()

    await page.add_async(
        ft.ElevatedButton("Let's click!", on_click=button_click),
        texts,
    )

ft.app(target=main)