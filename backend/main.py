# CRUD app, CRUD : Create, Read, Update, Delete


# TODO create
# - first_name
# - last_name
# - email

from flask import request, jsonify
from config import app, db
from models import Contact


# this is called a decorator, we specify the route and the method we want to implement
@app.route("/contacts", methods=["GET"])
def get_contact():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts}), 200
#it uses flask sql alchemy to get all the contacts that are in the database


# this function creates a new contact
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    email = request.json.get('email')

    if not first_name or not last_name or not email :
        return (jsonify({"message": "You must include a first name and last name and a email address"}),
                400)

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact),
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "user created successfully!"}), 201


# this function edits the created contacts, it gets the id of the contact
@app.route('/update_contact/<int:user_id>', methods=['PATCH'])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.email = data.get('email', contact.email)

    db.session.commit()

    return jsonify({"message": "User updated"}), 200


# this function deletes the created contacts from the database
@app.route('/delete_contact', methods=['DELETE'])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "contact not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted"}), 200

# this is a checker function to make sure that if we import main it doesn't run everything
# but if we run main it imports everything and runs as wanted
if __name__ == '__main__':
    # this creates all the different models and rows that we have in the database
    with app.app_context():
        db.create_all()

    app.run(debug=True)


