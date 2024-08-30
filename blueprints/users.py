from flask_restx import Namespace, Resource, fields

from models.sql_models import User
from config import db

api = Namespace('users', description="User related ops")

@api.route('')
class UserOps(Resource):
    def get(self):
        """Get all Users"""
        
        users = User.query.all()
        
        return {'message':'Fetched all Users', 'data': [user.to_dict() for user in users]}, 200
    
    
    user_model = api.model("User model", {
        "username": fields.String(description="The username"),
        "email": fields.String(description="The email"),
    })
    @api.expect(user_model)
    def post(self):
        """Create a user"""
        data = api.payload
        
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'New User added', 'data': new_user.to_dict()}