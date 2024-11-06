
class WriteTxt:

	__slots__ = []

	def __init__(self, sel, data=None):
		if sel == 'record':
			self.records(data)
		elif sel == 'vers':
			self.save_vers(data)
		elif sel == 'doc':
			self.get_doc()
		elif sel == 'get':
			pass
		else:
			return {'title': '[Erro]', 'content': 'Opção invalida.'}

	def records(self, data):
		path = 'components/others/records.txt'
		lines = []

		arquive = open(path)
		for line in arquive:
			line = line.split()
			lines.append(line)
		arquive.close()
		
		if len(lines) > 0 and int(lines[0][1]) <= int(data[0]):
			arquive = open(path, 'w')
			data = f'{data[2]} {data[0]} {data[1]} {data[3]}'
			arquive.write(data)
			arquive.close()

	def get_record(self):
		path = 'components/others/records.txt'
		lines = []

		arquive = open(path)
		for line in arquive:
			line = line.split()
			lines.append(line)
		arquive.close()

		return lines[0]

	def save_vers(self, book, text):
		path = 'components/others/versicles.txt'

		arquive = open(path, 'a')
		arquive.write(book)
		arquive.write(text)

		arquive.close()
		return {'title': 'Sucesso!', 'content': 'Vercículo cadastrado com sucesso.'}


	def get_vers(self):
		path = 'components/others/versicles.txt'
		lines = []
		items = []

		arquive = open(path)
		c = 0
		for line in arquive:
			items.append(line[:-1])
			c += 1
			if c > 1:
				lines.append(items)
				items = []
				c = 0
		arquive.close()

		return lines

	def get_doc(self):
		path = 'components/others/doc.txt'

		arquive = open(path, 'r')
		doc = arquive.read()
		arquive.close()

		return doc
