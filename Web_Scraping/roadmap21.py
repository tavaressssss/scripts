import json
import os

caminho_ficheiro = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
print(caminho_ficheiro)

def load_config(caminho,defaults):
    config_final = defaults.copy()
    if os.path.exists(caminho):
        with open(caminho, 'r') as file:
            try:
                dados =  json.load(file)
                config_final.update(dados)
                return dados
            except json.JSONDecodeError:
                raise ValueError(f"Configuration file '{caminho}' contains invalid JSON.")
    else:
        print("Aviso: Ficheiro não encontrado, usando apenas os padrões.")
        
    return config_final

if __name__ == "__main__":

    meus_defaults = {
        "max_pages": {"pages": 1},
        "timeout": {"timeout": 300},
        "output_format": {"format": "json"}
    }

    try:
        config = load_config(caminho_ficheiro,meus_defaults)

        bot_config = config.get("max_pages", {})
        pages = bot_config.get("pages",0)

        if pages > 0:
            print(f"Formato final: {config['output_format']['format']}")
            print(json.dumps(config, indent= 4))
        else:
            print("Não tem páginas")
    
    except Exception as e:
        print(f"Erro {e}")