import csv

list_string = ["name", "lastName","age"]
print("TXT")
with open("headlines.txt", "r+", encoding="UTF-8") as file:
    for row in list_string:
        print(row)
        file.write(f"{row}\n")

print("="*50)
print("CSV")

product = [
    {"name": "moisés", "category": "Portuguese", "price": 19},
    {"name": "tuga", "category": "Brazilian", "price": 200}
    ]

headers = ["name", "category", "price"]
with open("csvfile.csv", "r+", newline = "", encoding="UTF-8") as file_csv:
    writer = csv.DictWriter(file_csv, fieldnames=headers)
    writer.writeheader()
    writer.writerows(product)
    print("Ficheiro criado!")

with open("csvfile.csv", "r+", encoding="UTF-8") as file_csv:
    reader = csv. DictReader(file_csv)
    for linha in reader:
        if float(linha["price"]) > 100:
            print(f"Name: {linha["name"]}, category: {linha["category"]}, {linha["price"]}€")