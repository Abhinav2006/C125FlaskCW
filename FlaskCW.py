from flask import Flask, jsonify, request
print("work")
print(__name__)
app = Flask(__name__)

task = [
    {
        'id': 1, 
        'title': "Playing",
        'description': 'Playing games with friends',
        'done': False
    },{
        'id': 2,
        'title': "Studying",
        'description': 'Studying at night',
        'done': True
    }
]

@app.route("/")
def helloWorld():
    return "hello world"

@app.route("/get-data")
def getTask():
    return jsonify({
        "data": task
    })

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the required data"
        }, 400)
    task2 = {
        'id': task[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    task.append(task2)
    return jsonify({
        "status": "success",
        "message": "task added successfully"
    })
    
if(__name__ == "__main__"):
    app.run(debug = True)