from tkinter import Tk, PhotoImage

from controllers.ctrlhome import CtrlHome
from components.styleapp import StyleApp
from components.cpbase64 import CpBase64


class App:

	__slots__ = ['_root', '_home', '_imgs']

	def __init__(self):
		self._root = Tk()

		# controllers
		self._home = CtrlHome(self._root)
		self._imgs = CpBase64()

		#
		# stilos
		StyleApp()

	def run(self):
		self._root.title('Jogo Acerte o versículo')
		self._root.iconphoto(False, self._imgs.get_iconlogo())
		self._root.geometry('392x600+50+50')
		self._root.resizable(False, False)
		self._root.configure(bg='#fbfbb8')
		self._root.mainloop()
