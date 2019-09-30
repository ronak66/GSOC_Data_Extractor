from gsoc_extractor import db
from datetime import datetime

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    technology = db.Column(db.String, default = "")
    year = db.Column(db.String)
    created_on = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)

    def __repr__(self):
        return "id: {}, technology: {}, year: {}, created_on: {}".format(self.id, \
            self.technology, self.year, self.created_on )