from calendar import Calendar
import calendar
from email.policy import default
from multiprocessing import set_forkserver_preload
from queue import Full
from sqlite3 import Date
from sys import maxsize
from time import daylight
from tkinter import *
from tkinter import ttk
from tkinter.tix import NoteBook
from datetime import datetime

root = Tk()

logoEmpresa = PhotoImage(file="img/logoficticia.png")
logoLimpar = PhotoImage(file="img/limpar.png")
logoBuscar = PhotoImage(file="img/buscar.png")
logoNovo = PhotoImage(file="img/novo.png")
logoAlterar = PhotoImage(file="img/alterar.png")
logoExcluir = PhotoImage(file="img/excluir.png")

# -----------Cores do sistema--------------
col_Branca = "#FFFFFF"  # BRANCA
col_Preta = "#000000"  # Letra PRETA (exceto letras Botoes)
col_AzulClaro = "#448ccc"  # Letra VERDE
col_AzulEscuro = '#1E90FF'  # Background Button AZUL
col_Vermelho = '#FF6347'  # Background Button VERMELHO
col_Entry = "#C4CED1"

# -----------Variaveis ComboBox--------------

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
trueFalse = ["Sim", "Não"]

class Apllication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frameHeaderFlooter()
        self.frameSistema()
        self.notebook()
        self.frame1Nb()
        self.colunaNb1()
        self.frame2Nb()
        self.colunaNb2()

        root.mainloop()

# TELA
    def tela(self):
        self.root.title("")
        self.root.configure(background=col_Branca)
        self.root.geometry("1366x768")
        self.root.resizable(True, True)
        self.root.maxsize(width=1366, height=768)
        self.root.minsize(width=500, height=400)

# ---------------N-O-T-E-B-O-O-K-----A-B-A---01--------------

#FRAME_HEADER (Cabeçalho)
    def frameHeaderFlooter(self):
        #     Criando o Frame para o Titulo do Header, Flooter e Logo da Empresa ( Cabeçalho, Rodapé e Logo )
        # -----Cabeçalho-----
        self.frameHeader = Frame(
            self.root, bg=col_Branca, bd=1, width=800, height=90)
        self.frameHeader.place(x=0, y=0)
        self.frameHeaderTexto = Label(self.frameHeader, text="Cadastro de Ativos e Bens",
                                      bd=4, bg=col_Branca, fg=col_AzulClaro, font=('Ivy Mode Regular', 25))
        self.frameHeaderTexto.place(relx=0.18, rely=0.26, width=400, height=50)

        # -----Rodapé-----
        self.frameFlooter = Frame(self.root)
        self.frameFlooter.place(relx=0.02, rely=0.925,
                                relwidth=0.96, relheight=0.6)
        self.frameFlooter = Label(self.frameFlooter, text="Desenvolvido por: Aristoteles Aguiar",
                                  bd=4, bg=col_Branca, fg=col_AzulClaro, font=('Ivy Mode Regular', 8))
        self.frameFlooter.place(relx=0.85, rely=0.06)

        # -----Logo Empresa-----
        self.frameHeaderLogo = Label(self.frameHeader, image=logoEmpresa)
        self.frameHeaderLogo.place(relx=0.03, rely=0.02)

# FRAME SISTEMA
    def frameSistema(self):
        # Frame do sistema-----
        self.frameSistema1 = Frame(
            self.root, bd=4, bg=col_Branca)
        self.frameSistema1.place(
            relx=0.02, rely=0.125, relwidth=0.96, relheight=0.49)


# RADIOBUTTON
        self.radioBt = ttk.Radiobutton(
            self.frameSistema1, text="Entrada  |", value="E",)
        self.radioBt.place(relx=0.033, rely=0.02)

        self.radioBt = ttk.Radiobutton(
            self.frameSistema1, text="Saida", value="S")
        self.radioBt.place(relx=0.093, rely=0.02)

