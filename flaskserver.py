import os
from flask import Flask
from flask import request
result="" 
app = Flask(__name__)
 
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    global result
    #print (request.is_json)
    content = request.get_json()
    #print (content)
    #print ("true")
    #print (content["encode"])
    #print (content["aaa"])
    result=(content["aaa"])
    os.chdir("/home/ec2-user/sdpd")
    with open("image.jpg", "wb") as fh:
    	fh.write(content["encode"].decode('base64'))
    	
    return 'JSON posted'

@app.route('/getjson')
def getJsonHandler():
    global result
    print result
    if (result == "tomato"):
    	os.chdir("/home/ec2-user/sdpd/tomato")
    	os.system("python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=/home/ec2-user/sdpd/image.jpg > a.txt")
    elif (result == "potato"):
    	os.chdir("/home/ec2-user/sdpd/tensor")
    	os.system("python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=/home/ec2-user/sdpd/image.jpg > a.txt")
    elif (result == "corn"):
        os.chdir("/home/ec2-user/sdpd/corn")
        os.system("python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=/home/ec2-user/sdpd/image.jpg > a.txt")
    elif (result == "grape"):
        os.chdir("/home/ec2-user/sdpd/grape")
        os.system("python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=/home/ec2-user/sdpd/image.jpg > a.txt")

    file = open("a.txt", "r") 
    aa=""
    for i in file.readline():
       if (i.isdigit()):
         break
       aa= aa+i
    baa = aa.replace(" ","")
    os.chdir("/home/ec2-user/sdpd")
    file1 = open(baa + ".txt","r")
    aa = aa + " \n \n \n \n" + file1.read()
    return aa 
    #return 'string posted'    
    
 
app.run(host='ec2-13-127-4-47.ap-south-1.compute.amazonaws.com', port= 8090)
