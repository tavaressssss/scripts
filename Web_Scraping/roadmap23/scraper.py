import argparse

def main():
    parser = argparse.ArgumentParser(description="A minha ferramenta global de web scraping.")
    parser.add_argument("--url", default="https://news.ycombinator.com/", help="O URL alvo")
    parser.add_argument("--delay", type=int, default=2, help="Segundos de espera")
    
    args = parser.parse_args()

    print(f"Extrator iniciado")
    print(f"Alvo: {args.url}")
    print(f"A aguardar {args.delay} segundos por segurança...")
    print("Extração concluída com sucesso! (Simulação)")

if __name__ == "__main__":
    main()