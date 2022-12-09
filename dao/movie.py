# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def get_all(self, filter):

        status = filter.get("status")
        page = filter.get("page") # посмотреть page is not None???

        if status == "new" and page is not None:
            return self.session.query(Movie).order_by(Movie.year.desc()).paginate(int(page), per_page=12).items
        elif page is not None:
            return self.session.query(Movie).paginate(int(page), per_page=12).items
        elif status == "new":
            return self.session.query(Movie).order_by(Movie.year.desc()).all()

        return self.session.query(Movie).all()


    def get_by_director_id(self, value):
        return self.session.query(Movie).filter(Movie.director_id == value).all()

    def get_by_genre_id(self, value):
        return self.session.query(Movie).filter(Movie.genre_id == value).all()

    def get_by_year(self, value):
        return self.session.query(Movie).filter(Movie.year == value).all()


    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, data):
        movie = self.get_one(data.get("id"))
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")
        self.session.add(movie)
        self.session.commit()

    # def update_partial(self, data):
    #     uid = data.get("id")
    #     movie = self.session.query(Movie).get(uid)
    #     return movie


    def delete(self, uid):
        movie = self.get_one(uid) #

        self.session.delete(movie)
        self.session.commit()
