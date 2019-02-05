import unittest
from app import electoral_app
import json
from app.api.v1.views.petitions_views import Petition
from app.api.v1.models.petitions_model import PetitionsModel
from utils.dummy import new_petition, petition_keys

class TestDataParcel(unittest.TestCase):

	def setUp(self):

		self.app = electoral_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

	def test_petition(self):

		response = self.client.post(
			'/api/v6/petitions', data=json.dumps(new_petition), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'petition filed successfully')
		assert response.status_code == 201

	def test_petition_keys(self):

		response = self.client.post(
			'/api/v6/petitions', data=json.dumps(petition_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid createdOn key')
		assert response.status_code == 400