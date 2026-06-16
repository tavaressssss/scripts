import shutil
from pathlib import Path
import time

def organize_downloads():
    base_path = Path.cwd()
    before = 7 *24 *60* 60
    now = time.time()
    extension_map = {
        '.pdf': 'Web_Scraping_Documents',
        '.txt': 'Web_Scraping_Documents',
        '.jpg': 'Web_Scraping_Documents_Images',
        '.png': 'Web_Scraping_Documents_Images',
        '.zip': 'Web_Scraping_Documents_Archives',
        '.csv': 'Web_Scraping_Documents_CSV'
    }

    for file in base_path.iterdir():
        if file.is_dir():
            continue
        if file.suffix.lower() == '.py':
            continue

        file_Temp= Path(file).stat().st_mtime

        folder_name = extension_map.get(file.suffix.lower(), 'Others')
        target_folder = base_path / folder_name
        target_folder.mkdir(exist_ok=True)

        if (now - file_Temp) < before:
            caminho_destino = target_folder / file.name
            if not (target_folder / file.name).exists():
                shutil.move(str(file), str(target_folder / file.name))
                print(f"Moved {file.name} to {folder_name}/")
            else: 
                inc = 1
                
                while True:
                    novo_nome = f"{file.stem}_{inc}{file.suffix}"
                    caminho_destino = target_folder / novo_nome
                    
                    if not caminho_destino.exists():
                        shutil.move(file, caminho_destino)
                        print(f"Movido (Renomeado): {file.name} -> {novo_nome}")
                        break
                        
                    inc += 1

if __name__ == "__main__":
    organize_downloads()