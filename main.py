from flask import Flask, abort, jsonify, render_template
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/text_simi")
def text_simi():
    agenda = []
 
    filepath = "data/agenda.csv"
    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            agenda.append(line.split(',', 2))

    return render_template("text_simi.html", test=agenda)

@app.route("/api/get_user/<user>")
def getUser (user):
    
    agenda = []
    filepath = "data/agenda.csv"
    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            agenda.append(line.split(',', 2))

    for contact in agenda:
        if user == contact[0]:
            return jsonify(name=contact[0], number=contact[1])
        

    return jsonify(user=user, error="User not found."), 404



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
