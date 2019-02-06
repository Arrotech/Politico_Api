import unittest
from app import electoral_app
import json
from app.api.v1.views.office_views import Office
from app.api.v1.models.offices_model import OfficesModel
from utils.dummy import create_office, office_keys, get_office, office_category, office_name


class TestOffice(unittest.TestCase):
	"""Test office endpoint."""

	def setUp(self):
		"""Set up the app for testing."""

		self.app = electoral_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

	def test_create_office(self):
		"""Test create a new office."""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'office created successfully!')
		assert response.status_code == 201

	def test_unexisting_officeUrl(self):
		"""Test when unexisting url is provided."""

		response = self.client.get(
			'/api/v2/office')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_office_keys(self):
		"""Test office json keys"""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(office_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid category key')
		assert response.status_code == 400

	def test_get_offices(self):
		"""Test fetching all offices that have been created."""

		response = self.client.get(
			'/api/v2/offices', data=json.dumps(get_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_get_office(self):
		"""Test getting a specific office by id."""

		response = self.client.get(
			'/api/v2/offices/1', data=json.dumps(get_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response.status_code == 200

	def test_unexisting_office(self):
		"""Test fetching unexisting office."""

		response = self.client.get(
			'/api/v2/offices/5')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_office_categoryValue(self):
		"""Test office json values."""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(office_category), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'category is in wrong format')
		assert response.status_code == 400

	def test_office_nameValue(self):
		"""Test office json values."""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(office_name), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'name is in wrong format')
		assert response.status_code == 400


