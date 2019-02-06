import unittest
from app import electoral_app
import json
from app.api.v1.views.party_views import Party
from app.api.v1.models.parties_model import PartiesModel
from utils.dummy import create_party, get_party, party, party_keys, party_name, party_hqAddress, party_logoUrl, update_party


class TestParty(unittest.TestCase):
	"""Test party endpoints."""

	def setUp(self):
		"""Set up the app for testing."""

		self.app = electoral_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

	def test_create_party(self):
		"""Test when a user creates a new party."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(create_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'party created successfully!')
		assert response.status_code == 201

	def test_get_parties(self):
		"""Test when a user gets all parties."""

		response = self.client.get(
			'/api/v1/parties', data=json.dumps(party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_update_party(self):
		"""Test when a user wants to edit a specific party."""

		response = self.client.patch(
			'/api/v1/parties/1/edit', data=json.dumps(update_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"party updated successfully")
		assert response.status_code == 200

	def test_unexisting_partyUrl(self):
		"""Test when a user provides unexisting url."""

		response = self.client.get(
			'/api/v1/party')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_get_party(self):
		"""Test when a user wants to fetch a specific party."""

		response = self.client.get(
			'/api/v1/parties/1', data=json.dumps(get_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result["message"],
			"success")
		assert response.status_code == 200

	def test_unexisting_party(self):
		"""Test when a user wants to fetch unexisting party."""

		response = self.client.get(
			'/api/v1/parties/5')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_party_keys(self):
		"""Test party json keys."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid name key')
		assert response.status_code == 400

	def test_party_nameValue(self):
		"""Test party json values."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_name), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'name is in wrong format')
		assert response.status_code == 400

	def test_party_hqAddressValue(self):
		"""Test party json values."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_hqAddress), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'hqAddress is in wrong format')
		assert response.status_code == 400

	def test_party_logoUrlValue(self):
		"""Test party json values."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_logoUrl), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'logoUrl is in wrong format')
		assert response.status_code == 400
