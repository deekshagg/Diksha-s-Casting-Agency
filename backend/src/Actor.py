from flask import jsonify, request
from database.models import Actor


def select_actor():
    try:
        actors = Actor.query.all()
        actor_data = []
        for actor in actors:
            actor_data.append({
                'id': actor.id,
                'name': actor.name,
                'age': actor.age,
                'gender': actor.gender
            })
        response = {
            'success': True,
            'Actors': actor_data
        }
        return jsonify(response), 200

    except Exception as e:
        print(e)
        return jsonify(
            {'success': False, 'error': 'Failed to retrieve Actors'}), 500


def select_actor_detail(actor_id):
    try:
        actor = Actor.query.get(actor_id)

        if not actor:
            return jsonify(
                {'success': False, 'error': 'Actor Not Found'}), 404

        response = {
            'success': True,
            'id': actor.id,
            'name': actor.name,
            'age': actor.age,
            'gender': actor.gender
        }
        return jsonify(response), 200

    except Exception as e:
        print(e)
        return jsonify(
            {'success': False, 'error': 'Failed to retrieve Actor'}), 500


def insert_actor():
    try:
        data = request.json
        name = data['name']
        age = data['age']
        gender = data['gender']

        new_actor = Actor(name=name, age=age, gender=gender)

        Actor.insert(new_actor)

        response = {
            'success': True,
            'message': 'actor added successfully',
            'actor': new_actor.name
        }
        return jsonify(response), 201

    except Exception as e:
        print(e)
        return jsonify(
            {'success': False, 'error': 'Failed to add actor'}), 500


def patch_actor(actor_id):
    try:
        actor = Actor.query.get(actor_id)

        if not actor:
            return jsonify(
                {'success': False, 'error': 'Actor Not Found'}), 404

        update_data = request.json
        name = update_data['name']
        age = update_data['age']
        gender = update_data['gender']

        Actor.patch(actor, name, age, gender)

        response = {
            'success': True,
            'message': 'actor updated successfully',
            'actor': actor.name
        }
        return jsonify(response), 201

    except Exception as e:

        print(e)
        return jsonify(
            {'success': False, 'error': 'Failed to update actor'}), 500


def delete_actor(actor_id):

    try:
        actor = Actor.query.get(actor_id)

        if not actor:
            return jsonify(
                {'success': False, 'error': 'Actor Not Found'}), 404

        Actor.delete(actor)

        response = {
            'success': True,
            'message': 'Actor updated successfully',
            'actor': actor.name
        }
        return jsonify(response), 201

    except Exception as e:

        print(e)
        return jsonify(
            {'success': False, 'error': 'Failed to update actor'}), 500
