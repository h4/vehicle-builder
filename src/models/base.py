from gino import Gino

db = Gino()


class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
