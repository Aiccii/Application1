from config import db


class Contact(db.Model):
    # this is the key we want to index for stuff
    id = db.Column(db.Integer, primary_key=True) # it must be unique

    # unique=False means that there can be multiple ppl with the same name
    # nullable=False means you cannot leave it empty, String(80) is 80 characters is the limit
    first_name = db.Column(db.String(80), unique=False, nullable=False)

    # unique=False means that there can be multiple ppl with the same name
    # nullable=False means you cannot leave it empty
    last_name = db.Column(db.String(80), unique=False, nullable=False)

    # unique=True means that there cannot be 2 emails with the same name
    email = db.Column(db.String(120), unique=True, nullable=False)

    # this function stores the above information in json so it can be used for saving and displaying
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
