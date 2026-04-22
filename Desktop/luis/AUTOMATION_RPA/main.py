from src.modules.mock import mockuser
from src.register_user.main import User

if __name__ == "__main__":
    usuario = User()

    usuario.ir_para_login()
    usuario.realizar_signup(mockuser)
    usuario.selecionar_mr()
    usuario.preencher_conta(mockuser)
    usuario.preencher_endereco(mockuser)
    usuario.criar_conta()

    #usuario.driver.quit()