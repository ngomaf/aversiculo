from tkinter.ttk import Style


class StyleApp:

	__slots__ = []

	def __init__(self):

		# fontes
		farabian = ('ARABIAN KNIGHT', 11)
		fnunito = ('Nunito', 10)
		fnunito1 = ('Nunito', 12)
		fnunito_bold = ('Nunito', 10, 'bold')
		fnunito_medium = ('Nunito', 14)
		fnunito_big = ('Nunito', 16)

		# estilo
		style = Style()
		style.theme_use('clam')

		# janela princiapal
		style.configure('TLabel', font=fnunito, justify='center', foreground='#666', background='#fbfbb8', padding=0, borderwidth=0)
		style.configure('Setting.TLabel', font=farabian, foreground='#0a0a63')
		style.configure('Time.TLabel', font=fnunito, foreground='#bbbbbb')
		style.configure('Msb.TLabel', font=fnunito_bold, justify='center', foreground='#666', background='#fbfbb8', padding=0, borderwidth=0)
		style.configure('Versicle.TLabel', font=fnunito_medium, foreground='#0a0a63')
		style.configure('Oportunity.TLabel', font=fnunito, foreground='#a70000')
		style.configure('True.TLabel', font=fnunito, foreground='#0aff00')
		style.configure('ErrorTitle.TLabel', font=fnunito, foreground='#ff0000')
		style.configure('ErrorMsg.TLabel', font=fnunito_medium, foreground='#ff0000')
		style.configure('SucessTitle.TLabel', font=fnunito, foreground='#0aff00')
		style.configure('SucessMsg.TLabel', font=fnunito_medium, foreground='#0aff00')
		style.configure('PointResult.TLabel', font=fnunito_big, foreground='#666')
		style.configure('TimeResult.TLabel', font=fnunito, foreground='#bbbbbb')
		style.configure('ClassResult.TLabel', font=fnunito, foreground='#0a0a63')
		style.configure('Setting.TButton', padding=0, background='#fbfbb8', relief='')
		style.configure('Game.TButton', font=fnunito_medium, padding=(0, 8), foreground='white', background='#3f8efc')
		style.configure('TEntry', foreground='#0a0a63', padding=(5,8))
		style.configure('TFrame', background='#fbfbb8')

		# map
		style.map('Setting.TButton',
             background=[('pressed', '!focus', '#3f8efc'), ('active', '#fff')],
             highlightcolor=[('focus', 'green'), ('!focus', 'red')],
             relief=[('pressed', 'flat'), ('!pressed', 'flat')])
		style.map('Game.TButton',
             foreground=[('pressed', 'orange'), ('active', '#fff')],
             background=[('pressed', '!focus', '#375777'), ('active', '#26AAFF')],
             relief=[('pressed', 'groove'), ('!pressed', 'flat')])

		# window setting
		style.configure('Setting2.TLabel', font=fnunito_bold, foreground='#0a0a63', padding=0, background='#fbfbb8', relief='')
		style.configure('Set.TLabel', font=fnunito_medium, padding=0, background='#fbfbb8', relief='')
		style.configure('About.TLabel', font=fnunito, foreground='#3f8efc')
		style.configure('Raking.TLabel', padding=5, font=fnunito1, justify='left', foreground='#0a0a63', background='#fff')
		style.configure('Menu.TButton', font=fnunito, foreground='white', background='#3f8efc')
		style.configure('Back.TButton', font=fnunito, width=7, borderwidth=0, padding=0, foreground='#ff0000', background='#fbfbb8', relief='flat')
		style.configure('Set.TButton', padding=(3,5), borderwidth=0, font=fnunito, foreground='white', background='#3f8efc')
		style.configure('Book.TEntry', padding=5, font=fnunito1, foreground='#333', relief='flat')

		style.configure('Treeview', font=fnunito, borderwidth=0, background='#E6E6E6')
		style.configure('Heading', font=fnunito_bold, padding=(3, 6), borderwidth=0, relief='ridge', background='#D8D8D8')
		style.configure('TScrollbar', width=4, borderwidth=0, arrowsize=4, arrowcolor='#188fdd', background='#188fdd', troughtcolor='#E6E6E6', relief='ridge')

		style.map('Treeview',
            background=[('selected', '#188fdd')])
		style.map('TScrollbar',
             arrowcolor=[('pressed', '#188fdd'), ('active', '#26AAFF')],
             background=[('pressed', '!focus', '#188fdd'), ('active', '#26AAFF')],
             relief=[('pressed', 'groove'), ('!pressed', 'flat')])

		# map
		style.map('Menu.TButton',
             foreground=[('pressed', 'orange'), ('active', '#fff')],
             background=[('pressed', '!focus', '#375777'), ('active', '#26AAFF')],
             relief=[('pressed', 'groove'), ('!pressed', 'flat')])

		style.map('Set.TButton',
             foreground=[('pressed', 'orange'), ('active', '#fff')],
             background=[('pressed', '!focus', '#375777'), ('active', '#26AAFF')],
             relief=[('pressed', 'groove'), ('!pressed', 'flat')])

		style.map('Back.TButton',
             foreground=[('pressed', 'orange'), ('active', '#a70000')],
             background=[('pressed', '!focus', '#375777'), ('active', '#fbfbb8')],
             relief=[('pressed', 'groove'), ('!pressed', 'flat')])

		# gamer
		style.configure('Gamer.TLabel', font=fnunito_medium, padding=0, background='#eeee8c', relief='')
		style.configure('SGamer.TLabel', font=fnunito, padding=0, background='#eeee8c', relief='')
		style.configure('ErGamer.TLabel', font=fnunito, padding=0, foreground='#ff0000', background='#eeee8c', relief='')
		style.configure('Gamer.TFrame', background='#eeee8c')

