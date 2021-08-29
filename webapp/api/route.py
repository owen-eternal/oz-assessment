import os
from flask import Blueprint
from flask import current_app
from flasgger import swag_from
from flask.json import jsonify, request
from sorting.bubble_sort import BubbleSort

sorting = Blueprint('sorting', __name__)

# instantiate the sort algorithm
sort = BubbleSort()
doc = os.getcwd() + "/webapp/swagger_docs/docs.yml"


# check if the list is empty
def isEmpty(array):
    if not array:
        return True


# sorting api
@sorting.route('/api/v1/bubble', methods=['POST'])
@swag_from(doc)
def bubble_sort():
    try:
        unsorted_list = request.get_json()['unsorted-list']
        if isEmpty(unsorted_list):
            return jsonify({'message': 'Must not be empty'}), 401
        else:
            sorted_list = sort.bubble_sort(unsorted_list, int(current_app.config['MAXIMUM_LENGTH']))
        return jsonify({'sorted-list': sorted_list}), 201
    except Exception:
        return jsonify(
            {
                'error': 'ValueError',
                'message': 'Elements in list must be less then Max Length'
            }), 401
