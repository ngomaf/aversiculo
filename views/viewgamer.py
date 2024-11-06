from tkinter import Toplevel, PhotoImage, Text
from tkinter.ttk import Frame, Label, Button, Entry, Treeview
from tkinter.ttk import Scrollbar

from components.cpbase64 import CpBase64


class ViewGamer:

	__slots__ = ['_win', '_border', '_oportunity', '_et_gamer', '_ugamer',
				'_lb_msg', '_lb_error_msg']

	def __init__(self, mother):
		self._win = Toplevel()
		self._win.transient(mother)
		self._win.title('Configurações')
		self._win.iconphoto(False, CpBase64().get_iconlogo())
		self._win.geometry('392x450+50+160')
		self._win.overrideredirect(True)
		self._win.resizable(False, False)
		self._win.configure(bg='#eeee8c') # fbfbb8
		self._win.focus_force()
		self._win.grab_set()

		self._border = Frame(self._win, style='Gamer.TFrame')
		self._border.pack(fill='both', padx=50, pady=20)

		# inicializacao de componentes
		self.show_widgets()
		self._ugamer = ''

	def comecar(self):
		if self._et_gamer.get() != '':
			self.get_gamer()
			self._win.destroy()
		else:
			self._et_gamer.focus_force()
			self._lb_msg['text'] = ''
			self._lb_error_msg['text'] = 'Digite o seu nome aqui.'
			self._lb_error_msg.after(1500, self.change_msg)

	def change_msg(self):
		self._lb_error_msg['text'] = ''
		self._lb_msg['text'] = 'Digite o seu nome para começar a jogar.'

	def get_gamer(self):
		self._ugamer = self._et_gamer.get().strip().title()

	def show_widgets(self):

		Label(self._border, text='Seu nome', style='Gamer.TLabel').pack(pady=(10,15))

		# toolpit
		toolpit = Frame(self._border, style='Gamer.TFrame')
		toolpit.pack(fill='x')

		self._lb_msg = Label(toolpit, text='Digite o seu nome para começar a jogar.', style='SGamer.TLabel')
		self._lb_msg.pack(side='left')

		self._lb_error_msg = Label(toolpit, style='ErGamer.TLabel')
		self._lb_error_msg.pack(side='left')

		self._et_gamer = Entry(self._border, font=('Nunito', 12), justify='center', width=28)
		self._et_gamer.focus_force()
		self._et_gamer.pack()

		Button(self._border, text='Começar', command=self.comecar, cursor='hand1', style='Game.TButton').pack(fill='x', pady=(15, 0))
		
		Label(self._border, text='            Dicas do jogo*', style='Gamer.TLabel').pack(anchor='w', pady=(50,5))

		Label(self._border, text='                    30 segundos por pergunta.', style='SGamer.TLabel').pack(anchor='w')
		Label(self._border, text='                    Um erro por pergunta.', style='SGamer.TLabel').pack(anchor='w')
		Label(self._border, text='                    Três saltos por jogo.', style='SGamer.TLabel').pack(anchor='w')
