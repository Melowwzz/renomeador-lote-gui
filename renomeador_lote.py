import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class RenomeadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Renomeador de Arquivos em Lote - Vibe 🖤")
        self.root.geometry("800x600")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.caminho_pasta = ""

        self.criar_widgets()

    def criar_widgets(self):
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        folder_selection_frame = ctk.CTkFrame(main_frame)
        folder_selection_frame.pack(pady=10, fill="x")

        self.label_folder = ctk.CTkLabel(folder_selection_frame, text="Nenhuma pasta selecionada")
        self.label_folder.pack(side="left", padx=10, pady=5)

        btn_select_folder = ctk.CTkButton(folder_selection_frame, text="Selecionar Pasta", command=self.selecionar_pasta)
        btn_select_folder.pack(side="right", padx=10, pady=5)

        options_frame = ctk.CTkFrame(main_frame)
        options_frame.pack(pady=10, fill="x")

        prefix_suffix_frame = ctk.CTkFrame(options_frame)
        prefix_suffix_frame.pack(pady=5, fill="x")

        self.check_prefixo = ctk.CTkCheckBox(prefix_suffix_frame, text="Adicionar Prefixo:", command=self.toggle_prefixo_sufixo)
        self.check_prefixo.pack(side="left", padx=5)
        self.entry_prefixo = ctk.CTkEntry(prefix_suffix_frame, placeholder_text="Digite o prefixo")
        self.entry_prefixo.pack(side="left", expand=True, fill="x", padx=5)

        self.check_sufixo = ctk.CTkCheckBox(prefix_suffix_frame, text="Adicionar Sufixo:", command=self.toggle_prefixo_sufixo)
        self.check_sufixo.pack(side="left", padx=5)
        self.entry_sufixo = ctk.CTkEntry(prefix_suffix_frame, placeholder_text="Digite o sufixo")
        self.entry_sufixo.pack(side="left", expand=True, fill="x", padx=5)

        replace_frame = ctk.CTkFrame(options_frame)
        replace_frame.pack(pady=5, fill="x")

        self.check_substituir = ctk.CTkCheckBox(replace_frame, text="Substituir Texto:")
        self.check_substituir.pack(side="left", padx=5)
        self.entry_procurar = ctk.CTkEntry(replace_frame, placeholder_text="Procurar por")
        self.entry_procurar.pack(side="left", expand=True, fill="x", padx=5)
        self.label_por = ctk.CTkLabel(replace_frame, text="por:")
        self.label_por.pack(side="left", padx=5)
        self.entry_substituir = ctk.CTkEntry(replace_frame, placeholder_text="Substituir por")
        self.entry_substituir.pack(side="left", expand=True, fill="x", padx=5)

        num_frame = ctk.CTkFrame(options_frame)
        num_frame.pack(pady=5, fill="x")
        self.check_numerar = ctk.CTkCheckBox(num_frame, text="Numerar Arquivos")
        self.check_numerar.pack(side="left", padx=5)

        btn_pre_visualizar = ctk.CTkButton(main_frame, text="Pré-Visualizar", command=self.pre_visualizar)
        btn_pre_visualizar.pack(pady=10)

        self.preview_text = ctk.CTkTextbox(main_frame, width=700, height=150, wrap="word")
        self.preview_text.pack(pady=10)
        self.preview_text.insert("end", "Pré-visualização dos nomes dos arquivos aparecerá aqui.")
        self.preview_text.configure(state="disabled")

        rename_progress_frame = ctk.CTkFrame(main_frame)
        rename_progress_frame.pack(pady=10, fill="x")

        self.progress_bar = ctk.CTkProgressBar(rename_progress_frame, orientation="horizontal")
        self.progress_bar.pack(side="left", expand=True, fill="x", padx=10)
        self.progress_bar.set(0)

        btn_renomear = ctk.CTkButton(rename_progress_frame, text="Renomear Arquivos", command=self.renomear_arquivos)
        btn_renomear.pack(side="right", padx=10)

        self.log_text = ctk.CTkTextbox(main_frame, width=700, height=80, wrap="word")
        self.log_text.pack(pady=10)
        self.log_text.insert("end", "Logs de operação aparecerão aqui.")
        self.log_text.configure(state="disabled")

        self.toggle_prefixo_sufixo()

    def toggle_prefixo_sufixo(self):
        if self.check_prefixo.get() == 1:
            self.entry_prefixo.configure(state="normal")
        else:
            self.entry_prefixo.configure(state="disabled")
            self.entry_prefixo.delete(0, "end")

        if self.check_sufixo.get() == 1:
            self.entry_sufixo.configure(state="normal")
        else:
            self.entry_sufixo.configure(state="disabled")
            self.entry_sufixo.delete(0, "end")

    def selecionar_pasta(self):
        self.caminho_pasta = filedialog.askdirectory()
        if self.caminho_pasta:
            self.label_folder.configure(text=f"Pasta Selecionada: {self.caminho_pasta}")
            self.log_message(f"Pasta selecionada: {self.caminho_pasta}")
            self.pre_visualizar()
        else:
            self.log_message("Seleção de pasta cancelada.")

    def pre_visualizar(self):
        if not self.caminho_pasta:
            self.log_message("Por favor, selecione uma pasta primeiro.")
            return

        self.preview_text.configure(state="normal")
        self.preview_text.delete("1.0", "end")

        arquivos = [f for f in os.listdir(self.caminho_pasta) if os.path.isfile(os.path.join(self.caminho_pasta, f))]
        
        if not arquivos:
            self.preview_text.insert("end", "Nenhum arquivo encontrado nesta pasta.")
            self.preview_text.configure(state="disabled")
            return

        for i, arquivo_original in enumerate(sorted(arquivos)):
            nome_base, extensao = os.path.splitext(arquivo_original)
            novo_nome_base = nome_base

            if self.check_substituir.get() == 1:
                procurar_por = self.entry_procurar.get()
                substituir_por = self.entry_substituir.get()
                if procurar_por:
                    novo_nome_base = novo_nome_base.replace(procurar_por, substituir_por)

            if self.check_numerar.get() == 1:
                num_formatado = str(i + 1).zfill(len(str(len(arquivos))))
                novo_nome_base = f"{novo_nome_base}_{num_formatado}"

            if self.check_prefixo.get() == 1:
                prefixo = self.entry_prefixo.get()
                novo_nome_base = f"{prefixo}{novo_nome_base}"
            
            if self.check_sufixo.get() == 1:
                sufixo = self.entry_sufixo.get()
                novo_nome_base = f"{novo_nome_base}{sufixo}"

            novo_nome_completo = f"{novo_nome_base}{extensao}"
            self.preview_text.insert("end", f"De: {arquivo_original}  ->  Para: {novo_nome_completo}\n")

        self.preview_text.configure(state="disabled")

    def renomear_arquivos(self):
        if not self.caminho_pasta:
            messagebox.showwarning("Atenção", "Por favor, selecione uma pasta primeiro.")
            return
        
        resposta = messagebox.askyesno("Confirmar Renomeação", 
                                       "Tem certeza que deseja renomear os arquivos? Esta ação não pode ser desfeita!")
        if not resposta:
            self.log_message("Operação de renomeação cancelada pelo usuário.")
            return

        self.log_message("Iniciando renomeação de arquivos...")
        self.progress_bar.set(0)

        arquivos = [f for f in os.listdir(self.caminho_pasta) if os.path.isfile(os.path.join(self.caminho_pasta, f))]
        total_arquivos = len(arquivos)

        if not arquivos:
            self.log_message("Nenhum arquivo para renomear na pasta selecionada.")
            return

        for i, arquivo_original in enumerate(sorted(arquivos)):
            caminho_antigo = os.path.join(self.caminho_pasta, arquivo_original)
            nome_base, extensao = os.path.splitext(arquivo_original)
            novo_nome_base = nome_base

            try:
                if self.check_substituir.get() == 1:
                    procurar_por = self.entry_procurar.get()
                    substituir_por = self.entry_substituir.get()
                    if procurar_por:
                        novo_nome_base = novo_nome_base.replace(procurar_por, substituir_por)

                if self.check_numerar.get() == 1:
                    num_formatado = str(i + 1).zfill(len(str(total_arquivos)))
                    novo_nome_base = f"{novo_nome_base}_{num_formatado}"

                if self.check_prefixo.get() == 1:
                    prefixo = self.entry_prefixo.get()
                    novo_nome_base = f"{prefixo}{novo_nome_base}"
                
                if self.check_sufixo.get() == 1:
                    sufixo = self.entry_sufixo.get()
                    novo_nome_base = f"{novo_nome_base}{sufixo}"

                novo_nome_completo = f"{novo_nome_base}{extensao}"
                caminho_novo = os.path.join(self.caminho_pasta, novo_nome_completo)

                if os.path.exists(caminho_novo) and caminho_novo != caminho_antigo:
                    self.log_message(f"AVISO: O arquivo '{novo_nome_completo}' já existe. '{arquivo_original}' não foi renomeado.", level="warning")
                else:
                    os.rename(caminho_antigo, caminho_novo)
                    self.log_message(f"Renomeado: '{arquivo_original}' para '{novo_nome_completo}'")
            except Exception as e:
                self.log_message(f"ERRO ao renomear '{arquivo_original}': {e}", level="error")
            
            self.progress_bar.set((i + 1) / total_arquivos)
            self.root.update_idletasks()

        self.log_message("Renomeação de arquivos concluída!")
        self.pre_visualizar()

    def log_message(self, message, level="info"):
        self.log_text.configure(state="normal")
        if level == "error":
            self.log_text.insert("end", f"ERRO: {message}\n", "error")
        elif level == "warning":
            self.log_text.insert("end", f"AVISO: {message}\n", "warning")
        else:
            self.log_text.insert("end", f"{message}\n")
        
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

if __name__ == "__main__":
    root = ctk.CTk()
    app = RenomeadorApp(root)
    root.mainloop()
