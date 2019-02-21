import unittest
import json
from app.api.v2.views.vote import Vote
from app.api.v2.models.voters_model import VotersModel
from utils.dummy import new_vote2, vote_keys2, create_account, user_login, voters_createdOn_value, voters_office_value2, voters_candidate_value2, voters_createdBy_value2
from .base_test import BaseTest

class TestVote(BaseTest):
	"""Test voting endpoint."""
  
	def get_token(self):

		self.client.post('/api/v2/auth/signup', data=json.dumps(create_account),
		content_type='application/json')
		resp = self.client.post('/api/v2/auth/login', data=json.dumps(user_login),
			content_type='application/json')
		access_token = json.loads(resp.get_data(as_text=True))['token']
		auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
		return auth_header

	def test_vote_keys(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/voters', data=json.dumps(vote_keys2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid candidate key')
		assert response.status_code == 400

	def test_office_value(self):
		"""Test office name format."""

		response = self.client.post(
			'/api/v2/voters', data=json.dumps(voters_office_value2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'only positive integer is accepted')
		assert response.status_code == 400

	def test_candidate_value(self):
		"""Test the candidates name format."""

		response = self.client.post(
			'/api/v2/voters', data=json.dumps(voters_candidate_value2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'only positive integer is accepted')
		assert response.status_code == 400

	def test_createdBy_value(self):
		"""Test the voter's name format"""

		response = self.client.post(
			'/api/v2/voters', data=json.dumps(voters_createdBy_value2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'only positive integer is accepted')
		assert response.status_code == 400