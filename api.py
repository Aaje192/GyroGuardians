from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    new_user["id"] = max(user["id"] for user in users) + 1 if users else 1
    users.append(new_user)
    return jsonify(new_user), 201

# Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.update(request.json)
    return jsonify(user)

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)
