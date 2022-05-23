from flask import Flask, abort, jsonify, render_template
 
app = Flask(__name__)

def readAgenda():
    agenda = []

    filepath = "data/agenda.csv"
    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            if (line):
                agenda.append(line.split(',',4))

    return agenda

agenda = readAgenda()



@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/text_simi")
def text_simi():
    return render_template("text_simi.html", test=agenda)

@app.route("/api/get_user/<user>")
def getUser (user):
    for contact in agenda:
        if user == contact[0]:
            return jsonify(name=contact[0], number=contact[1], birth=contact[2], gender=contact[3])
        

    return jsonify(user=user, error="User not found."), 404

@app.route("/api/get_adults")
def getAdult():

    adults = []

    for contact in agenda:
        year = int(contact[2][:4])
        
        if year < 2004:
            adults.append([contact[0], contact[2]])
    
    return jsonify(adults)
    
            

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
