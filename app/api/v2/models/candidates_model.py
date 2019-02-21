from app.api.v2.models.db_conn import Database
import json
from flask_jwt_extended import jwt_required
import psycopg2

Database().create_table()

class CandidatesModel(Database):
	"""Initiallization."""

	def __init__(self, office=None, candidate=None, party=None):
		super().__init__()
		self.office = office
		self.candidate = candidate
		
	def save(self, office, candidate, party):
		"""Create a new candidate."""

		try:
			self.curr.execute(
				''' INSERT INTO candidates(office, candidate, party)\
				VALUES('{}','{}','{}')\
				 RETURNING office, candidate, party'''\
				.format(office, candidate, party))

			candidate = self.curr.fetchone()
			self.conn.commit()
			self.curr.close()
			return candidate

			query = """
					SELECT offices.name, parties.name, users.email FROM candidates\
					INNER JOIN offices ON candidates.office=offices.office_id\
					INNER JOIN users ON candidates.candidate=users.user_id\
					INNER JOIN parties ON candidates.party=parties.party_id;

					"""

			candidate = self.curr.fetchall()

			self.curr.execute(query)
			self.conn.commit()
			self.curr.close()

			return json.dumps(candidate, default=str)
		except psycopg2.IntegrityError:
			return "error"



	# def convert_to_int(id):

 #    try:
 #        value = int(id)
 #        return value
 #    except Exception as e:
 #        return {"message": e}
	