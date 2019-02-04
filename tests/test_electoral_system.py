import unittest
from app import electoral_app
import json
from app.api.v1.views.party_views import CreateParty, GetParties, GetParty, DeleteParty
from app.api.v1.views.office_views import CreateOffice, GetOffices, GetOffice, DeleteOffice
from app.api.v1.models.parties_model import PartiesModel
from app.api.v1.models.offices_model import OfficesModel
from utils.dummy import create_party, get_party, create_office, office_keys, get_office, party, party_keys


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
			'/api/v1/parties', data=json.dumps(party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_party_wrong_url(self):

		response = self.client.get(
			'/api/v1/party')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_get_party(self):

		response = self.client.get(
			'/api/v1/parties/1', data=json.dumps(get_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result["message"],
			"success")
		assert response.status_code == 200

	def test_unexisting_party(self):

		response = self.client.get(
			'/api/v1/parties/5')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_party_keys(self):

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid name key')
		assert response.status_code == 400

	def test_create_office(self):

		response = self.client.post(
			'/api/v1/offices', data=json.dumps(create_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'office created successfully!')
		assert response.status_code == 201

	def test_office_wrong_url(self):

		response = self.client.get(
			'/api/v1/office')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_office_keys(self):

		response = self.client.post(
			'/api/v1/offices', data=json.dumps(office_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid category key')
		assert response.status_code == 400

	def test_get(self):

		response = self.client.get(
			'/api/v1/offices', data=json.dumps(get_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_get_office(self):

		response = self.client.get(
			'/api/v1/offices/1', data=json.dumps(get_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response.status_code == 200

	def test_unexisting_office(self):

		response = self.client.get(
			'/api/v1/offices/5')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"


