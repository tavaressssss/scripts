#String Methods
numero_string = "42"
texto_linhas = "Primeira linha\nSegunda linha"
price = 2.
tupla = ("John", "Anna")
string = f"  hello, wórld\t!"
molde_string = "Hello, {price:.2f} wórld\t!"
tabela = str.maketrans('h', 'S')

print(f"String  com caracter inicial em maiúscula: {string.capitalize()}")
print(f"String toda em minúscula: {string.casefold()}")
print(f"String centrada: {string.center(30)}")
print(f"Conta o número de vezes que certo valor aparece na string: {string.count("o")}")
print(f"encripta a string com acentos etc: {string.encode()}")
print(f"Retorna a True caso acabe com o caracter certo e False caso o caracter seja diferente do último: {string.endswith("!")}")
print(f"Expande os tabs da string com espaços em branco: {string.expandtabs(2)}")
print(f"Procura um valor específico na string e retorna onde começa: {string.find("wó")}")
print(f"Formata o valor especificado na string: {molde_string.format(price = 49)}")
print(f"Procura na string o valor específicado: {string.index("llo")}")
print(f"Retorna True se todos os carateres forem alfanuméricos: {string.isalnum()}")
print(f"Retorna True se todos os carateres estiverem no alfabeto: {string.isalpha()}")
print(f"Retorna True se todos os carateres estiverem na tabela ascii: {string.isascii()}")
print(f"Retorna True se todos os carateres forem decimais: {string.isdecimal()}")
print(f"Retorna True se todos os carateres forem dígitos: {string.isdigit()}")
print(f"Retorna True se for um identificador (apenas letras, números e sem espaços): {string.isidentifier()}")
print(f"Retorna True se todos os carateres forem lower case: {string.islower()}")
print(f"Retorna True se todos os carateres forem numéricos (-1 e 0.5 não são pois - e . não são numéricos): {string.isnumeric()}")
print(f"Retorna True se todos os carateres forem printáveis (\\n, não é): {string.isprintable()}")
print(f"Retorna True se todos os carateres forem espaços em branco: {string.isspace()}")
print(f"Retorna True se todos os carateres forem lower case menos o primeiro: {string.istitle()}")
print(f"Retorna True se todos os carateres forem upper case: {string.isupper()}")
print(f"Junta os dados de um iterável e coloca os na string: {string}{" # ".join(tupla)}")
print(f"Retorna uma versão justificada à esquerda da minha string: {string} {" Justifica ".ljust(20)}")
print(f"Coloca tudo da string a lower case: {string.lower()}")
print(f"Retira os espaços em branco à esquerda da minha string: {string.lstrip()}")
print(f"Cria uma tabela que pode ser usada com o translate() para substituir coisas: {string.translate(tabela)}")
# partition(): Divide em 3 (antes do separador, o separador, e o depois)
print(f"Divide a string em 3 partes pela 1ª ocorrência ('w'): {string.partition('w')}")
# replace(): Substitui texto
print(f"Substitui um valor por outro: {string.replace('hello', 'adeus')}")
# rfind() e rindex(): Procuram da direita para a esquerda (Right Find)
print(f"Retorna a ÚLTIMA posição onde o valor ('o') foi encontrado: {string.rfind('o')}")
print(f"Igual ao rfind, mas dá erro se não encontrar: {string.rindex('o')}")
# rjust(): Right Justify
print(f"Justifica à direita (preenchendo os 30 espaços com *): {string.rjust(30, '*')}")
# rpartition(): Divide em 3, mas a partir da última ocorrência
print(f"Divide em 3 partes pela ÚLTIMA ocorrência ('o'): {string.rpartition('o')}")
# rsplit(): Divide numa lista começando da direita
print(f"Divide numa lista a partir da direita: {string.rsplit(',')}")
# rstrip(): Right Strip (Remove espaços apenas do final)
# Note que ele vai remover o '\t' que estava no final da sua string!
print(f"Remove espaços/tabs à DIREITA: '{string.rstrip()}'")
# split(): O clássico separador de listas
print(f"Divide a string numa lista usando um separador: {string.split(',')}")
# splitlines(): Útil para ler arquivos de texto com várias linhas
print(f"Divide a string onde houver quebras de linha (\\n): {texto_linhas.splitlines()}")
# startswith(): O oposto do endswith()
print(f"Retorna True se começar com o valor ('  h'): {string.startswith('  h')}")
# strip(): O limpador geral (tira espaços da esquerda E da direita)
print(f"Remove espaços/tabs de AMBOS os lados: '{string.strip()}'")
# swapcase(): Inverte maiúsculas e minúsculas
print(f"Inverte as maiúsculas e minúsculas: {string.swapcase()}")
# title(): Formato de Título
print(f"Converte a 1ª letra de cada palavra em maiúscula: {string.title()}")
# upper(): Tudo maiúsculo
print(f"Converte toda a string para maiúsculas: {string.upper()}")
# zfill(): Zero Fill (Muito usado para formatar números em faturas/IDs)
print(f"Preenche com zeros à esquerda até ter 5 dígitos: {numero_string.zfill(5)}")