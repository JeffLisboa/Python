import difflib


with open('arquivo1.txt', 'r') as arquivo1, open('arquivo2.txt', 'r') as arquivo2:
    linhas_arquivo1 = arquivo1.readlines()
    linhas_arquivo2 = arquivo2.readlines()

    diff = difflib.unified_diff(linhas_arquivo1, linhas_arquivo2, lineterm='', fromfile='arquivo1', tofile='arquivo2')
for linha in diff:
    if linha.startswith('+') or linha.startswith('-'):
        print(linha)
