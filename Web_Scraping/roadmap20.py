import argparse
import asyncio
from playwright.async_api import async_playwright
from roadmap18 import atualizar_json

def setup_args():
    parser = argparse.ArgumentParser(description="A script to scrape data from a target URL.")
    parser.add_argument("--url", nargs="?" ,help="URL to scrape") #Se quiser um defautl so adicionar default = "https://news.ycombinator.com/"
    parser.add_argument("--headless", action="store_true", help="correr sem mostrar a abrir o website python roadmap20.py --url https://news.ycombinator.com/ --headless")
    parser.add_argument("--delay", type=int, default=5, help="Tempo de espera em segundos (Padrão: 5)")
    parser.add_argument("-o", "--output", default="C:/Users/moises.tavares/Downloads/scripts/Web_Scraping/", help="Output path")
    parser.add_argument("--format", choices=["json", "csv", "txt"], default="json", help="Format")
    return parser.parse_args()

async def scraping(tab1,url):
    try:
        print(f"A ir para: {url}")
        await tab1.goto(url)
        pesquisa_title = tab1.locator(".titleline > a")
        primeiros_titulos = await pesquisa_title.all()
        headlines = primeiros_titulos[:5]
        lista = []
        contador_id=0
        for headline in headlines:
            titulo = await headline.inner_text()
            link = await headline.get_attribute("href")
            contador_id+=1
            if not titulo:
                titulo = "N/A"
            if not link:
                link = "N/A"
                
            dicionario = {
                "id":contador_id,
                "headline": titulo,
                "link" : link
            }
            lista.append(dicionario)
        return lista
    except Exception as e:
        print(f"Erro durante a extração: {e}")
        return []

async def main():
    args = setup_args()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=args.headless)
        context = await browser.new_context()
        tab1 = await context.new_page()
        ficheiro_json_extraido = await scraping(tab1, args.url)
        await tab1.close()
        print(f"A aguardar {args.delay} segundos antes de começar...")
        for segundos in range(args.delay, 0, -1):
            print(f"A aguardar... {segundos}")
            await asyncio.sleep(1)
        print("\nA processar os dados para o cofre JSON...")
        for noticia in ficheiro_json_extraido:
            atualizar_json(noticia)

if __name__ == "__main__":
    asyncio.run(main())

    #Correr assim python roadmap20.py --url https://news.ycombinator.com/