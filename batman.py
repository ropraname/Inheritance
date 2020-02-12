class Man(object):
	def __init__(self):
		print('man is man when its man')

	def man_pii(self):
		print('im man')

	def man_error(self):
		return ('man error!')


class BatMan(Man):
	def __init__(self):
		super().__init__()

	def man_pii(self):
		print('кхм кхм')

	def man_error(self):
		super().bat_error()
		return('but BATMAN have no errors')




		
		