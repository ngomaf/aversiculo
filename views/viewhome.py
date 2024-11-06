from tkinter import PhotoImage
from tkinter.ttk import Frame, Label, Button, Entry
import textwrap

from random import randint
from datetime import datetime
import unicodedata
import base64

from controllers.ctrlsetting import CtrlSetting
from controllers.ctrlgamer import CtrlGamer
from components.writetxt import WriteTxt
from components.cpbase64 import CpBase64


class ViewHome:

	__slots__ = ['_mother', '_top', '_gamer', '_border', '_lb_points', '_bt_setting', 
				'_lb_time', '_body', '_versiculo', '_lb_versiculo','_oportunity',  
				'_et_versicle', '_true', '_n_error', '_n_sucess', '_lb_gamer', 
				'_vers_list', '_unid', '_book', '_points', '_time', '_time_state',
				'_my_time', '_date', '_vers_list2', '_n_jump', '_bt_jump', 
				'_time_now', '_imgs']

	def __init__(self, mother):
		self._mother = mother
		self._top = Frame(self._mother)
		self._top.pack()

		self._border = Frame(self._mother)
		self._border.pack(fill='both', expand=True, padx=(28, 20), pady=0)

		# variaveis globais
		self._n_error = 0
		self._n_sucess = 0
		self._n_jump = 3
		self._points = 0

		self._time = 0
		self._time_now = 0
		self._time_state = False
		self._date = ''

		self._vers_list =  WriteTxt('get').get_vers()
		self._imgs = CpBase64()

		# inicializando metodos
		self.show_widgets()
		self.show_gamer()

	def show_gamer(self):
		self._gamer = CtrlGamer(self._mother)

	def vers_generator(self):
		self._lb_versiculo['text'] = ''

		self._unid = randint(0, len(self._vers_list)-1)
		self._book = self._vers_list[self._unid][0]

		self._versiculo = self._vers_list[self._unid][1]
		self._vers_list.pop(self._unid)

		# quebra de linha
		for line in textwrap.wrap(self._versiculo, 40):
			self._lb_versiculo['text'] += line + '\n'

	def togame(self):

		if self._time == 0:
			self.timer()
			self._lb_gamer['text'] = f'Jogador: {self._gamer._view._ugamer}'
		
		data = self._et_versicle.get().strip()
		my_time = self._time_now
		if data != '':
			slug_data = self.slug_gernerator(data)
			slug_book = self.slug_gernerator(self._book)
			if slug_data == slug_book:
				self._oportunity['text'] = ''
				self._true['text'] = 'Você acertou.'
				self._true.after(1500, self.new_oportunity)

				self.vers_generator()

				self._n_error = 0
				self._n_sucess += 1
				self._points += 1
				self._time_now = 0

				self._lb_points['text'] = f'Pontos: {self._points}'

				if self._n_sucess == 30:
					date = datetime.now()
					self._date = date.strftime('%d.%m.%Y %H:%M')
					
					WriteTxt('record', [f'{self._points}', f'{self._time}', self._gamer._view._ugamer, self._date])

					self.shampion()
					self._lb_time.after_cancel(self._my_time)
					self._vers_list =  WriteTxt('get').get_vers() # reiniciar a lista de versiculos
					self.new_oportunity()
					self._time = 0
					self._points = 0
					self._n_sucess = 0
					self._n_jump = 3

					self._lb_points['text'] = 'Pontos: 0'
					self._lb_time['text'] = 'Tempo: 0s'
					self._lb_gamer['text'] = 'Jogador: `..´'
			else:
				self._oportunity['text'] = 'Resposta errada.'
				self._oportunity.after(1500, self.show_oportunity)

				self._n_error += 1

				if self._n_error > 1:
					date = datetime.now()
					self._date = date.strftime('%d.%m.%Y %H:%M')

					WriteTxt('record', [f'{self._points}', f'{self._time}', self._gamer._view._ugamer, self._date])

					self.loss()
					self._vers_list =  WriteTxt('get').get_vers() # reiniciar a lista de versiculos
					self.new_oportunity()
					
					self._lb_time.after_cancel(self._my_time)
					self._time = 0
					self._points = 0
					self._n_error = 0
					self._n_sucess = 0
					self._time_now = 0
					self._n_jump = 3

					self._lb_points['text'] = 'Pontos: 0'
					self._lb_time['text'] = 'Tempo: 0s'
					self._lb_gamer['text'] = 'Jogador: `..´'
					
		else:
			self._et_versicle.focus_force()
			self._oportunity['text'] = '[Erro!] Campo vazio.'
			self._oportunity.after(1500, self.entry_empty)

	def tojump(self):
		self._et_versicle.focus_force()
		if self._n_jump > 0:
			if self._time == 0:
				self.timer()
				self._lb_gamer['text'] = f'Jogador: {self._gamer._view._ugamer}'

			self._et_versicle.focus_force()
			self.vers_generator()

			self._n_jump -= 1
			self._time_now = 0
			self._bt_jump['text'] = f'Saltar {self._n_jump} »'

	def new_oportunity(self):
		msg = 'Tentativa 1/2'
		self._true['text'] = ''
		self._oportunity['text'] = msg
		self._et_versicle.focus_force()
		self._et_versicle.delete(0, 'end')

	def show_oportunity(self):
		msg = 'Última tentativa.'
		self._oportunity['text'] = msg
		self._et_versicle.focus_force()

	def entry_empty(self):
		msg = 'Tentativa 1/2'
		self._oportunity['text'] = msg

	def loss(self):
		self._body.pack_forget()

		self._body = Frame(self._border)
		self._body.pack(pady=(30,0))

		self._lb_points['text'] = 'Resultado'
		self._lb_time['text'] = ''

		img_error = self._imgs.get_iconerror()
		lb_error = Label(self._body, image=img_error)
		lb_error.image = img_error
		lb_error.pack()

		classific = self.classific(self._points)

		Label(self._body, text='Que mal!', style='ErrorTitle.TLabel').pack(pady=(10, 0))
		Label(self._body, text=f'{self._gamer._view._ugamer}', style='ErrorMsg.TLabel').pack()
		Label(self._body, text='Você perdeu.', style='ErrorMsg.TLabel').pack(pady=(0, 20))

		Label(self._body, text=f'Conseguiste {self._points} pontos', style='PointResult.TLabel').pack()
		Label(self._body, text=f'Tempo: {self._time} segundos', style='TimeResult.TLabel').pack(pady=(10,8))
		Label(self._body, text=f'{classific}', style='ClassResult.TLabel').pack()

		button = Frame(self._body)
		button.pack(fill='x')

		Button(button, text='« Voltar a jogar', command=self.back, cursor='hand1', style='Game.TButton').pack(fill='x', pady=(25, 0))

	def shampion(self):
		self._body.pack_forget()

		self._body = Frame(self._border)
		self._body.pack(pady=(30,0))

		self._lb_points['text'] = 'Resultado'
		self._lb_time['text'] = ''

		img_sucess = self._imgs.get_iconsucess()
		lb_sucess = Label(self._body, image=img_sucess)
		lb_sucess.image = img_sucess
		lb_sucess.pack()

		classific = self.classific(self._points)

		Label(self._body, text='Parabens!', style='SucessTitle.TLabel').pack(pady=(10, 0))
		Label(self._body, text=f'{self._gamer._view._ugamer}', style='SucessMsg.TLabel').pack()
		Label(self._body, text='Você finalizou o jogo.', style='SucessMsg.TLabel').pack(pady=(0, 20))

		Label(self._body, text=f'Conseguiste {self._points} pontos', style='PointResult.TLabel').pack()
		Label(self._body, text=f'Tempo: {self._time} segundos', style='TimeResult.TLabel').pack(pady=(10,8))
		Label(self._body, text=f'{classific}', style='ClassResult.TLabel').pack()

		button = Frame(self._body)
		button.pack(fill='x')

		Button(button, text='« Voltar a jogar', command=self.back, cursor='hand1', style='Game.TButton').pack(fill='x', pady=(25, 0))

	def question(self):
		self._body = Frame(self._border)
		self._body.pack(fill='x')

		self._lb_points['text'] = 'Pontos: 0'
		self._lb_time['text'] = 'Time: 0s'

		img_question = self._imgs.get_iconquestion()
		lb_question = Label(self._body, image=img_question)
		lb_question.image = img_question
		lb_question.pack()

		self._versiculo = '''Porque DEUS amou o mundo de tal maneira que deu...'''

		Label(self._body, text='Qual é o livro, capítulo e, versículo\nque diz:', style='Msb.TLabel').pack(pady=(10, 15))
		self._lb_versiculo = Label(self._body, style='Versicle.TLabel', text='')

		# quebra de linha
		for line in textwrap.wrap(self._versiculo, 45):
			self._lb_versiculo['text'] += line + '\n'

		self._lb_versiculo.pack()

		# jogar
		entry_button = Frame(self._body)
		entry_button.pack()

		# toolpit
		toolpit = Frame(entry_button)
		toolpit.pack(fill='x')

		Label(toolpit, text='Exemplo: 2 Corintíos 5:17').pack(side='left')

		self._oportunity = Label(toolpit, text='Tentativa 1/2', style='Oportunity.TLabel')
		self._oportunity.pack(side='right')

		self._true = Label(toolpit, style='True.TLabel')
		self._true.pack(side='right')

		self._et_versicle = Entry(entry_button, font=('Nunito', 12), justify='center', width=28)
		# self._et_versicle.focus_force()
		self._et_versicle.pack()

		Button(entry_button, text='Jogar', command=self.togame, cursor='hand1', style='Game.TButton').pack(fill='x', pady=(15, 0))
		self._bt_jump = Button(entry_button, text='Saltar 3 »', command=self.tojump, cursor='hand1', style='Back.TButton')
		self._bt_jump.pack(anchor='e', pady=(5, 0))
		self.vers_generator()
		
	def classific(self, point):
		if point < 6:
			level = 'Péssimo'
		elif point < 15:
			level = 'Normal'
		elif point < 25:
			level = 'Bom'
		else:
			level = 'Excelente'

		'''if point < 26:
			level = 'Péssimo'
		elif point < 51:
			level = 'Mau'
		elif point < 76:
			level = 'Bom'
		else:
			level = 'Excelente'''

		return level

	def timer(self):
		self._time += 1
		self._time_now  += 1
		self._lb_time['text'] = f'Tempo: {self._time_now}s'
		self._my_time = self._lb_time.after(1000, self.timer)

		if self._time_now > 30:
			self.loss()
			self.new_oportunity()
			
			self._lb_time.after_cancel(self._my_time)
			self._time = 0
			self._points = 0
			self._n_error = 0
			self._n_sucess = 0
			self._time_now = 0
			self._n_jump = 3

			self._lb_points['text'] = 'Pontos: 0'
			self._lb_time['text'] = 'Tempo: 0s'
			self._lb_gamer['text'] = 'Jogador: `..´'

	def back(self):
		self._body.pack_forget()
		self.question()
		self.show_gamer()

	def on_setting(self):
		CtrlSetting(self._mother)

	def slug_gernerator(self, text):
		data = unicodedata.normalize("NFD", text)
		data = data.encode("ascii", "ignore")
		data = data.decode("utf-8")

		data = data.lower()
		data = data.split()
		slug = ''.join(data)

		return slug

	def show_widgets(self):
		# topo e logo
		img_toplogo = self._imgs.get_imgtop()
		toplogo = Label(self._top, image=img_toplogo)
		toplogo.image = img_toplogo
		toplogo.pack()

		setting = Frame(self._border)
		setting.pack(fill='x')

		time = Frame(self._border)
		time.pack(fill='x')

		self._lb_points = Label(setting, text='Pontos: 0', style='Setting.TLabel')
		self._lb_points.pack(side='left')

		img_setting = self._imgs.get_iconsettng()
		self._bt_setting = Button(setting, cursor='hand1', style='Setting.TButton', image=img_setting)
		self._bt_setting.image = img_setting
		self._bt_setting['command'] = self.on_setting
		self._bt_setting.pack(side='right')

		self._lb_gamer = Label(time, text='Jogador: `..´')
		self._lb_gamer.pack(side='left')
		self._lb_time = Label(time, text='Tempo: 0s', style='Time.TLabel')
		self._lb_time.pack(side='right')

		self.question()
