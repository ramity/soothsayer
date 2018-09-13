from flask_mongoengine import MongoEngine

engine = MongoEngine()

class BaseModel(engine.Document):

    meta = {"allow_inheritance" : True}
    engine = engine
