from views.viewsetting import ViewSetting


class CtrlSetting:

	__slots__ = ['_view']

	def __init__(self, mother):
		self._view = ViewSetting(mother)