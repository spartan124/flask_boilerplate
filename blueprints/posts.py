from flask_restx import Namespace, Resource, fields

from models.mongo_models import Post

api = Namespace('posts', description='Post Ops')

post_model = api.model('Post', {
    'author': fields.String(required=False, description='Post Author'),
    'content': fields.String(required=True, description='Post content')
})

@api.route('')
class PostOps(Resource):
    def get(self):
        """Get all post"""
        posts = Post.objects()
        
        return {'message':'Posts fetched successfully', 'data': [post.to_dict() for post in posts]}
    
    @api.expect(post_model)
    def post(self):
        """Create a post"""
        data = api.payload
        
        post = Post(**data)
        post.save()
        
        return {'message':'Post added successfully', 'data': post.to_dict()}