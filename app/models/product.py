from .db import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    image_link = db.Column(db.String(), nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('product_categories.id'), nullable=False)
    on_menu = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())




    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image_link': self.image_link,
            'category': self.category,
            'on_menu':self.on_menu,
            'created_on': self.created_on,
            'updated_on': self.updated_on
        }
