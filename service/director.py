from dao.director import DirectorDAO

class DirectorService:
	def __init__(self, dao: DirectorDAO):
		self.dao = dao

	def get_one(self, did):
		director_one = self.dao.get_one(did)

		if not director_one:
			return None

		return director_one

	def get_all(self, filters):
		return self.dao.get_all(filters)

	def create(self, data):
		return self.dao.create(data)

	def update(self, data):
		self.dao.update(data)
		return self.dao

	def delete(self, did):
		self.dao.delete(did)
