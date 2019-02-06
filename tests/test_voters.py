import unittest
from app import electoral_app
import json
from app.api.v1.views.voters_views import Vote
from app.api.v1.models.voters_model import VotersModel
from utils.dummy import new_vote, vote_keys

class TestVote(unittest.TestCase):
	"""Test voting endpoint."""

	def setUp(self):
		"""Set up the app for testing."""

		self.app = electoral_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

	def test_vote(self):
		"""Test a new vote."""

		response = self.client.post(
			'/api/v5/voters', data=json.dumps(new_vote), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'voted successfully')
		assert response.status_code == 201

	def test_vote_keys(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v5/voters', data=json.dumps(vote_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid candidate key')
		assert response.status_code == 400