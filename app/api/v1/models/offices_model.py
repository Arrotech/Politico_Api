offices = []

class OfficesModel():         

	def __init__(self):
		"""Initialization."""
		
		self.entries = offices

	def save(self, category, name):
		"""Save a new party that has been created."""

		new_office = {
		"office_id" : len(self.entries)+1,
		"category" : category,
		"name" : name,
		}
		self.entries.append(new_office)
		return self.entries

	def get_all_offices(self):
		"""Fetch all the existing offices."""

		return self.entries

	def get_an_office(self, office_id):
		"""Fetch a specific political office."""

		if self.entries:
			for office in self.entries:
				if office.get('office_id') == office_id:
					return office