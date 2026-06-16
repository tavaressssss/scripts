from pathlib import Path

def input_user_file():

    try:
        while True:
            try:
                lista_ficheiros = []
                current_Dir = Path.cwd()
                for idx, files in enumerate(current_Dir.iterdir(), start=1):
                    if files.is_dir():
                        continue
                    lista_ficheiros.append(files)
                    print(f"Ficheiro {idx} - {files.name}")
                user_Input = (input("Diga o nome / número ou sair para sair: ")).strip()
        
                if user_Input.lower() == "sair":
                    print("A sair!!!")
                    break

                if user_Input.isdigit():
                    escolha_digito = int(user_Input)

                    if 1 <= escolha_digito <= len(lista_ficheiros):
                        caminho_ficheiro = lista_ficheiros[escolha_digito-1]
                    
                    else:
                        print("\nEsse número não corresponde a um ficheiro")
                        input("Press Enter para tentar novamente...")
                        continue
                else:
                    caminho_ficheiro = current_Dir / user_Input

                with open(caminho_ficheiro, 'r', encoding= 'utf-8') as file:
                        file_content = file.read()
                        print(file_content)
                        input("Press Enter to continue...")
                        print("="*40)
                            
            except FileNotFoundError:
                print("ficheiro não encontrado")
                print("="*40)
                continue
                
    except FileExistsError:
        print("Ficheiro não existe")
if __name__ == "__main__":
    input_user_file()