import unittest
import json
from app.api.v2.views.petition import Petition
from app.api.v2.models.petitions_model import PetitionsModel
from utils.dummy import new_petition, petition_keys2, petition_date_value, petition_office_value, petitioner_value
from .base_test import BaseTest

class TestPetitions(BaseTest):
	"""Test petitions endpoint."""

	def test_petition(self):
		"""Test filing a new petition."""

		response = self.client.post(
			'/api/v2/auth/petitions', data=json.dumps(new_petition), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'petition filed successfully')
		assert response.status_code == 201

	def test_office_value(self):
		"""Test input format of the office name."""

		response = self.client.post(
			'/api/v2/auth/petitions', data=json.dumps(petition_office_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_petitioner_value(self):
		"""Test input of the petitioner format."""

		response = self.client.post(
			'/api/v2/auth/petitions', data=json.dumps(petitioner_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_petition_keys(self):
		"""Test petition json keys."""

		response = self.client.post(
			'/api/v2/auth/petitions', data=json.dumps(petition_keys2), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid createdBy key')
		assert response.status_code == 400