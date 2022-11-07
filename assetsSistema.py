from cgitb import text
from distutils.cmd import Command
from os import path
import time
from tkinter import ttk
from tkinter.tix import IMAGETEXT
from turtle import bgcolor, width
from tkinter import *
from tkinter.ttk import Notebook, Style
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
from datetime import datetime
import calendar
import locale
import webbrowser
data_atual = datetime.today()
date = datetime.now()
#locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

#now = time("%H:%M:%S")
# print(now)

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("light")

# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()  # create CTk window like you do with the Tk window

col_Branca = "#FFFFFF"  # BRANCA
col_Preta = "#000000"  # Letra PRETA (exceto letras Botoes)
col_AzulClaro = "#448ccc"  # Letra VERDE
col_AzulEscuro = '#1E90FF'  # Background Button AZUL
col_Vermelho = '#FF6347'  # Background Button VERMELHO
col_Entry = "#C4CED1"
col_Cinza = "#4c4c4c"
col_bgSistema = "#dcdcdc"

logoEmpresa = PhotoImage(file="img/logoficticia2.png")
logoLimpar = PhotoImage(file="img/limpar.png")
logoBuscar = PhotoImage(file="img/buscar.png")
logoNovo = PhotoImage(file="img/novo.png")
logoAlterar = PhotoImage(file="img/alterar.png")
logoExcluir = PhotoImage(file="img/excluir.png")
logoInsta = PhotoImage(file="img/insta.png")
logoAADev = PhotoImage(file="img/aadev.png")

unidEmpresa = [
    "Azul Participações CE", "Azul Participações RN", "Azul Participações SP", "Azul Participações MG"]
setor = [
    "Administração", "Atendimento", "Comercial", "Diretoria", "Financeiro", "Rel. Empresarial", "Tecnologia da informação", "Vendas"
]
tecnico = [
    "Aristoteles Aguiar", "Jessica Katariny",
    "George Michael", "Plinio Dias"]
sistOper = [
    "Windows 7", "Windows 8", "Windows 10", "Windows 11", "macOS", "Linux"]
trueFalse = [
    "Sim", "Não"]


class Apllication():

    def __init__(self):
        self.root = root
        self.systemScreen()
        self.frameLateral()
        self.frameLateralDir()
        self.framePrincipal()
        self.noteBook()
        self.change_appearance_mode
        self.on_closing

        root.mainloop()

    def systemScreen(self):
        self.root.title("")
        self.root.geometry("1366x788")

    def frameLateral(self):
        self.frame_lateral = customtkinter.CTkFrame(
            self.root, width=(190), height=(690))
        self.frame_lateral.place(x=10, y=10)

# Logo EMPRESA ------
        self.frameHeaderLogo = customtkinter.CTkLabel(
            self.frame_lateral, image=logoEmpresa)
        self.frameHeaderLogo.place(relx=0.125, rely=0.02)
# ===============================================================
    # Label (Cadastro de Bens)
        self.label_lateral = customtkinter.CTkLabel(
            self.frame_lateral, text="Cadastro de Bens", text_font=("Ivy Mode Regular", -18))
        self.label_lateral.place(relx=0.1, rely=0.2)
# ===============================================================
    # CheckBox Entrada
        self.label_cxBox_lateral_Entr = customtkinter.CTkLabel(
            self.frame_lateral, text="Entrada")
        self.label_cxBox_lateral_Entr.place(relx=0.17, rely=0.27)

        self.checkBox_entrada = customtkinter.CTkCheckBox(
            self.frame_lateral, text="")
        self.checkBox_entrada.place(relx=0.25, rely=0.27)
    # CheckBox Saida
        self.label_cxBox_lateral_Saida = customtkinter.CTkLabel(
            self.frame_lateral, text="Saida")
        self.label_cxBox_lateral_Saida.place(relx=0.17, rely=0.34)

        self.checkBox_saida = customtkinter.CTkCheckBox(
            self.frame_lateral, text="")
        self.checkBox_saida.place(relx=0.25, rely=0.34)
