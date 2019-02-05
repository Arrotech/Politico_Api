import unittest
from app import electoral_app
import json
from app.api.v1.views.party_views import Party
from app.api.v1.views.office_views import Office
from app.api.v1.models.parties_model import PartiesModel
from app.api.v1.models.offices_model import OfficesModel
from utils.dummy import create_party, get_party, create_office, office_keys, get_office, party, party_keys, office_category, office_name, party_name, party_hqAddress, party_logoUrl


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

	def test_get_parties(self):

		response = self.client.get(
			'/api/v1/parties', data=json.dumps(party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_edit_party(self):

		response = self.client.put(
			'/api/v1/parties/1/edit', data=json.dumps(party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"party updated successfully")
		assert response.status_code == 200

	def test_unexisting_partyUrl(self):

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

	def test_office_nameValue(self):

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_name), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'name is in wrong format')
		assert response.status_code == 400

	def test_office_hqAddressValue(self):

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_hqAddress), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'hqAddress is in wrong format')
		assert response.status_code == 400

	def test_office_logoUrlValue(self):

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_logoUrl), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'logoUrl is in wrong format')
		assert response.status_code == 400

	def test_create_office(self):

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'office created successfully!')
		assert response.status_code == 201

	def test_unexisting_officeUrl(self):

		response = self.client.get(
			'/api/v2/office')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_office_keys(self):

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(office_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid category key')
		assert response.status_code == 400

	def test_get_offices(self):

		response = self.client.get(
			'/api/v2/offices', data=json.dumps(get_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_get_office(self):

		response = self.client.get(
			'/api/v2/offices/1', data=json.dumps(get_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response.status_code == 200

	def test_unexisting_office(self):

		response = self.client.get(
			'/api/v2/offices/5')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_office_categoryValue(self):

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(office_category), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'category is in wrong format')
		assert response.status_code == 400

	def test_office_nameValue(self):

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(office_name), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'name is in wrong format')
		assert response.status_code == 400


