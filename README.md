# 🗂️ Organizador de Arquivos por Extensão

Este script em Python ajuda a **organizar arquivos bagunçados em uma pasta**, movendo automaticamente imagens, planilhas, PDFs e outros arquivos para pastas separadas com base em sua extensão.

## 🚀 Problema que resolve

Sabe quando sua pasta de **Downloads** (ou qualquer outra) vira uma bagunça com dezenas de arquivos misturados?

Este organizador automatiza a separação dos arquivos em categorias como:

- `Imagens/` (ex: `.jpg`, `.png`, etc)
- `Planilhas/` (ex: `.xlsx`, `.csv`, etc)
- `PDFs/`
- `Outros/` (tudo que não pertence às categorias acima)

Com um clique, sua pasta é limpa e organizada!

---

## 🛠️ Como usar

### Pré-requisitos

- Python 3 instalado

### Passo a passo

1. **Clone este repositório** (ou apenas baixe o script `.py`)
2. Execute o script:

```bash
python organizador.py
```

3. Uma janela irá abrir pedindo para você selecionar a pasta que deseja organizar.
4. Os arquivos da pasta serão automaticamente movidos para subpastas com base em suas extensões.

---

## 🧠 Tecnologias usadas

- `os` – para manipular arquivos e diretórios
- `tkinter.filedialog` – para abrir uma janela gráfica de seleção de pasta

---

## 📂 Estrutura após organização

Se a pasta original tiver arquivos como:

```
foto.jpg
relatorio.pdf
planilha.xlsx
nota.txt
```

Ela será organizada assim:

```
/Imagens/foto.jpg
/PDFs/relatorio.pdf
/Planilhas/planilha.xlsx
/Outros/nota.txt
```

---

## ✅ Resultado

Rápida organização de arquivos com apenas alguns cliques, sem necessidade de mover manualmente cada item.

---

## 📌 Observações

- Apenas arquivos diretamente na pasta selecionada são organizados (não varre subpastas).
- Se o arquivo já estiver dentro de uma pasta com o nome da categoria, ele será ignorado.
- O script é seguro: apenas move arquivos, não deleta nada.

---

## 📬 Contribuições

Sugestões de novas categorias ou melhorias são bem-vindas! Basta abrir uma *issue* ou enviar um *pull request*.

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.
