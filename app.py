from flask_cors import CORS
from flask import Flask, jsonify, request
import base64
import os
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)
stats = []

@app.route("/")
def helloWorld():
    """
    Root route 
    
    Returns:
        String -- Return a valid string
    """
    return "Hello, cross-origin-world!"

@app.route('/ping', methods=['GET'])
def pingPong():
    """
    Ping route for sanity check
    
    Returns:
        JSON Dictionary -- Return a valid key value pair
    """
    return jsonify({'data': 'pong!'})

@app.route('/upload', methods=['POST'])
def uploadFile():
    """
    REST API endpoint for image inference
    
    Returns:
        JSON Dictionary -- Return a dictionary containing image in base64 format and statistics of the counts and classification of rotifers
    """
    file = request.files['file']
    file.save("./test.jpg")
    os.system("python3 social-distancing.py --image enabled --video disabled --image_in ./test.jpg --image_out ./output.jpg --horizontal_ratio 0.7 --vertical_ratio 0.7 --openpose_folder /openpose/models/")
    with open("output.jpg","rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        base64_string = encoded_string.decode('utf-8')
    return jsonify(img=base64_string)



if __name__ == '__main__':
   # predict()  
   app.run(host='0.0.0.0', port=8888)
