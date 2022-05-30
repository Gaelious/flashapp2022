from flask import Flask, abort, jsonify, render_template
import json
from Contact import Contact

app = Flask(__name__)


def readAgenda() -> list[Contact]:
    agenda = []

    filepath = "data/agenda.csv"
    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            if (line):
                contact_info = line.split(',')    # ["Name","Phone Number","date","genre"]
                usuario = Contact(contact_info[0], contact_info[1], contact_info[2],contact_info[3])
                agenda.append(usuario)
                
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
        if user == contact.name:
            return json.dumps(contact, default=lambda x : x.__dict__)
        
    return jsonify(user=user, error="User not found."), 404

@app.route("/api/get_adults")
def getAdults():
    adults = []

    for contact in agenda:
        if contact.isAdult():
            adults.append()    

    return json.dumps(adults, default=lambda x : x.__dict__)
    
        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