# COMBOBOX
        self.CbBoxUnEmp = Label(self.frameSistema1, text="Empresa:", bg=col_Branca, font=(
            'Ivy Mode Regular', 9))
        self.CbBoxUnEmp.place(relx=0.18, rely=0.02)
        self.CbBoxUnEmp = ttk.Combobox(self.frameSistema1, values=unidEmpresa)
        self.CbBoxUnEmp.place(relx=0.18, rely=0.115, relwidth=0.11)
        self.CbBoxUnEmp.set("Azul Participações")

#   BUTTON - FRAME 1

    # Button LIMPAR
        self.bt_limpar_frame1 = Button(self.frameSistema1, image=logoLimpar)
        self.bt_limpar_frame1.place(
            relx=0.008, rely=0.1, relwidth=0.03, relheight=0.08)
    # Button BUSCAR
        self.bt_buscar_frame1 = Button(self.frameSistema1, image=logoBuscar)
        self.bt_buscar_frame1.place(
            relx=0.038, rely=0.1, relwidth=0.03, relheight=0.08)
    # Button NOVO
        self.bt_novo_frame1 = Button(self.frameSistema1, image=logoNovo)
        self.bt_novo_frame1.place(
            relx=0.068, rely=0.1, relwidth=0.03, relheight=0.08)
    # Button ALTERAR
        self.bt_alterar_frame1 = Button(self.frameSistema1, image=logoAlterar)
        self.bt_alterar_frame1.place(
            relx=0.098, rely=0.1, relwidth=0.03, relheight=0.08)
    # Button EXCLUIR
        self.bt_excluir_frame1 = Button(self.frameSistema1, image=logoExcluir)
        self.bt_excluir_frame1.place(
            relx=0.128, rely=0.1, relwidth=0.03, relheight=0.08)

# NOTEBOOK
    def notebook(self):

        self.notebook = ttk.Notebook(root)
        self.notebook.place(relx=0.02, rely=0.23,
                            relwidth=0.96, relheight=0.74)

    # frames
        self.frame1 = ttk.Frame(self.notebook, width=500, height=10)
        self.frame2 = ttk.Frame(self.notebook, width=500, height=10)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)

    # add frames to notebook
        self.notebook.add(self.frame1, text='    Entrada de Ativo    ')
        self.notebook.add(self.frame2, text='    Saída de Ativo    ')

