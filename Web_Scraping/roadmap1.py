error_list = [0, 3, 5]

string = ""
for i, erro in enumerate(error_list):
    print(f"Index {i} - {erro}")
    
string = ", ".join(str(erro) for erro in error_list)
print(f"A string unida é : {string}")