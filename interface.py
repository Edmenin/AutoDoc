import tkinter as tk
from tkinter import messagebox
import re
import os
import sys

from preenchimento import preencher_contrato

def validar_apenas_letras(texto):
    """Valida se o texto contém apenas letras, números, espaços, acentos e alguns caracteres especiais."""
    return re.match(r"^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ0-9\s\-.,'´`~]+$", texto) is not None

def validar_apenas_numeros(texto):
    """Valida se o texto contém apenas números."""
    return re.match(r"^\d+$", texto) is not None

def validar_letras_numeros(texto):
    """Valida se o texto contém letras, números, espaços, acentos e caracteres especiais comuns em endereços."""
    return re.match(r"^[A-Za-z0-9\s.,\-/áàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ'´`~]+$", texto) is not None

def validar_data(texto):
    """Valida se o texto está no formato de data (DD/MM/AAAA)."""
    return re.match(r"^\d{2}/\d{2}/\d{4}$", texto) is not None

def validar_cnpj(texto):
    """Valida se o texto está no formato de CNPJ (XX.XXX.XXX/XXXX-XX)."""
    return re.match(r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$", texto) is not None

def validar_cpf(texto):
    """Valida se o texto está no formato de CPF (XXX.XXX.XXX-XX)."""
    return re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", texto) is not None

def validar_cep(texto):
    """Valida se o texto está no formato de CEP (XXXXX-XXX)."""
    return re.match(r"^\d{5}-\d{3}$", texto) is not None

def validar_telefone(texto):
    """Valida se o texto está no formato de telefone (XX) XXXX-XXXX ou (XX) XXXXX-XXXX."""
    return re.match(r"^\(\d{2}\) \d{4,5}-\d{4}$", texto) is not None

def preencher_contrato_interface():
    dados_empresa = {
        "{{nome-contratante}}": nome_contratante_var.get(),
        "{{rua-e-numero}}": rua_numero_var.get(),
        "{{bairro}}": bairro_var.get(),
        "{{cep}}": cep_var.get(),
        "{{cidade-e-estado}}": cidade_estado_var.get(),
        "{{cnpj}}": cnpj_var.get(),
        "{{inicio-campanha}}": inicio_campanha_var.get(),
        "{{fim-campanha}}": fim_campanha_var.get(),
        "{{data-atual}}": data_atual_var.get(),
        "{{nome}}": nome_responsavel_var.get(),
        "{{cargo}}": cargo_var.get(),
        "{{cpf}}": cpf_var.get(),
        "{{associacao}}": associacao_var.get(),
        "{{nome-promocao}}": nome_promocao_var.get(),  
        "{{telefone-fax}}": telefone_fax_var.get()    
    }

    if not validar_apenas_letras(dados_empresa["{{nome-contratante}}"]):
        messagebox.showerror("Erro", "Nome do contratante deve conter apenas letras, números e caracteres especiais permitidos.")
        return
    if not validar_letras_numeros(dados_empresa["{{rua-e-numero}}"]):
        messagebox.showerror("Erro", "Rua e número devem conter letras, números e caracteres especiais permitidos.")
        return
    if not validar_apenas_letras(dados_empresa["{{bairro}}"]):
        messagebox.showerror("Erro", "Bairro deve conter apenas letras e caracteres especiais permitidos.")
        return
    if not validar_cep(dados_empresa["{{cep}}"]):
        messagebox.showerror("Erro", "CEP deve estar no formato XXXXX-XXX.")
        return
    if not validar_letras_numeros(dados_empresa["{{cidade-e-estado}}"]):
        messagebox.showerror("Erro", "Cidade e estado devem conter apenas letras, números e caracteres especiais permitidos.")
        return
    if not validar_cnpj(dados_empresa["{{cnpj}}"]):
        messagebox.showerror("Erro", "CNPJ deve estar no formato XX.XXX.XXX/XXXX-XX.")
        return
    if not validar_data(dados_empresa["{{inicio-campanha}}"]):
        messagebox.showerror("Erro", "Data de início da campanha deve estar no formato DD/MM/AAAA.")
        return
    if not validar_data(dados_empresa["{{fim-campanha}}"]):
        messagebox.showerror("Erro", "Data de fim da campanha deve estar no formato DD/MM/AAAA.")
        return
    if not validar_data(dados_empresa["{{data-atual}}"]):
        messagebox.showerror("Erro", "Data atual deve estar no formato DD/MM/AAAA.")
        return
    if not validar_apenas_letras(dados_empresa["{{nome}}"]):
        messagebox.showerror("Erro", "Nome do responsável deve conter apenas letras e caracteres especiais permitidos.")
        return
    if not validar_apenas_letras(dados_empresa["{{cargo}}"]):
        messagebox.showerror("Erro", "Cargo deve conter apenas letras e caracteres especiais permitidos.")
        return
    if not validar_cpf(dados_empresa["{{cpf}}"]):
        messagebox.showerror("Erro", "CPF deve estar no formato XXX.XXX.XXX-XX.")
        return
    if not validar_apenas_letras(dados_empresa["{{associacao}}"]):
        messagebox.showerror("Erro", "Associação deve conter apenas letras e caracteres especiais permitidos.")
        return
    if not validar_apenas_letras(dados_empresa["{{nome-promocao}}"]):  
        messagebox.showerror("Erro", "Nome da promoção deve conter apenas letras, números e caracteres especiais permitidos.")
        return
    if not validar_telefone(dados_empresa["{{telefone-fax}}"]):  
        messagebox.showerror("Erro", "Telefone/Fax deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.")
        return

    if preencher_contrato(dados_empresa):
        messagebox.showinfo("Sucesso", "Contratos preenchidos com sucesso!")

root = tk.Tk()
root.title("Preenchimento de Contratos")
root.geometry("500x600")  
root.config(bg="#f7f7f7")

font_label = ("Helvetica", 10)
font_entry = ("Helvetica", 12)
font_button = ("Helvetica", 12, "bold")
bg_color = "#4CAF50"
btn_color = "#fff"
label_color = "#333"
entry_color = "#f1f1f1"

def style_widget(widget, width=30):
    widget.config(font=font_entry, bg=entry_color, width=width, relief="solid", bd=1, highlightthickness=1)

nome_contratante_var = tk.StringVar()
rua_numero_var = tk.StringVar()
bairro_var = tk.StringVar()
cep_var = tk.StringVar()
cidade_estado_var = tk.StringVar()
cnpj_var = tk.StringVar()
inicio_campanha_var = tk.StringVar()
fim_campanha_var = tk.StringVar()
data_atual_var = tk.StringVar()
nome_responsavel_var = tk.StringVar()
cargo_var = tk.StringVar()
cpf_var = tk.StringVar()
associacao_var = tk.StringVar()
nome_promocao_var = tk.StringVar() 
telefone_fax_var = tk.StringVar()

tk.Label(root, text="Nome do Contratante", font=font_label, bg="#f7f7f7", anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")
nome_contratante_entry = tk.Entry(root, textvariable=nome_contratante_var)
nome_contratante_entry.grid(row=0, column=1, padx=10, pady=5)
style_widget(nome_contratante_entry)

tk.Label(root, text="Rua e Número", font=font_label, bg="#f7f7f7", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
rua_numero_entry = tk.Entry(root, textvariable=rua_numero_var)
rua_numero_entry.grid(row=1, column=1, padx=10, pady=5)
style_widget(rua_numero_entry)

tk.Label(root, text="Bairro", font=font_label, bg="#f7f7f7", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
bairro_entry = tk.Entry(root, textvariable=bairro_var)
bairro_entry.grid(row=2, column=1, padx=10, pady=5)
style_widget(bairro_entry)

tk.Label(root, text="CEP", font=font_label, bg="#f7f7f7", anchor="w").grid(row=3, column=0, padx=10, pady=5, sticky="w")
cep_entry = tk.Entry(root, textvariable=cep_var)
cep_entry.grid(row=3, column=1, padx=10, pady=5)
style_widget(cep_entry)

tk.Label(root, text="Cidade e Estado", font=font_label, bg="#f7f7f7", anchor="w").grid(row=4, column=0, padx=10, pady=5, sticky="w")
cidade_estado_entry = tk.Entry(root, textvariable=cidade_estado_var)
cidade_estado_entry.grid(row=4, column=1, padx=10, pady=5)
style_widget(cidade_estado_entry)

tk.Label(root, text="CNPJ", font=font_label, bg="#f7f7f7", anchor="w").grid(row=5, column=0, padx=10, pady=5, sticky="w")
cnpj_entry = tk.Entry(root, textvariable=cnpj_var)
cnpj_entry.grid(row=5, column=1, padx=10, pady=5)
style_widget(cnpj_entry)

tk.Label(root, text="Início da Campanha", font=font_label, bg="#f7f7f7", anchor="w").grid(row=6, column=0, padx=10, pady=5, sticky="w")
inicio_campanha_entry = tk.Entry(root, textvariable=inicio_campanha_var)
inicio_campanha_entry.grid(row=6, column=1, padx=10, pady=5)
style_widget(inicio_campanha_entry)

tk.Label(root, text="Fim da Campanha", font=font_label, bg="#f7f7f7", anchor="w").grid(row=7, column=0, padx=10, pady=5, sticky="w")
fim_campanha_entry = tk.Entry(root, textvariable=fim_campanha_var)
fim_campanha_entry.grid(row=7, column=1, padx=10, pady=5)
style_widget(fim_campanha_entry)

tk.Label(root, text="Data Atual", font=font_label, bg="#f7f7f7", anchor="w").grid(row=8, column=0, padx=10, pady=5, sticky="w")
data_atual_entry = tk.Entry(root, textvariable=data_atual_var)
data_atual_entry.grid(row=8, column=1, padx=10, pady=5)
style_widget(data_atual_entry)

tk.Label(root, text="Nome do Responsável", font=font_label, bg="#f7f7f7", anchor="w").grid(row=9, column=0, padx=10, pady=5, sticky="w")
nome_responsavel_entry = tk.Entry(root, textvariable=nome_responsavel_var)
nome_responsavel_entry.grid(row=9, column=1, padx=10, pady=5)
style_widget(nome_responsavel_entry)

tk.Label(root, text="Cargo", font=font_label, bg="#f7f7f7", anchor="w").grid(row=10, column=0, padx=10, pady=5, sticky="w")
cargo_entry = tk.Entry(root, textvariable=cargo_var)
cargo_entry.grid(row=10, column=1, padx=10, pady=5)
style_widget(cargo_entry)

tk.Label(root, text="CPF", font=font_label, bg="#f7f7f7", anchor="w").grid(row=11, column=0, padx=10, pady=5, sticky="w")
cpf_entry = tk.Entry(root, textvariable=cpf_var)
cpf_entry.grid(row=11, column=1, padx=10, pady=5)
style_widget(cpf_entry)

tk.Label(root, text="Associação", font=font_label, bg="#f7f7f7", anchor="w").grid(row=12, column=0, padx=10, pady=5, sticky="w")
associacao_entry = tk.Entry(root, textvariable=associacao_var)
associacao_entry.grid(row=12, column=1, padx=10, pady=5)
style_widget(associacao_entry)

tk.Label(root, text="Nome da Promoção", font=font_label, bg="#f7f7f7", anchor="w").grid(row=13, column=0, padx=10, pady=5, sticky="w")
nome_promocao_entry = tk.Entry(root, textvariable=nome_promocao_var)
nome_promocao_entry.grid(row=13, column=1, padx=10, pady=5)
style_widget(nome_promocao_entry)

tk.Label(root, text="Telefone/Fax", font=font_label, bg="#f7f7f7", anchor="w").grid(row=14, column=0, padx=10, pady=5, sticky="w")
telefone_fax_entry = tk.Entry(root, textvariable=telefone_fax_var)
telefone_fax_entry.grid(row=14, column=1, padx=10, pady=5)
style_widget(telefone_fax_entry)

tk.Button(root, text="Gerar Contratos", command=preencher_contrato_interface, bg=bg_color, fg=btn_color, font=font_button, relief="flat").grid(row=15, column=0, columnspan=2, pady=20)

root.mainloop()