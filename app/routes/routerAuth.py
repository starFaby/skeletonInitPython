from flask import Blueprint
from app.auth.auth import Auth
auth= Blueprint('auth', __name__)
auth.route('/auth', methods=['GET'])(Auth.onGetAuth)
auth.route('/createauth', methods=['POST'])(Auth.onGetCreateAuth)
auth.route('/listauth', methods=['GET'])(Auth.onGetListAuth)
# user_bp.route('/<int:user_id>/edit', methods=['PUT'])(update)
# user_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)
