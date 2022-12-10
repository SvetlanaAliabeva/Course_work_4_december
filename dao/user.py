from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d("id"))
        user.email = user_d.get("email")
        user.password = user_d.get("password")
        user.name = user_d.get("name")
        user.surname = user_d.get("surname")
        user.favorite_genre = user_d.get("favorite_genre")

        self.session.add(user)
        self.session.commit()
