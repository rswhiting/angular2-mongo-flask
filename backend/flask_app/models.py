"""All the database related entities are in this module."""


from flask_security import RoleMixin, MongoEngineUserDatastore, UserMixin
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Role(db.Document, RoleMixin):
    """Create roles in the database."""

    __tablename__ = 'auth_role'
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    def __init__(self, name):
        """Initialize the Role object."""
        self.name = name

    def __repr__(self):
        """String representation of the class."""
        return '<Role %r>' % self.name


class User(db.Document, UserMixin):
    """Create users in the database."""

    __tablename__ = 'auth_user'
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    first_name = db.StringField(max_length=255)
    last_name = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    last_login_at = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip = db.StringField(max_length=45)
    current_login_ip = db.StringField(max_length=45)
    login_count = db.IntField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def __repr__(self):
        """String representation of the class."""
        return '<User %r>' % self.email

user_datastore = MongoEngineUserDatastore(db, User, Role)
