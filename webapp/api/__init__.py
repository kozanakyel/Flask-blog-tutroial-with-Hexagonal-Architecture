from flask_restful import Api
from .blog.conrollers import PostApi

rest_api = Api()

def create_module(app, **kwargs):
    
    rest_api.add_resource(
        PostApi,
        '/api/post',
        '/api/post/<int:post_id>',  # forgtotten leading slash
    )
    rest_api.init_app(app)