# FRAME 1 NOTEBOOK
    def frame1Nb(self):
        # codigo_frame1 NOTEBOOK
        self.codigo = Label(self.frame1, text="Codigo",
                            fg=col_Preta, font=('Ivy Mode Regular', 9))
        self.codigo.place(relx=0.01, rely=0.01)

        self.codigo_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.codigo_entry.place(relx=0.01, rely=0.05,
                                relwidth=0.04, relheight=0.045)
    # serie/tombo_frame1 NOTEBOOK
        self.tmbSerie = Label(self.frame1, text="Tombo/Nº Serie",
                              fg=col_Preta, font=('Ivy Mode Regular', 9))
        self.tmbSerie.place(relx=0.06, rely=0.01)

        self.tmbSerie_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.tmbSerie_entry.place(
            relx=0.06, rely=0.05, relwidth=0.08, relheight=0.045)

    # hostname_frame1 NOTEBOOK

        self.hostName = Label(self.frame1, text="Hostname",
                              fg=col_Preta, font=('Ivy Mode Regular', 9))
        self.hostName.place(relx=0.15, rely=0.01)

        self.hostName_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.hostName_entry.place(
            relx=0.15, rely=0.05, relwidth=0.08, relheight=0.045)

        # COMBOBOX Notebook Frame 1 ( Tecnico, Setor, Sistema Operacional )

    # sistema operacioanal

        self.sistOper = Label(self.frame1, text=" Sistema Operacional", font=(
            'Ivy Mode Regular', 9))
        self.sistOper.place(relx=0.315, rely=0.003)
        self.sistOper = ttk.Combobox(self.frame1, values=sistOper)
        self.sistOper.place(relx=0.32, rely=0.05, relwidth=0.099)
        self.sistOper.set("Informe S.O")

    # setor do usuario

        self.setorUser = Label(self.frame1, text="Setor do usuário", font=(
            'Ivy Mode Regular', 9))
        self.setorUser.place(relx=0.418, rely=0.003)
        self.setorUser = ttk.Combobox(self.frame1, values=setor)
        self.setorUser.place(relx=0.42, rely=0.05, relwidth=0.099)
        self.setorUser.set("Informe o setor")

    # tecnico responsavel

        self.tecnico = Label(self.frame1, text="Tecnico Responsavel", font=(
            'Ivy Mode Regular', 9))
        self.tecnico.place(relx=0.518, rely=0.003)
        self.tecnico = ttk.Combobox(self.frame1, values=tecnico)
        self.tecnico.place(relx=0.52, rely=0.05, relwidth=0.099)
        self.tecnico.set("Informe o Tecnico")

    # descrição_frame1 NOTEBOOK
        self.descricao = Label(self.frame1, text="Descrição (Equipamento-Modelo)",
                               fg=col_Preta, font=('Ivy Mode Regular', 9))
        self.descricao.place(relx=0.01, rely=0.1)

        self.descricao_entry = Entry(self.frame1, bg=col_Branca, border=3)

        self.descricao_entry.place(
            relx=0.01, rely=0.15, relwidth=0.3, relheight=0.045)

    # acessorios_frame1 NOTEBOOK
        self.acessorio = Label(self.frame1, text="Acessórios",
                               fg=col_Preta, font=('Ivy Mode Regular', 9))
        self.acessorio.place(relx=0.32, rely=0.1)

        self.acessorio_entry = Entry(self.frame1, bg=col_Branca, border=3)

        self.acessorio_entry.place(
            relx=0.32, rely=0.15, relwidth=0.3, relheight=0.045)

    # fornecedor/origem_frame1 NOTEBOOK
        self.fornecedor = Label(self.frame1, text="Fornecedor", fg=col_Preta, font=(
            'Ivy Mode Regular', 9))
        self.fornecedor.place(relx=0.01, rely=0.2)

        self.fornecedor_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.fornecedor_entry.place(
            relx=0.01, rely=0.25, relwidth=0.3, relheight=0.045)
    # usuario

        self.userSetor = Label(self.frame1, text="Usuário do Setor", fg=col_Preta, font=(
            'Ivy Mode Regular', 9))
        self.userSetor.place(relx=0.32, rely=0.2)

        self.userSetor_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.userSetor_entry.place(
            relx=0.32, rely=0.25, relwidth=0.15, relheight=0.045)

