from flask import Flask, jsonify, request
  
app = Flask(__name__)
  
  
@app.route('/hello', methods=['GET'])
def byeworld():
    if(request.method == 'GET'):
        data = {"data": "good bye"}
        return jsonify(data)
  
  
if __name__ == '__main__':
    app.run(debug=True)
