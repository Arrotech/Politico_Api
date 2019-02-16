import unittest
import json
from app.api.v2.views.auth_views import Register
from app.api.v2.models.users_model import UsersModel
from utils.dummy import create_account, account_keys, email_value, passport_value, new_account, phone_value, firstname_value, lastname_value, othername_value, role_value, user_login, unregistered_user,  email_exists, phone_exists, passport_exists
from .base_test import BaseTest

class TestUsersAccount(BaseTest):
	"""Testing the users account endpoint."""

	def get_token(self):

		self.client.post('/api/v2/auth/signup', data=json.dumps(create_account),
		content_type='application/json')
		resp = self.client.post('/api/v2/auth/login', data=json.dumps(user_login),
			content_type='application/json')
		access_token = json.loads(resp.get_data(as_text=True))['token']
		auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
		return auth_header

	def test_email_exists(self):
		"""Test create a new account."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(email_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Email already exists!')
		assert response.status_code == 400

	def test_phoneNumber_exists(self):
		"""Test create a new account."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(phone_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'phoneNumber already exists!')
		assert response.status_code == 400

	def test_passportUrl_exists(self):
		"""Test create a new account."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(passport_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'passportUrl already in use!')
		assert response.status_code == 400

	def test_signin_account(self):
		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(user_login), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'successfully logged in email@gmail.co.ke', msg='not allowed')
		assert response.status_code == 200

	def test_unexisting_url(self):
		response = self.client.post(
			'/api/v2/auth/lo8563gin', data=json.dumps(user_login), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['status'], 'not found', msg='not allowed')
		assert response.status_code == 404

	def test_unexisting_user(self):
		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(unregistered_user), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['status'], 'not found', msg='not allowed')
		assert response.status_code == 404

	def test_account_keys(self):
		"""Test account json keys."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(account_keys), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid firstname key')
		assert response.status_code == 400

	def test_account_emailValue(self):
		"""Test the account email format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(email_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Email is in the wrong format')
		assert response.status_code == 400

	def test_firstname_value(self):
		"""Test the account firstname format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(firstname_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'firstname is in wrong format')
		assert response.status_code == 400

	def test_lastname_value(self):
		"""Test the account lastname format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(lastname_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'lastname is in wrong format')
		assert response.status_code == 400

	def test_role_value(self):
		"""Test the account role format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(role_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'role is in wrong format')
		assert response.status_code == 400

	def test_account_phoneValue(self):
		"""Test the account phone number format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(phone_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'phone number is in the wrong format')
		assert response.status_code == 400

	def test_account_passportValue(self):
		"""Test the account passport url format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(passport_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'passportUrl is in the wrong format')
		assert response.status_code == 400