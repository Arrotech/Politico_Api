from app.api.v2.models.db_conn import Database
import json
from flask_jwt_extended import jwt_required

Database().create_table()

class OfficesModel(Database):
	"""Initiallization."""

	def __init__(self, category=None, name=None):
		super().__init__()
		self.category = category
		self.name = name
		
	def save(self, category, name):
		"""Create a new offices."""

		print(category, name)
		self.curr.execute(
			''' INSERT INTO offices(category, name)\
			VALUES('{}','{}')\
			 RETURNING category, name'''\
			.format(category, name))
		office = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return office
		
	def get_offices(self):
		"""Fetch all offices"""

		self.curr.execute(''' SELECT * FROM offices''')
		offices = self.curr.fetchall()
		self.conn.commit()
		self.curr.close()
		return json.dumps(offices, default=str)

	def get_office_by_id(self, office_id):
		"""Fetch a single office"""

		self.curr.execute(""" SELECT * FROM offices WHERE office_id={}""".format(office_id ))
		office = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return json.dumps(office, default=str)

	def get_office_name(self, name):
		"""Get an office with specific name."""

		self.curr.execute(''' SELECT * FROM offices WHERE name=%s''',(name, ))
		office = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return json.dumps(office, default=str)