from pathlib import Path

current_dir = Path.cwd()

data_file = current_dir / "logs"
data_file1 = current_dir / "data"
data_file2 = current_dir / "exports"

folders_list = [data_file, data_file1, data_file2]
print("Criar pastas")

for folder in folders_list:
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)
        print(f"Pasta {folder} criada!")
    else:
        print(f"Pasta {folder} já existe")

print("="*50)
print("Pathlib")

for file in current_dir.glob("*.csv"):
    print(f"O ficheiro é este: {file}")

print("="*50)
print("size, path, parent")

specific = current_dir / "roadmap5.py"

print(f"Caminho absoluto: {specific.resolve()}")
print(f"Tamanho: {specific.stat().st_size}")
print(f"Pai: {specific.parent.name}")