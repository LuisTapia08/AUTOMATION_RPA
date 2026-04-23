from src.modules.mock import mockuser
from src.register_user.main import User
from src.login_user.main import LoginUser
from time import sleep

if __name__ == "__main__":
    usuario = User()

    usuario.ir_para_login()
    usuario.realizar_signup(mockuser)
    login = LoginUser(usuario.wait)

    if usuario.usuario_ja_existe():
        login.realizar_login(mockuser)
        sleep(5)
        usuario.delete_account()
        
    else:
        usuario.selecionar_mr()
        usuario.preencher_conta(mockuser)
        usuario.preencher_endereco(mockuser)
        usuario.criar_conta()
    sleep(3)
    usuario.driver.quit()