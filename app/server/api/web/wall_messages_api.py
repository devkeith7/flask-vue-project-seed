
from flask import Blueprint, jsonify

from service.wall_messages import WallMessages
web_wall_messages_api = Blueprint('web_wall_messages_api', __name__)


@web_wall_messages_api.route('/get-all', methods=['GET'])
def get_all():
	"""
	Get all wall messages.

	"""

	wms = WallMessages.get_all()
	response = [ wm.to_dict() for wm in wms ]
	return jsonify(response)


@web_wall_messages_api.route('/add-message', methods=['POST'])
def add_message():
	"""
	Add a wall message.

	"""

	message_body = str(request.form['body'])
	message_attribution = str(request.form['attribution'])
	wm = WallMessages.add_message(
		message_body=message_body,
		message_attribution=message_attribution
	)
	return jsonify(wm)
