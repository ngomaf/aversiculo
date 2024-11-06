from tkinter import Toplevel, PhotoImage, Text
from tkinter.ttk import Frame, Label, Button, Entry, Treeview
from tkinter.ttk import Scrollbar, Separator

import textwrap
from components.writetxt import WriteTxt
from components.cpbase64 import CpBase64


class ViewSetting:

	__slots__ = ['_win', '_border', '_lb_setting', '_body', '_menu', '_vers',
				'_lb_set', '_text', '_book', '_bt_edit', '_bt_delete', 
				'_tv_versicles', '_sc_versicles', '_record',
				'_lb_sucess', '_doc']

	def __init__(self, mother):
		self._win = Toplevel()
		self._win.transient(mother)
		self._win.title('Configurações')
		self._win.iconphoto(False, CpBase64().get_iconlogo())
		self._win.geometry('392x500+100+100')
		self._win.resizable(False, False)
		self._win.configure(bg='#fbfbb8')
		self._win.focus_force()
		self._win.grab_set()

		self._border = Frame(self._win)
		self._border.pack(fill='both', padx=20, pady=20)

		# inicializacao de componentes
		self.show_widgets()

	def setting(self):
		self._menu = Frame(self._body)
		self._menu.pack(fill='x', padx=30, pady=30)

		Button(self._menu, text='Versículos', command=self.sett_versicle, cursor='hand1', style='Menu.TButton').pack(fill='x')
		Button(self._menu, text='Recordes', command=self.records, cursor='hand1', style='Menu.TButton').pack(fill='x', pady=10)
		Button(self._menu, text='Documentação', command=self.doc, cursor='hand1', style='Menu.TButton').pack(fill='x', pady=(0,10))
		Button(self._menu, text='« Voltar', command=self._win.destroy, cursor='hand1', style='Menu.TButton').pack(fill='x')

		Label(self._menu, text='Acerte o versículo 0.1', style='Setting.TLabel').pack(pady=(40,10))

		Label(self._menu, text='Ngoma & Rosa', style='About.TLabel').pack()

	def sett_versicle(self):
		def back():
			self._vers.pack_forget()
			self.setting()

		self._menu.pack_forget()

		self._vers = Frame(self._body)
		self._vers.pack(fill='x')

		Button(self._vers, text='[« Voltar]', command=back, cursor='hand1', style='Back.TButton').pack(anchor='e')

		self._lb_set = Label(self._vers, text='Cadastrar versículo', style='Set.TLabel')
		self._lb_set.pack()

		self._lb_sucess = Label(self._vers, style='True.TLabel')
		self._lb_sucess.pack()

		form = Frame(self._vers)
		form.pack()

		self._text = Text(form, font=('Nunito', 12), fg='#333', height=3, relief='flat')
		self._text.focus_force()
		self._text.pack(pady=5)

		self._book = Entry(form, width=35, style='Book.TEntry')
		self._book.pack(side='left', fill='x')

		def count_vers():
			vers = WriteTxt('get')
			list_vers = vers.get_vers()

			return len(list_vers)

		def set_versicle():
			self._text.focus_force()

			book = self._book.get().strip() + '\n'
			text = self._text.get('1.0', 'end').strip() + '\n'

			if book != '\n' and text != '\n':
				self._book.delete(0, 'end')
				self._text.delete('1.0', 'end')

				result = WriteTxt('get').save_vers(book, text)

				if 'Sucesso' in result['title']:
					def show_msg():
						self._lb_sucess['text'] = ''

					self._lb_sucess['text'] = result['content']
					self._lb_sucess.after(2000, show_msg)

				n_vers['text'] = f'{count_vers()} versículos cadastrados do Novo e Velho'

				print(result['title'])
				print(result['content'])

		Button(form, text='Cadastrar', cursor='hand1', command=set_versicle, style='Set.TButton').pack(padx=(5,0))

		Label(self._vers, text='Estatística', style='Set.TLabel').pack(anchor='w', pady=(50,5))

		n_vers = Label(self._vers, text=f'{count_vers()} versículos cadastrados do Novo e Velho ', style='TLabel')
		n_vers.pack(anchor='w')
		Label(self._vers, text='testamento.', style='TLabel').pack(anchor='w')

		'''
		treeview = Frame(self._vers)
		treeview.pack(fill='x', pady=(10,0))

		buttons = Frame(treeview)
		buttons.pack(fill='x')

		img_edit = PhotoImage(file=r'components/icons/edit.png')
		self._bt_edit = Button(buttons, cursor='hand1', style='Setting.TButton', image=img_edit)
		self._bt_edit.image = img_edit
		# self._bt_edit['command'] = self.on_setting
		self._bt_edit.pack(side='left')

		img_delete = PhotoImage(file=r'components/icons/delete.png')
		self._bt_delete = Button(buttons, cursor='hand1', style='Setting.TButton', image=img_delete)
		self._bt_delete.image = img_delete
		# self._bt_delete['command'] = self.on_setting
		self._bt_delete.pack(side='left')

		self._tv_versicles = Treeview(treeview, selectmode="extended", height=10)
		self._tv_versicles['columns']=('#' ,'Book', 'Text')
		self._tv_versicles.column('#0', width=0, stretch='no')
		self._tv_versicles.column('#', anchor='w', width=20)
		self._tv_versicles.column('Book', anchor='w', width=80)
		self._tv_versicles.column('Text', anchor='w', width=200)

		self._tv_versicles.heading('#0', text='', anchor='w')
		self._tv_versicles.heading('#', text='#', anchor='w')
		self._tv_versicles.heading('Book', text='Livro', anchor='w')
		self._tv_versicles.heading('Text', text='Texto', anchor='w')
		self._tv_versicles.pack(side='left', fill='both', expand=True)

		self._sc_versicles = Scrollbar(treeview, orient='vertical')
		self._sc_versicles.pack(side='left', fill='y', padx=(2,0))
		
		self._tv_versicles.config(yscrollcommand=self._sc_versicles.set)
		self._sc_versicles.config(command=self._tv_versicles.yview)

		for item in range(15):
			self._tv_versicles.insert(parent='', index=item, iid=item, text='', values=(item,'João 3:16','Porque DEUS amou o mundo de tal...'))
		'''

	def records(self):

		def back():
			self._record.pack_forget()
			self.setting()

		self._menu.pack_forget()

		self._record = Frame(self._body)
		self._record.pack(fill='x')

		Button(self._record, text='[« Voltar]', command=back, cursor='hand1', style='Back.TButton').pack(anchor='e')

		bd_raking = Frame(self._record)
		bd_raking.pack(fill='x', pady=(10,0))

		Label(bd_raking, text='Melhor jogador', style='Set.TLabel').pack(pady=(0,15))
		# Label(bd_raking, text='Raking', style='Set.TLabel').pack(pady=(0,15))

		Separator(bd_raking, orient='horizontal').pack(fill='x', pady=(0,20))

		strong = WriteTxt('get').get_record()
		Label(bd_raking, text=f'Nome: {strong[0]} \nPontos: {strong[1]} \nTempo: {strong[2]}s \nData: {strong[3]} {strong[4]}', style='Raking.TLabel').pack(fill='x', pady=(1,0))

	def doc(self):

		def back():
			self._doc.pack_forget()
			self.setting()

		self._menu.pack_forget()

		self._doc = Frame(self._body)
		self._doc.pack(fill='x')

		Button(self._doc, text='[« Voltar]', command=back, cursor='hand1', style='Back.TButton').pack(anchor='e')

		bd_doc = Frame(self._doc)
		bd_doc.pack(fill='x', pady=(10,0))

		doc = WriteTxt('doc')
		tx_doc = Text(bd_doc, font=('Nunito', 12), fg='#666', bg='#fbfbb8', highlightthickness=0, highlightcolor='#fbfbb8', highlightbackground='#fbfbb8', relief='flat')
		tx_doc.pack()

		for line in textwrap.wrap(doc.get_doc(), 45):
			tx_doc.insert('insert', line+'\n')

	def show_widgets(self):
		img_setting = CpBase64().get_iconsettng()
		self._lb_setting = Label(self._border, text=' Configurações', style='Setting2.TLabel', image=img_setting)
		self._lb_setting.image = img_setting
		self._lb_setting['compound'] = 'left'
		self._lb_setting.pack(anchor='w')

		# campo base para menu e entrada de versiculos
		self._body = Frame(self._border)
		self._body.pack(fill='x')

		self.setting()
		