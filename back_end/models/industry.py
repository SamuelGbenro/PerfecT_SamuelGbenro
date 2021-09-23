from db import db

class IndustryModel(db.Model):
    __tablename__ = 'industry'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    contact = db.Column(db.String(80))
    website = db.Column(db.String(80))
    facebook = db.Column(db.String(80))
    twitter = db.Column(db.String(80))
    instagram = db.Column(db.String(80))
    postalAddress = db.Column(db.String(80))
    streetAddress = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    callCentre = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name, contact, website, facebook, twitter, instagram, postalAddress, streetAddress, phone, callCentre):
        self.name = name
        self.contact = contact
        self.website = website
        self.facebook = facebook
        self.twitter = twitter
        self.instagram = instagram
        self.postalAddress = postalAddress
        self.streetAddress = streetAddress
        self.phone = phone
        self.callCentre = callCentre

     # def json(self):
     #     return {'name': self.name, 'items': [self.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
       return cls.query.filter_by(name=name).first()

    def save_to_db(self):
       db.session.add(self)
       db.session.commit()


    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()

