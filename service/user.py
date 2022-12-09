import hashlib
import base64
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO

class UserService:
	def __init__(self, dao: UserDAO):
		self.dao = dao

	def get_one(self, uid):
		return self.dao.get_one(uid)

	def get_email(self, email):
		return self.dao.get_by_email(email)


	def get_all(self):
		return self.dao.get_all()

	def create(self, data):
		data["password"] = self.get_hash(data.get("password"))   # кодирование пароля
		return self.dao.create(data)

	def update(self, data):
		self.dao.update(data)
		return self.dao

	def delete(self, uid):
		self.dao.delete(uid)

	def get_hash(self, password):
		"""
		получаем кодированный пароль
		"""
		return base64.b64encode(hashlib.pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),  # Convert the password to bytes
			PWD_HASH_SALT,
			PWD_HASH_ITERATIONS
		))

	def compare_passwords(self, password_hash, request_password) -> bool:
		return hmac.compare_digest(
			password_hash,
			self.get_hash(request_password)
			)
