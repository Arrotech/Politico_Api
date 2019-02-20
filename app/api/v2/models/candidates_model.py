# from app.api.v2.models.db_conn import Database
# import json
# from flask_jwt_extended import jwt_required

# Database().create_table()

# class CandidatesModel(Database):
# 	"""Initiallization."""

# 	def __init__(self, office=None, user=None):
# 		super().__init__()
# 		self.office = office
# 		self.user = user
		
# 	def save(self, office, user):
# 		"""Create a new candidate."""

# 		print(office, user)
# 		self.curr.execute(
# 			''' INSERT INTO candidates(office, user)\
# 			VALUES('{}','{}')\
# 			 RETURNING office, user'''\
# 			.format(office, user))
# 		candidate = self.curr.fetchone()
# 		self.conn.commit()
# 		self.curr.close()
# 		return candidate
# 		