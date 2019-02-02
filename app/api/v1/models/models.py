parties = []

class ElectionsModel():         

	def __init__(self):
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






