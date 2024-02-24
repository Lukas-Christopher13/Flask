#arquivo separado para os serealizadores!

from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("email", "username")
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)