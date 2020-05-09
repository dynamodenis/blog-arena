from . import  db

class RegularUser(db.Model):
    __tablename__='regular_user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(50))

def __repr__(self):
    return f"User {self.username}"