# TREEVIEW
    def colunaNb1(self):
        # FRAME PARA COLUMAS
        self.frameNb1 = Frame(self.frame1, bd=4, bg=col_Entry,
                              highlightbackground=col_Preta, highlightthickness=0)
        self.frameNb1.place(relx=0.01, rely=0.32,
                            relwidth=0.98, relheight=0.65)

    # colunas

        self.colunaNb1 = ttk.Treeview(self.frameNb1, height=4, column=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.colunaNb1.heading("#0", text="")
        self.colunaNb1.heading("#1", text="Tombo/Serie")
        self.colunaNb1.heading("#2", text="Hostname")
        self.colunaNb1.heading("#3", text="S.O")
        self.colunaNb1.heading("#4", text="Setor")
        self.colunaNb1.heading("#5", text="Tecnico")
        self.colunaNb1.heading("#6", text="Descrição")
        self.colunaNb1.heading("#7", text="Acessorios")
        self.colunaNb1.heading("#8", text="Fornecedor")
        self.colunaNb1.heading("#9", text="Usuario")

        self.colunaNb1.column("#0", width=1)
        self.colunaNb1.column("#1", width=8)
        self.colunaNb1.column("#2", width=12)
        self.colunaNb1.column("#3", width=15)
        self.colunaNb1.column("#4", width=20)
        self.colunaNb1.column("#5", width=25)
        self.colunaNb1.column("#6", width=30)
        self.colunaNb1.column("#7", width=30)
        self.colunaNb1.column("#8", width=30)
        self.colunaNb1.column("#9", width=15)

        self.colunaNb1.place(relx=0.005, rely=0.02,
                             relwidth=0.975, relheight=0.95)

    # scrollbar colunaNb1
        self.colunaNb1Scroll = Scrollbar(self.frameNb1, orient='vertical')
        self.colunaNb1.configure(yscroll=self.colunaNb1Scroll.set)
        self.colunaNb1Scroll.place(
            relx=0.982, rely=0.024, relwidth=0.0195, relheight=0.944)

# ---------------N-O-T-E-B-O-O-K-----A-B-A---02--------------

# FRAME 2 NOTEBOOK
    def frame2Nb(self):

#------------C O M B O - B O X-------------------
#Ingresso DOMINIO

        self.label_cbx_Dominio = Label(self.frame2, text="Ingr. Dominio", font=(
            'Ivy Mode Regular', 9))
        self.label_cbx_Dominio.place(relx=0.01, rely=0.02)
        self.cbx_Dominio = ttk.Combobox(self.frame2, value=trueFalse)
        self.cbx_Dominio.place(relx=0.01, rely=0.06, relwidth=0.08)
        
#Instalação SISTEMA OPERACIONAL

        self.label_cbBox_Inst_SO = Label(self.frame2, text="Instalado S.O")
        self.label_cbBox_Inst_SO.place(relx=0.091, rely=0.02)
        self.cbx_Inst_SO = ttk.Combobox(self.frame2, value=trueFalse)
        self.cbx_Inst_SO.place(relx=0.091, rely=0.06, relwidth=0.08)

#Sistema OPERACIONAL

        self.label_sist_Oper2 = Label(self.frame2, text="Sist. Operacional", font=(
            'Ivy Mode Regular', 9))
        self.label_sist_Oper2.place(relx=0.172, rely=0.02)
        self.sist_Oper2 = ttk.Combobox(self.frame2, values=sistOper)
        self.sist_Oper2.place(relx=0.172, rely=0.06, relwidth=0.08)
             
#Atualização SISTEMA OPERACIONAL
    
        self.label_atual_SO = Label(self.frame2, text="Atualizado S.O", font=(
            'Ivy Mode Regular', 9))
        self.label_atual_SO.place(relx=0.253, rely=0.02)
        self.cbx_Atual_SO = ttk.Combobox(self.frame2, values=trueFalse)
        self.cbx_Atual_SO.place(relx=0.253, rely=0.06, relwidth=0.08)
                
#Setor USUARIO FINAL

        self.label_setorUser = Label(self.frame2, text="Setor do usuário", font=(
            'Ivy Mode Regular', 9))
        self.label_setorUser.place(relx=0.334, rely=0.02)
        self.setorUser = ttk.Combobox(self.frame2, values=setor)
        self.setorUser.place(relx=0.334, rely=0.06, relwidth=0.099)
              
#Unidade DESTINO

        self.label_unid_Destino = Label(self.frame2, text="Empresa Destino", font=(
            'Ivy Mode Regular', 9))
        self.label_unid_Destino.place(relx=0.4335, rely=0.02)
        self.unid_Destino = ttk.Combobox(self.frame2, values=unidEmpresa)
        self.unid_Destino.place(relx=0.4335, rely=0.06, relwidth=0.11)
       
       
#------------E N T R Y-------------------
#HostName EQUIPAMENTO

        self.label_hostName = Label(self.frame2, text="Hostname",
                              fg=col_Preta, font=('Ivy Mode Regular', 9))
        self.label_hostName.place(relx=0.01, rely=0.12)

        self.hostName_entry = Entry(self.frame2, bg=col_Branca, border=3)
        self.hostName_entry.place(relx=0.01, rely=0.16, relwidth=0.08, relheight=0.045)    
         
#Usuario ADMIN LOCAL

        self.usu_Admin = Label(self.frame2, text="Usuario Admin",
                              fg=col_Preta, font=('Ivy Mode Regular', 9))
        self.usu_Admin.place(relx=0.091, rely=0.12)

        self.usu_Admin_entry = Entry(self.frame2, bg=col_Branca, border=3)
        self.usu_Admin_entry.place(
            relx=0.091, rely=0.16, relwidth=0.08, relheight=0.045)

#Senha ADMIN LOCAL

        self.pass_Admin = Label(self.frame2, text="Senha Admin",
                              fg=col_Preta, font=('Ivy Mode Regular', 9))
        self.pass_Admin.place(relx=0.172, rely=0.12)

        self.pass_Admin_entry = Entry(self.frame2, bg=col_Branca, border=3)
        self.pass_Admin_entry.place(
            relx=0.172, rely=0.16, relwidth=0.08, relheight=0.045)

#Expiração de ADMIN SENHA

        self.pass_Admin_Exp = Label(self.frame2, text="Expira Senha",
                              fg=col_Preta, font=('Ivy Mode Regular', 9))
        self.pass_Admin_Exp.place(relx=0.253, rely=0.12)

        self.pass_Admin_Exp_entry = Entry(self.frame2, bg=col_Branca, border=3)
        self.pass_Admin_Exp_entry.place(
            relx=0.253, rely=0.16, relwidth=0.08, relheight=0.045)
  
#Usuario FINAL

        self.label_setorUser = Label(self.frame2, text="Usuário", font=(
            'Ivy Mode Regular', 9))
        self.label_setorUser.place(relx=0.334, rely=0.12)
        self.setorUser_entry = Entry(self.frame2, bg=col_Branca, border=3)
        self.setorUser_entry.place(
            relx=0.334, rely=0.16, relwidth=0.099, relheight=0.045)
        
        
  # informação de DATA
        self.label_dataSaida = Label(self.frame2, text="Data da Saida", font=(
            'Ivy Mode Regular', 9))
        self.label_dataSaida.place(relx=0.4335, rely=0.12)
        
# TREEVIEW
    def colunaNb2(self):
        # FRAME PARA COLUMAS
        self.frameNb2 = Frame(self.frame2, bd=4, bg=col_Entry,
                              highlightbackground=col_Preta, highlightthickness=0)
        self.frameNb2.place(relx=0.01, rely=0.32,
                            relwidth=0.98, relheight=0.65)

    # colunas

        self.colunaNb2 = ttk.Treeview(self.frameNb2, height=4, column=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12"))
        self.colunaNb2.heading("#0", text="")
        self.colunaNb2.heading("#1", text="Ing. Dominio")
        self.colunaNb2.heading("#2", text="Inst. S.O")
        self.colunaNb2.heading("#3", text="S.Operac")
        self.colunaNb2.heading("#4", text="Atual. S.O")
        self.colunaNb2.heading("#5", text="Set. Usuário")
        self.colunaNb2.heading("#6", text="Un. Destino")
        self.colunaNb2.heading("#7", text="Hostname")
        self.colunaNb2.heading("#8", text="Usr. Admin")
        self.colunaNb2.heading("#9", text="Sen. Admin")
        self.colunaNb2.heading("#10", text="Exp. Senha")
        self.colunaNb2.heading("#11", text="Usr.Setor")
        self.colunaNb2.heading("#12", text="Data Saida")
        
        self.colunaNb2.column("#0", width=1)
        self.colunaNb2.column("#1", width=8)
        self.colunaNb2.column("#2", width=12)
        self.colunaNb2.column("#3", width=15)
        self.colunaNb2.column("#4", width=20)
        self.colunaNb2.column("#5", width=25)
        self.colunaNb2.column("#6", width=30)
        self.colunaNb2.column("#7", width=30)
        self.colunaNb2.column("#8", width=30)
        self.colunaNb2.column("#9", width=15)
        self.colunaNb2.column("#10", width=15)
        self.colunaNb2.column("#11", width=15)
        self.colunaNb2.column("#12", width=15)

        self.colunaNb2.place(relx=0.005, rely=0.02,
                             relwidth=0.975, relheight=0.95)

    # scrollbar colunaNb1
        self.colunaNb2Scroll = Scrollbar(self.frameNb2, orient='vertical')
        self.colunaNb2.configure(yscroll=self.colunaNb2Scroll.set)
        self.colunaNb2Scroll.place(
            relx=0.982, rely=0.024, relwidth=0.0195, relheight=0.944)


Apllication()
