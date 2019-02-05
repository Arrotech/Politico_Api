import json

parties = []

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

	def get_a_party(self, party_id):
		"""Fetch a specific political party."""

		if self.entries:
			for party in self.entries:
				if party.get('party_id') == party_id:
					return party

	def update_party(self, name, hqAddress, logoUrl):
		"""Returns a tuple as dictionary."""

		party = {
		"name" : name,
		"hqAddress" : hqAddress,
		"logoUrl" : logoUrl,
		}

		return party
