from app.api.v2.models.db_conn import Database
import json


class VotersModel(Database):
	"""Initialization."""

	def __init__(self,createdBy=None,
		office=None,
		candidate=None):

		super().__init__()
		self.createdBy = createdBy
		self.office = office
		self.candidate = candidate

	def save(self, createdBy, office, candidate):
		"""Save information of the new voter"""

		self.curr.execute(
            ''' INSERT INTO voters(createdBy, office, candidate)\
             VALUES('{}','{}','{}')\
             RETURNING createdBy, office, candidate'''\
            .format(createdBy, office, candidate))
		voter = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return voter