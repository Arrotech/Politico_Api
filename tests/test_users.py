import unittest
from app import electoral_app
import json
from app.api.v1.views.user_views import Register
from app.api.v1.views.candidates_views import Candidates
from app.api.v1.models.candidates_model import CandidatesModel
from utils.dummy import create_account, account_keys


class TestUsersAccount(unittest.TestCase):
	"""Testing the users account endpoint."""

	def setUp(self):
		"""Set up the app for testing."""

		self.app = electoral_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

	def test_create_account(self):
		"""Test create a new account."""

		response = self.client.post(
			'/api/v3/users', data=json.dumps(create_account), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Account created successfully')
		assert response.status_code == 201

	def test_account_keys(self):
		"""Test account json keys."""

		response = self.client.post(
			'/api/v3/users', data=json.dumps(account_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid firstname key')
		assert response.status_code == 400