import flet as ft

def main(page:ft.Page):
    page.title = 'Contador Flet'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    txt_num = ft.TextField(value=0, text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_num.value = str(int(txt_num.value) - 1)
        page.update()

    def add_click(e):
        txt_num.value = str(int(txt_num.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_num,
                ft.IconButton(ft.icons.ADD, on_click=add_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    

if __name__ == '__main__':
    ft.app(main)