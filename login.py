import flet as ft

def main(page: ft.Page):
    page.title = 'Tela de login'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    usuario = ft.TextField(label='Usuario',width=300)
    senha = ft.TextField(label='Senha',password=True,can_reveal_password=True,width=300)
    mensagem = ft.Text("",color="red")

    def entrar(e):
        if usuario.value == "admin" and senha.value == "1234":
            mensagem.value = "Login bem-sucedido!"
            mensagem.color = "green"
        else:
            mensagem.value = "Usuario ou senha invalida"
            mensagem.color = "red"
            page.update()
    btn_login = ft.ElevatedButton("Entrar", on_click=entrar)
    page.add(ft.Column([ft.Text("Sistema de Login",size=24,weight="bold"),
                        usuario,senha,btn_login,mensagem],
                        alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,))
ft.app(target=main)