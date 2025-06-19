# 🚀 Renomeador de Arquivos em Lote - Vibe 🖤

Um aplicativo Python moderno com interface gráfica (GUI) para renomear múltiplos arquivos de uma vez, desenvolvido para otimizar sua organização digital. Perfeito para fotos, documentos e qualquer conjunto de arquivos que precise de um toque de organização!

---

## ✨ Funcionalidades

* **Seleção de Pasta Intuitiva:** Escolha facilmente a pasta com os arquivos a serem renomeados.
* **Adicionar Prefixo/Sufixo:** Inclua textos no início ou no fim dos nomes dos arquivos.
* **Substituir Texto:** Troque partes específicas dos nomes dos arquivos por outras.
* **Numeração Automática:** Organize seus arquivos com uma sequência numérica personalizada.
* **Pré-Visualização:** Veja como os nomes dos arquivos ficarão antes de aplicar as mudanças.
* **Interface Limpa e Moderna:** Desenvolvido com `CustomTkinter` para uma experiência de usuário agradável.
* **Portátil:** Disponível como um executável para Windows, sem necessidade de instalação de Python ou bibliotecas.

---

## 📦 Como Usar (Para Usuários Finais - Plug & Play!)

Se você só quer usar o aplicativo e não se preocupar com código ou instalações:

1.  **Baixe o executável:**
    * Vá para a pasta `renomeador_lote.EXE` neste repositório (a mesma pasta onde você encontrou o `.exe`).
    * Faça o download do arquivo `renomeador_lote.exe`.
2.  **Execute o aplicativo:**
    * Dê um clique duplo no `renomeador_lote.exe`.
    * **Permissões:** Geralmente, não são necessárias permissões de administrador para renomear arquivos em suas pastas pessoais (Downloads, Documentos, etc.). Se encontrar problemas em pastas protegidas do sistema, tente executá-lo como administrador.
3.  **Comece a Renomear!** Siga as instruções na interface para selecionar sua pasta e aplicar as regras de renomeação.

---

## 🛠️ Como Desenvolver/Rodar o Código Fonte (Para Desenvolvedores)

Se você é um desenvolvedor e quer explorar o código-fonte, contribuir ou rodar o aplicativo diretamente via Python:

### Pré-requisitos

Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) instalado em seu sistema. Recomenda-se a versão mais recente e estável.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SeuUsuario/renomeador-lote.git](https://github.com/SeuUsuario/renomeador-lote.git) # Substitua 'SeuUsuario' e 'renomeador-lote' pelos seus dados reais do GitHub
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd renomeador-lote
    ```
3.  **Instale as dependências:**
    Este projeto utiliza o `customtkinter` para a interface gráfica, entre outras dependências listadas no `requirements.txt`. Instale as bibliotecas necessárias usando o `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
    * **Links para download das bibliotecas (se preferir baixar individualmente ou explorar):**
        * **CustomTkinter:** [https://github.com/TomSchimansky/CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
        * **Darkdetect:** [https://github.com/metaclassing/darkdetect](https://github.com/metaclassing/darkdetect) (Dependência do CustomTkinter)
        * **Packaging:** [https://github.com/pypa/packaging](https://github.com/pypa/packaging) (Dependência comum do Python, pode já vir instalada)
        * *(Outras bibliotecas como `pyinstaller`, `altgraph`, etc., presentes no `requirements.txt`, são usadas principalmente para a criação do executável e são gerenciadas automaticamente pelo `pip`.)* 

### Executando o Código Fonte

Após instalar as dependências, você pode rodar o aplicativo:

```bash
python renomeador_lote.py
