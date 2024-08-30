from datetime import datetime, timezone
from config import db
from uuid import uuid4

def gen_uuid():
    return str(uuid4())

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(36), primary_key=True, default=gen_uuid, unique=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
    
class User(BaseModel):
    __tablename__ = 'users'
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(36), nullable=False, unique=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }
    