# ===============================================================
    # Button LIMPAR
        self.btt_Limpar = customtkinter.CTkButton(
            self.frame_lateral, image=logoLimpar, text="Limpar")
        self.btt_Limpar.place(relx=0.1, rely=0.43)
    # botao EDITAR
        self.btt_Edit = customtkinter.CTkButton(
            self.frame_lateral, image=logoAlterar, text=" Editar ")
        self.btt_Edit.place(relx=0.1, rely=0.49)
    # botao BUSCAR
        self.btt_Buscar = customtkinter.CTkButton(
            self.frame_lateral, image=logoBuscar, text="Buscar")
        self.btt_Buscar.place(relx=0.1, rely=0.55)
    # botao EXCLUIR
        self.btt_Excluir = customtkinter.CTkButton(
            self.frame_lateral, image=logoExcluir, text="Excluir")
        self.btt_Excluir.place(relx=0.1, rely=0.61)
    # botao NOVO
        self.btt_Salvar = customtkinter.CTkButton(
            self.frame_lateral, image=logoNovo, text="Salvar")
        self.btt_Salvar.place(relx=0.1, rely=0.67)

# ===============================================================
    # Aparencia do MENU (DARK, LIGHT)

        self.label_mode = customtkinter.CTkLabel(
            self.frame_lateral, text="Tema")
        self.label_mode.place(relx=0.1, rely=0.9)

        self.optionmenu_1 = customtkinter.CTkComboBox(self.frame_lateral, values=("Light", "Dark"),
                                                      command=self.change_appearance_mode)
        self.optionmenu_1.place(relx=0.31, rely=0.94,
                                relwidth=0.37, relheight=0.04)

    def frameLateralDir(self):

        self.frame_lateralDir = customtkinter.CTkFrame(
            self.root, width=(190), height=(690))
        self.frame_lateralDir.place(x=1165, y=10)

        self.frame_Hora = customtkinter.CTkFrame(
            self.frame_lateralDir, height=30, width=150)
        self.frame_Hora.place(relx=0.11, rely=0.04)

        self.label_Hora = customtkinter.CTkLabel(
            self.frame_Hora, text=date.strftime("%d/%m/%Y"))
        self.label_Hora.place(relx=0.25, rely=0.01,
                              relwidth=0.5, relheight=0.9)

    # instagram

        self.label_LogoInsta = customtkinter.CTkLabel(
            self.frame_lateralDir, image=logoInsta, text="")
        self.label_LogoInsta.place(
            relx=0.4, rely=0.85, relwidth=0.2, relheight=0.05)

        self.label_InstaText = customtkinter.CTkButton(
            self.frame_lateralDir, text="", fg_color=col_Branca, image=logoAADev, 
            corner_radius=8, hover_color=col_Branca, command=lambda: webbrowser.open('https://www.instagram.com/aa_dev_py/'))
        self.label_InstaText.place(
            relx=0.07, rely=0.91, relwidth=0.85, relheight=0.08)
