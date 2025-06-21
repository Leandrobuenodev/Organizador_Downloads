import os
from tkinter.filedialog import askdirectory

# Seleciona a pasta onde está bagunçado
caminho = askdirectory(title="Selecione a pasta que deseja organizar")
lista_arquivos = os.listdir(caminho)

# Dicionário com categorias e extensões conhecidas
locais = {
    "Imagens": [".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff", ".svg", ".ico", ".heic"],
    "Planilhas": [".xls", ".xlsx", ".ods", ".csv", ".tsv"],
    "PDFs": [".pdf"]
}

# Loop pelos arquivos
for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()

    # Caminho completo do arquivo
    origem = os.path.join(caminho, arquivo)

    # Ignora se for uma pasta
    if os.path.isdir(origem):
        continue

    movido = False

    # Verifica se a extensão está em alguma categoria
    for categoria, extensoes in locais.items():
        if extensao in extensoes:
            destino_pasta = os.path.join(caminho, categoria)
            if not os.path.exists(destino_pasta):
                os.mkdir(destino_pasta)
            destino = os.path.join(destino_pasta, arquivo)
            os.rename(origem, destino)
            print(f"Movido: {arquivo} -> {categoria}/")
            movido = True
            break

    # Se não foi movido pra nenhuma categoria, vai pra "Outros"
    if not movido:
        pasta_outros = os.path.join(caminho, "Outros")
        if not os.path.exists(pasta_outros):
            os.mkdir(pasta_outros)
        destino = os.path.join(pasta_outros, arquivo)
        os.rename(origem, destino)
        print(f"Movido: {arquivo} -> Outros/")

print("\n✅ Organização finalizada com sucesso!")
