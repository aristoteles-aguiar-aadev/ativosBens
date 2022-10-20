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

class Apllication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frameHeaderFlooter()
        self.frameSistema()
        self.notebook()
        self.colunaNb1()
        
        root.mainloop()

#TELA
    def tela(self):
        self.root.title("")
        self.root.configure(background=col_Branca)
        self.root.geometry("1366x768")
        self.root.resizable(True, True)
        self.root.maxsize(width=1366, height=768)
        self.root.minsize(width=500, height=400)
    
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

#FRAME SISTEMA
    def frameSistema(self):
        # Frame do sistema-----
        self.frameSistema1 = Frame(
            self.root, bd=4, bg=col_Branca)
        self.frameSistema1.place(
            relx=0.02, rely=0.125, relwidth=0.96, relheight=0.49)



# RADIOBUTTON
        self.radioBt = ttk.Radiobutton(self.frameSistema1, text= "Entrada  |", value="e",)
        self.radioBt.place(relx=0.033, rely=0.02)

        self.radioBt = ttk.Radiobutton(self.frameSistema1, text= "Saida", value="s")
        self.radioBt.place(relx=0.093, rely=0.02)

# COMBOBOX
        self.CbBoxUnEmp = Label(self.frameSistema1, text="Empresa:", bg=col_Branca, font=(
            'Ivy Mode Regular', 9, "bold"))
        self.CbBoxUnEmp.place(relx=0.18, rely=0.02)
        self.CbBoxUnEmp = ttk.Combobox(self.frameSistema1, values=unidEmpresa)
        self.CbBoxUnEmp.place(relx=0.18, rely=0.115, relwidth=0.099)
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

#NOTEBOOK 
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
        self.notebook.add(self.frame1, text='  Entrada de Ativo  ')
        self.notebook.add(self.frame2, text='  Saída de Ativo  ')

#   CONJUNTO FRAME 1 NOTEBOOK

    # codigo_frame1 NOTEBOOK
        self.codigo = Label(self.frame1, text="Codigo",
                            fg=col_Preta, font=('Ivy Mode Regular', 10, 'bold'))
        self.codigo.place(relx=0.01, rely=0.01)

        self.codigo_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.codigo_entry.place(relx=0.01, rely=0.05,
                                relwidth=0.04, relheight=0.045)
    # serie/tombo_frame1 NOTEBOOK
        self.tmbSerie = Label(self.frame1, text="Tombo/Nº Serie",
                              fg=col_Preta, font=('Ivy Mode Regular', 10, 'bold'))
        self.tmbSerie.place(relx=0.06, rely=0.01)
    
        self.tmbSerie_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.tmbSerie_entry.place(
            relx=0.06, rely=0.05, relwidth=0.08, relheight=0.045)
        
    # hostname_frame1 NOTEBOOK

        self.hostName = Label(self.frame1, text="Hostname", fg=col_Preta, font=('Ivy Mode Regular', 10, 'bold'))
        self.hostName.place(relx=0.15, rely=0.01)

        self.hostName_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.hostName_entry.place(
            relx=0.15, rely=0.05, relwidth=0.08, relheight=0.045)

            # COMBOBOX Notebook Frame 1 ( Tecnico, Setor, Sistema Operacional )

    # sistema operacioanal

        self.sistOper = Label(self.frame1, text=" Sistema Operacional", font=(
            'Ivy Mode Regular', 9, 'bold'))
        self.sistOper.place(relx=0.315, rely=0.003)
        self.sistOper = ttk.Combobox(self.frame1, values=sistOper)
        self.sistOper.place(relx=0.32, rely=0.05, relwidth=0.099)
        self.sistOper.set("Informe S.O")
    
    
    # setor do usuario

        self.setorUser = Label(self.frame1, text="Setor do usuário", font=(
            'Ivy Mode Regular', 9, 'bold'))
        self.setorUser.place(relx=0.418, rely=0.003)
        self.setorUser = ttk.Combobox(self.frame1, values=setor)
        self.setorUser.place(relx=0.42, rely=0.05, relwidth=0.099)
        self.setorUser.set("Informe o setor")

    # tecnico responsavel

        self.tecnico = Label(self.frame1, text="Tecnico Responsavel", font=('Ivy Mode Regular', 9, 'bold'))
        self.tecnico.place(relx=0.518, rely=0.003)
        self.tecnico = ttk.Combobox(self.frame1, values=tecnico)
        self.tecnico.place(relx=0.52, rely=0.05, relwidth=0.099)
        self.tecnico.set("Informe o Tecnico")


    # descrição_frame1 NOTEBOOK
        self.descricao = Label(self.frame1, text="Descrição (Equipamento-Modelo)",
                                fg=col_Preta, font=('Ivy Mode Regular', 10, 'bold'))
        self.descricao.place(relx=0.01, rely=0.1)

        self.descricao_entry = Entry(self.frame1, bg=col_Branca, border=3)
        
        self.descricao_entry.place(
            relx=0.01, rely=0.15, relwidth=0.3, relheight=0.045)

    # acessorios_frame1 NOTEBOOK
        self.acessorio = Label(self.frame1, text="Acessórios", 
                               fg=col_Preta, font=('Ivy Mode Regular', 10, 'bold'))
        self.acessorio.place(relx=0.32, rely=0.1)

        self.acessorio_entry = Entry(self.frame1, bg=col_Branca, border=3)
        
        self.acessorio_entry.place(
            relx=0.32, rely=0.15, relwidth=0.3, relheight=0.045)

    # fornecedor/origem_frame1 NOTEBOOK
        self.fornecedor = Label(self.frame1, text="Fornecedor", fg=col_Preta, font=('Ivy Mode Regular', 10, 'bold'))
        self.fornecedor.place(relx=0.01, rely=0.2)

        self.fornecedor_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.fornecedor_entry.place(
            relx=0.01, rely=0.25, relwidth=0.3, relheight=0.045)
    # usuario 

        self.userSetor = Label(self.frame1, text="Usuário do Setor", fg=col_Preta, font=('Ivy Mode Regular', 10, 'bold'))
        self.userSetor.place(relx=0.32, rely=0.2)

        self.userSetor_entry = Entry(self.frame1, bg=col_Branca, border=3)
        self.userSetor_entry.place(
            relx=0.32, rely=0.25, relwidth=0.15, relheight=0.045)

#TREEVIEW
    def colunaNb1(self):
    # FRAME PARA COLUMAS
        self.frameNb1 = Frame(self.frame1, bd=4, bg=col_Entry, highlightbackground=col_Preta, highlightthickness=0)
        self.frameNb1.place(relx=0.01, rely=0.32, relwidth=0.98, relheight=0.65)

    # colunas
     
        self.colunaNb1 = ttk.Treeview(self.frameNb1, height=4, column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
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
        
        self.colunaNb1.place(relx=0.005, rely=0.02, relwidth=0.975, relheight=0.95)

    #scrollbar colunaNb1
        self.colunaNb1Scroll = Scrollbar(self.frameNb1,orient='vertical')
        self.colunaNb1.configure(yscroll=self.colunaNb1Scroll.set)
        self.colunaNb1Scroll.place(relx=0.982, rely= 0.024, relwidth=0.0195, relheight=0.944)


Apllication()
