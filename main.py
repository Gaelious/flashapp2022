from flask import Flask, render_template
import re
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/text_simi")
def text_simi():
    f = open("data/agenda.csv", 'r')
    agenda = []
    '''agenda2 = []
    for i in range(len(agenda)):
        if (agenda[i] != ","):
            agenda2[j] += agenda[i]'''
 
    filepath = "data/agenda.csv"
    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            contact = line.split(',', 2)
            print(contact)
            agenda.append(line.split(',', 2))
    #agenda = re.sub(r'(<)', '', agenda)
    return render_template("text_simi.html", test=agenda)
 
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
