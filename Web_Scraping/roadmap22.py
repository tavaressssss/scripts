import schedule
import time

# Conta quantas vezes a extração teve sucesso
successful_runs = 0 
deve_falhar_nesta_ronda = False 

def extrair_dados_instavel():
    global deve_falhar_nesta_ronda
    deve_falhar_nesta_ronda = not deve_falhar_nesta_ronda
    
    if deve_falhar_nesta_ronda:
        raise ConnectionError("O servidor demorou muito a responder (Timeout).")
    
    return "Dados extraídos com sucesso!"

def data_collection_job():
    global successful_runs
    print("\n--- A iniciar tarefa de extração ---")
    
    try:
        resultado = extrair_dados_instavel()
        print(f"[SUCESSO] {resultado}")
        successful_runs += 1
        
    except Exception as erro:
        print(f"[ERRO] A extração falhou nesta ronda: {erro}")
        
    finally:
        # O bloco 'finally' corre SEMPRE, quer tenha havido erro ou não
        print(f"[LOG] Job attempted. Total de sucessos desde o início: {successful_runs}")


def reporting_job():
    print(f"Relatório: O robô teve {successful_runs} extrações bem sucedidas até agora.")

if __name__ == "__main__":
    print("Robô iniciado. Pressiona CTRL+C para parar.")
    
    schedule.every(5).minutes.do(data_collection_job)
    schedule.every(1).hours.do(reporting_job)
    
    # O loop infinito que mantém o script vivo a verificar as horas
    while True:
        schedule.run_pending()
        time.sleep(1) # Dorme 1 segundo para não sobrecarregar o processador