from flask import Flask, jsonify

app = Flask(__name__)

values =[
    {
        "id": 1,
        "name": "Roberto"
    },
    {
        "id": 2,
        "name": "Rafael"
    }
]
@app.post("/")
def hello_world():
    return "Hello, World!"

@app.route("/")
def hello():
    return "<h1>Olá Mundo</h1>"

@app.get("/<int:id>/")
def get_one(id):
    for item in values:
        if item["id"] == id:
            return jsonify(item)
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)