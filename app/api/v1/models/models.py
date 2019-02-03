parties = []
offices = []

class PartiesModel():         

	def __init__(self):
		"""Initialization."""
		
		self.entries = parties

	def save(self, name, hqAddress, logoUrl):
		"""Save a new party that has been created."""

		new_party = {
		"party_id" : len(self.entries)+1,
		"name" : name,
		"hqAddress" : hqAddress,
		"logoUrl" : logoUrl,
		
		}
		self.entries.append(new_party)
		return self.entries

	def get_all_parties(self):
		"""Fetch all the existing parties."""

		return self.entries

	def get_party_by_id(self, party_id):
		"""Fetch a specific political party."""

		if self.entries:
			for party in self.entries:
				if party.get('party_id') == party_id:
					return party

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





