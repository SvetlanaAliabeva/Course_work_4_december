from dao.genre import GenreDAO

class GenreService:
	def __init__(self, dao: GenreDAO):
		self.dao = dao

	def get_one(self, gid):
		genre_one = self.dao.get_one(gid)
		if not genre_one:
			return None
		return genre_one

	def get_all(self, filter):
		return self.dao.get_all(filter)

	def create(self, data):
		return self.dao.create(data)

	def update(self, data):
		self.dao.update(data)
		return self.dao

	def delete(self, gid):
		self.dao.delete(gid)
