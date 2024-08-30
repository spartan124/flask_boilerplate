from datetime import datetime, timezone
from mongoengine import Document, StringField, DateTimeField, BooleanField, EmbeddedDocument, EmbeddedDocumentField, IntField, ListField, DictField, ObjectIdField, EnumField


class Post(Document):
    author = StringField(required=True, max_length=36, default='Anonymous')
    content = StringField(max_length=500)
    created_at = DateTimeField(default = lambda: datetime.now(timezone.utc) )
    
    def to_dict(self):
        return {
            "id": str(self.id),  # Convert ObjectId to string
            "content": self.content,
            "author": self.author,
            "created_at": self.created_at.isoformat()  # Convert datetime to ISO format
        }