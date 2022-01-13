from calculateArces import acres 
from flask import Flask, jsonify, request

#instantiate flask object 
    
"""
    A function to get request using flask
    evaluate and return result
    """
      
#app
app = Flask('__name__')

@app.route('/', methods=['GET', 'POST'])
def get_input():
    
    packet = request.get_json(force=True)
    print(packet)
    length = packet['length']
    width = packet['width']

    acres_ = acres(length, width)

    return {"Acres":acres_}

#driver function 

if __name__ == "__main__":
  app.run(debug=True)
    


