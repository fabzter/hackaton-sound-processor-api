from flask import Flask

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/api/task', methods=['GET'])
def get_tasks():
            
    return "lots of gets"

@app.route('/api/task', methods=['POST'])
def create_task():
        
    task = {
        'id': 1,
        'title': 'task 1',
        'description': 'description 11',
        'done': False
    }
    
    return task, 201



if __name__ == '__main__':
    app.run(port=5000)

