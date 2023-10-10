
import datetime
from shenlibackend import db

class BaseModel(db.Model):
    """
    paper base class
    """
    __abstract__ = True
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def serialize(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}