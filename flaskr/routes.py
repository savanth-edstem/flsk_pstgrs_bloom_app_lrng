from flask import request, jsonify, abort, Blueprint
from flaskr.extensions import db
from flaskr.modals import UserModel

main = Blueprint('main', __name__)


@main.route('/')
def hello():
    return "Hello World"


@main.route('/user', methods=['POST'])
def add_details_of_user():
    if (
            not request.json
    ):
        abort(400)
    body = request.json
    new_user = UserModel(name=body['name'], email=body['email'], edstem_id=body['edstem_id'])
    db.session.add(new_user)
    db.session.commit()
    return "success"


@main.route('/user', methods=['GET'])
def details_of_user():
    all_users = UserModel.query.all()
    results = [{"name": user.name,
                "email": user.email,
                "edstem_id": user.edstem_id
                } for user in all_users]

    return jsonify(results)


@main.route('/user/<user_id>', methods=['GET'])
def single_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    response = {"name": user.name,
                "email": user.email,
                "edstem_id": user.edstem_id}
    return jsonify(response)


@main.route('/user/<user_id>', methods=['POST'])
def update_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    body = request.json
    user.name = body['name']
    user.email = body['email']
    user.edstem_id = body['edstem_id']
    db.session.add(user)
    db.session.commit()
    return "successfully updated"


@main.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return "successfully deleted"
