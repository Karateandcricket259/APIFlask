from flask import Flask,request,jsonify
app=Flask(__name__)
contacts=[
    {
     "id":"1",
     "Contact":"2247729078",
     "Name":"Eashan",
     "done":False
    },
    {
      "id":"2",
      "Contact":"8476982017",
      "Name":"Bob",
      "done":False
    }
]
@app.route("/add-data",methods=["POST"])
def addcontact():
    if not request.json:
        return jsonify({
           "status":"error",
           "message":"Please provide the contacts"
        },400)
    contact={
        'id':contacts[-1]['id']+1,
        'Contact':request.json['Contact'],
        'Name':request.json.get['Name',""],
        'done':False
    }
    contacts.append(contact)
    return jsonify({
        "status":"successful",
        "message":"contact added successfully"
    })
@app.route("/get-data")
def getcontact():
    return jsonify({
        'data':contacts
    })
 
if(__name__=="__main__"):
    app.run(debug=True)
