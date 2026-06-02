from flask import Flask, request, jsonify
from pymongo import MongoClient
import bcrypt
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = 'mysecretkey'

# MongoDB Connection
client = MongoClient(
    'mongodb+srv://Bandaru:anji1234@cluster0.ab7xbzy.mongodb.net/?appName=Cluster0'
)

db = client["jwt"]
user_collection = db["users"]


@app.route('/')
def home():
    return "hello"


# =========================
# AUTH MIDDLEWARE
# =========================
def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        # Get token from headers
        if 'Authorization' in request.headers:

            bearer = request.headers['Authorization']

            # Remove Bearer word
            token = bearer.split(" ")[1]

        # Token missing
        if not token:
            return jsonify({
                "message": "Token is missing"
            }), 401

        try:

            # Decode token
            data = jwt.decode(
                token,
                app.config['SECRET_KEY'],
                algorithms=["HS256"]
            )

            # Find user
            current_user = user_collection.find_one({
                "email": data['email']
            })

            if not current_user:
                return jsonify({
                    "message": "User not found"
                }), 401

        except jwt.ExpiredSignatureError:
            return jsonify({
                "message": "Token expired"
            }), 401

        except jwt.InvalidTokenError:
            return jsonify({
                "message": "Invalid token"
            }), 401

        return f(current_user, *args, **kwargs)

    return decorated


# =========================
# SIGNUP API
# =========================
@app.route('/signup', methods=["POST"])
def signup():

    data = request.get_json()

    email = data.get("email")

    existing_user = user_collection.find_one({
        "email": email
    })

    if existing_user:
        return jsonify({
            "message": "Already registered"
        }), 400

    hashed_pass = bcrypt.hashpw(
        data.get("password").encode('utf-8'),
        bcrypt.gensalt()
    )

    new_user = {
        "name": data.get("name"),
        "email": data.get("email"),
        "password": hashed_pass
    }

    user_collection.insert_one(new_user)

    return jsonify({
        "message": "User registered successfully"
    }), 201


# =========================
# LOGIN API
# =========================
@app.route('/login', methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = user_collection.find_one({
        "email": email
    })

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    # Password check
    if bcrypt.checkpw(
        password.encode('utf-8'),
        user["password"]
    ):

        # Create JWT Token
        token = jwt.encode(
            {
                "email": user["email"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            },
            app.config['SECRET_KEY'],
            algorithm="HS256"
        )

        return jsonify({
            "message": "Login successful",
            "token": token
        }), 200

    else:
        return jsonify({
            "message": "Invalid password"
        }), 401


# =========================
# PROTECTED ROUTE
# =========================
@app.route('/profile', methods=["GET"])
@token_required
def profile(current_user):

    return jsonify({
        "message": "Protected route accessed",
        "user": {
            "name": current_user["name"],
            "email": current_user["email"]
        }
    })


if __name__ == "__main__":
    app.run(debug=True)