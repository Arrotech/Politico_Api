import unittest
import json
from app.api.v2.views.party_views import Party
from app.api.v2.models.parties_model import PartiesModel
from utils.dummy import party_hqAddress_exists, party_hqAddress_value, get_party2, party_name_exists, create_party2, create_account, user_login, party_name_keys, party_name_value
from .base_test import BaseTest


class TestOffice(BaseTest):
	"""Test office endpoint."""

	def get_token(self):

		self.client.post('/api/v2/auth/signup', data=json.dumps(create_account),
		content_type='application/json')
		resp = self.client.post('/api/v2/auth/login', data=json.dumps(user_login),
			content_type='application/json')
		access_token = json.loads(resp.get_data(as_text=True))['token']
		auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
		return auth_header

	def test_unexisting_officeUrl(self):
		"""Test when unexisting url is provided."""

		response = self.client.get(
			'/api/v2/auth/party')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_get_parties(self):
		"""Test fetching all offices that have been created."""
    
		response = self.client.get(
			'/api/v2/auth/parties', content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_get_party(self):
		"""Test getting a specific party by id."""

		response1 = self.client.post(
			'/api/v2/auth/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		return response1
		response1 = self.client.get(
			'/api/v2/auth/parties/1', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response1.status_code == 200

	def test_delete_party(self):
		"""Test deleting a specific party by id."""

		response1 = self.client.post(
			'/api/v2/auth/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response = self.client.delete(
			'/api/v2/auth/parties/1/delete', content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			'party deleted')
		assert response.status_code == 200

	def test_party_keys(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/auth/parties', data=json.dumps(party_name_keys), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid name key')
		assert response.status_code == 400

	def test_party_nameValue(self):
		"""Test name json values."""

		response = self.client.post(
			'/api/v2/auth/parties', data=json.dumps(party_name_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'name should only contain letters!')
		assert response.status_code == 400

	def test_party_hqAddressValue(self):
		"""Test name json values."""

		response = self.client.post(
			'/api/v2/auth/parties', data=json.dumps(party_hqAddress_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'hqAddress should only contain letters!')
		assert response.status_code == 400

	def test_update_party(self):
		"""Test updating an already existing party."""

		response1 = self.client.post(
			'/api/v2/auth/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		return response1
		response1 = self.client.put(
			'/api/v2/auth/parties/1/edit', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'party updated successfully!')
		assert response1.status_code == 200


