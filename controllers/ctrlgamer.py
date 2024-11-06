from views.viewgamer import ViewGamer


class CtrlGamer:

	__slots__ = ['_view']

	def __init__(self, mother):
		self._view = ViewGamer(mother)