# ===============================================================
    def framePrincipal(self):

        self.frame_Principal = customtkinter.CTkFrame(
            self.root, height=(350), width=(940))
        self.frame_Principal.place(relx=0.155, rely=0.05)

        self.frame_Principal_menor = customtkinter.CTkFrame(
            self.frame_Principal, height=320, width=200)
        self.frame_Principal_menor.place(relx=0.77, rely=0.05)

    # 1 campo CODIGO
        self.label_princ_cod = customtkinter.CTkLabel(
            self.frame_Principal, text="Código")
        self.label_princ_cod.place(
            relx=0.02, rely=0.02, relwidth=0.05, relheight=0.05)

        self.cod_princ_entry = customtkinter.CTkEntry(self.frame_Principal)
        self.cod_princ_entry.place(
            relx=0.02, rely=0.07, relwidth=0.05, relheight=0.07)

    # 2 campo TOMBO
        self.label_princ_tombo = customtkinter.CTkLabel(
            self.frame_Principal, text="Tombo/Serie")
        self.label_princ_tombo.place(
            relx=0.095, rely=0.02, relwidth=0.09, relheight=0.05)

        self.tombo_princ_entry = customtkinter.CTkEntry(self.frame_Principal)
        self.tombo_princ_entry.place(
            relx=0.095, rely=0.07, relwidth=0.09, relheight=0.07)

    # 3 campo HOSTNAME
        self.label_princ_hostname = customtkinter.CTkLabel(
            self.frame_Principal, text="Hostname")
        self.label_princ_hostname.place(
            relx=0.21, rely=0.02, relwidth=0.09, relheight=0.05)

        self.hostname_princ_entry = customtkinter.CTkEntry(
            self.frame_Principal)
        self.hostname_princ_entry.place(
            relx=0.21, rely=0.07, relwidth=0.09, relheight=0.07)

    # 4 campo INGRESSO DOMINIO /// ComboBox ///
        self.label_princ_ingDominio = customtkinter.CTkLabel(
            self.frame_Principal_menor, text="Ingr Dominio")
        self.label_princ_ingDominio.place(
            relx=0.06, rely=0.03, relwidth=0.4, relheight=0.05)

        self.ingDominio_princ_entry = customtkinter.CTkComboBox(
            self.frame_Principal_menor, values=trueFalse)
        self.ingDominio_princ_entry.place(
            relx=0.06, rely=0.09, relwidth=0.42, relheight=0.08)

    # 5 campo SISTEMA OPERACIONAL /// ComboBox ///
        self.label_princ_sistOperac = customtkinter.CTkLabel(
            self.frame_Principal_menor, text="Sist. Operacional")
        self.label_princ_sistOperac.place(
            relx=0.06, rely=0.17, relwidth=0.5, relheight=0.05)

        self.sistOperac_princ_entry = customtkinter.CTkComboBox(
            self.frame_Principal_menor, values=sistOper)
        self.sistOperac_princ_entry.place(
            relx=0.06, rely=0.22, relwidth=0.87, relheight=0.08)

    # 6 campo INSTALACAO S.O /// ComboBox ///
        self.label_princ_instSO = customtkinter.CTkLabel(
            self.frame_Principal_menor, text="Instalado S.O")
        self.label_princ_instSO.place(
            relx=0.06, rely=0.3, relwidth=0.4, relheight=0.05)

        self.instSO_princ_entry = customtkinter.CTkComboBox(
            self.frame_Principal_menor, values=trueFalse)
        self.instSO_princ_entry.place(
            relx=0.06, rely=0.35, relwidth=0.4, relheight=0.08)

    # 7 campo ATUALIZADO S.O /// ComboBox ///
        self.label_princ_atualSO = customtkinter.CTkLabel(
            self.frame_Principal_menor, text="Atualizado S.O")
        self.label_princ_atualSO.place(
            relx=0.06, rely=0.43, relwidth=0.4, relheight=0.05)

        self.atualSO_princ_entry = customtkinter.CTkComboBox(
            self.frame_Principal_menor, values=trueFalse)
        self.atualSO_princ_entry.place(
            relx=0.06, rely=0.48, relwidth=0.4, relheight=0.08)

    # 8 campo SETOR DO USUARIO /// ComboBox ///
        self.label_princ_setor = customtkinter.CTkLabel(
            self.frame_Principal_menor, text="Setor Usuário")
        self.label_princ_setor.place(
            relx=0.06, rely=0.56, relwidth=0.4, relheight=0.05)

        self.setor_princ_entry = customtkinter.CTkComboBox(
            self.frame_Principal_menor, values=setor)
        self.setor_princ_entry.place(
            relx=0.06, rely=0.61, relwidth=0.87, relheight=0.08)

    # 9 campo TECNICO RESPONSAVEL /// ComboBox ///
        self.label_princ_tecnico = customtkinter.CTkLabel(
            self.frame_Principal_menor, text="Tecnico Resp")
        self.label_princ_tecnico.place(
            relx=0.06, rely=0.69, relwidth=0.4, relheight=0.05)

        self.tecnico_princ_entry = customtkinter.CTkComboBox(
            self.frame_Principal_menor, values=tecnico)
        self.tecnico_princ_entry.place(
            relx=0.06, rely=0.74, relwidth=0.87, relheight=0.08)

    # 10 campo EMPRESA DESTINO /// ComboBox ///
        self.label_princ_emprDestino = customtkinter.CTkLabel(

            self.frame_Principal_menor, text="Empresa Destino")
        self.label_princ_emprDestino.place(
            relx=0.06, rely=0.82, relwidth=0.5, relheight=0.05)

        self.emprDestino_princ_entry = customtkinter.CTkComboBox(
            self.frame_Principal_menor, values=unidEmpresa)
        self.emprDestino_princ_entry.place(
            relx=0.06, rely=0.87, relwidth=0.87, relheight=0.08)

    # 11 campo DESCRICAO / EQUIPAMENTOS / MODELO
        self.label_princ_descricao = customtkinter.CTkLabel(
            self.frame_Principal, text="Descrição (Equipamento / Modelo)")
        self.label_princ_descricao.place(
            relx=0.026, rely=0.15, relwidth=0.21, relheight=0.05)

        self.descricao_princ_entry = customtkinter.CTkEntry(
            self.frame_Principal)
        self.descricao_princ_entry.place(
            relx=0.02, rely=0.2, relwidth=0.53, relheight=0.07)

    # 12 campo ACESSORIOS
        self.label_princ_acessorios = customtkinter.CTkLabel(
            self.frame_Principal, text="Acessorios")
        self.label_princ_acessorios.place(
            relx=0.02, rely=0.28, relwidth=0.08, relheight=0.04)

        self.acessorios_princ_entry = customtkinter.CTkEntry(
            self.frame_Principal)
        self.acessorios_princ_entry.place(
            relx=0.02, rely=0.33, relwidth=0.53, relheight=0.07)

    # 12,5 campo FORNECEDOR
        self.label_princ_fornecedor = customtkinter.CTkLabel(
            self.frame_Principal, text="Fornecedor")
        self.label_princ_fornecedor.place(
            relx=0.02, rely=0.405, relwidth=0.08, relheight=0.04)

        self.fornecedor_princ_entry = customtkinter.CTkEntry(
            self.frame_Principal)
        self.fornecedor_princ_entry.place(
            relx=0.02, rely=0.45, relwidth=0.53, relheight=0.07)

    # 14 campo USUARIO SETOR
        self.label_princ_userSetor = customtkinter.CTkLabel(
            self.frame_Principal, text="Usuario SETOR")
        self.label_princ_userSetor.place(
            relx=0.02, rely=0.52, relwidth=0.1, relheight=0.07)

        self.userSetor_princ_entry = customtkinter.CTkEntry(
            self.frame_Principal)
        self.userSetor_princ_entry.place(
            relx=0.02, rely=0.58, relwidth=0.25, relheight=0.07)

    # 15 campo USUARIO ADMIN
        self.label_princ_userAdmin = customtkinter.CTkLabel(
            self.frame_Principal, text="Usuario ADMIN")
        self.label_princ_userAdmin.place(
            relx=0.3, rely=0.52, relwidth=0.1, relheight=0.07)

        self.userAdmin_princ_entry = customtkinter.CTkEntry(
            self.frame_Principal)
        self.userAdmin_princ_entry.place(
            relx=0.3, rely=0.58, relwidth=0.25, relheight=0.07)

    # 16 campo SENHA ADMIN
        self.label_princ_passAdmin = customtkinter.CTkLabel(
            self.frame_Principal, text="Senha ADMIN")
        self.label_princ_passAdmin.place(
            relx=0.02, rely=0.65, relwidth=0.09, relheight=0.06)

        self.passAdmin_princ_entry = customtkinter.CTkEntry(
            self.frame_Principal)
        self.passAdmin_princ_entry.place(
            relx=0.02, rely=0.71, relwidth=0.15, relheight=0.07)

    # 17 campo EXPIRA SENHA
        self.label_princ_expPassAdmin = customtkinter.CTkLabel(
            self.frame_Principal, text="Expira SENHA")
        self.label_princ_expPassAdmin.place(
            relx=0.3, rely=0.65, relwidth=0.09, relheight=0.07)

        self.expPassAdmin_princ_entry = customtkinter.CTkEntry(
            self.frame_Principal)
        self.expPassAdmin_princ_entry.place(
            relx=0.3, rely=0.71, relwidth=0.15, relheight=0.07)

    # 18 campo DATA
        self.label_princ_data = customtkinter.CTkLabel(
            self.frame_Principal, text="Data")
        self.label_princ_data.place(
            relx=0.02, rely=0.79, relwidth=0.04, relheight=0.05)

        self.data_princ_entry = customtkinter.CTkComboBox(
            self.frame_Principal, values="05/11/2022")
        self.data_princ_entry.place(
            relx=0.02, rely=0.85, relwidth=0.15, relheight=0.08)
        self.data_princ_entry.set("    /    /     ")

    def noteBook(self):

        self.frame_ntBk = customtkinter.CTkFrame(
            self.root, height=270, width=940, bg=col_bgSistema)
        self.frame_ntBk.place(relx=0.155, rely=0.57)

        self.notebook = ttk.Notebook(self.frame_ntBk)
        self.notebook.place(relx=0.01, rely=0.03,
                            relwidth=0.98, relheight=0.94)

        # frames
        self.frame1 = ttk.Frame(self.notebook, width=10, height=10)
        self.frame2 = ttk.Frame(self.notebook, width=10, height=10)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)

        # add frames to notebook
        self.notebook.add(self.frame1, text='    Entrada de Ativo    ')
        self.notebook.add(self.frame2, text='    Saída de Ativo    ')

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


Apllication()
