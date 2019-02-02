import unittest
from app import electoral_app
import json
from app.api.v1.views.views import Elections, GetParties
from app.api.v1.models.models import ElectionsModel
from utils.dummy import create_party, empty_parties


class TestDataParcel(unittest.TestCase):

	def setUp(self):

		self.app = electoral_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

	def test_create_party(self):

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(create_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'party created successfully!')
		assert response.status_code == 201

	def test_get(self):

		response = self.client.get(
			'/api/v1/parties', data=json.dumps(create_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_wrong_url(self):
		response = self.client.get(
			'/api/v1/party')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"