# MLOps for AI Engineers and Data Scientists

# Omdena_MLOps-assignment2


## Flask API

Flask is a widely used micro web framework for creating APIs in Python. 
It is a simple yet powerful web framework which is designed to get started quick and easy, with the ability to scale up to complex applications.

```python:

pip install Flask
```

### Mininmal Flask App

```python:
from flask import Flask
app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
```

Save this file as app.py (or any other filename you want) and go to terminal and type python app.py

You should see something like this:

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

The code line-by-line:

from flask import Flask → Import the Flask class

app = Flask(__name__) → Create an instance of the class

@app.route('/hello/', methods=['GET', 'POST']) → We use the route() decorator to tell Flask what URL should trigger the function.
methods specify which HTTP methods are allowed. The default is ['GET']

if __name__ == '__main__' → __name__ is a special variable in Python which takes the value of the script name. 
This line ensures that our Flask app runs only when it is executed in the main file and not when it is imported in some other file
app.run(host='127.0.0.1', port=5000) → Run the Flask application
host specifies the server on which we want our flask application to run. The default value for host is localhost or 127.0.0.1
