from views.viewhome import ViewHome


class CtrlHome:

	__slots__ = ['_view']

	def __init__(self, mother):
		self._view = ViewHome(mother)
