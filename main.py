from src.modules.mock import mockuser
from src.register_user.main import User
from src.navigation.main import Navigation
from time import sleep
from src.navigation.contact_us import ContactUs

def main():
    usuario = User()
    usuario.ir_para_login()
    usuario.realizar_signup(mockuser)
    login = Navigation(usuario.wait)

    if usuario.usuario_ja_existe():
        print("Usuário já existe → fazendo login")
        login.realizar_login(mockuser)
        usuario.fechar_ads(usuario.wait)
    else:
        print("Usuário novo → completando cadastro")
        usuario.preencher_conta(mockuser)
        usuario.preencher_endereco(mockuser)
        usuario.criar_conta()

    sleep(3)
    #login.realizar_logout()
    contact = ContactUs(usuario.wait)
    contact.ir_para_contact()
    contact.preencher_formulario(
        mockuser,
        r"C:\Users\etech\Desktop\luis\AUTOMATION_RPA\banner-reclamacoes.png"
    )
    contact.enviar()
    contact.validar_sucesso()
    usuario.fechar_ads(usuario.wait)
    sleep(1)
    usuario.fechar_ads(usuario.wait)
    login.go_tests_cases()


if __name__ == "__main__":
    main()
