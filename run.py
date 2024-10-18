import subprocess
import os
import time
import webbrowser

def run_flask():
    # Change directory to the Flask backend and run the Flask app
    os.chdir('python-backend')  # Adjust the path if necessary
    subprocess.run(['python', 'app.py'])

def run_node():
    # Change directory to the Node.js backend and run the Node.js server
    os.chdir('chatbot-backend')  # Adjust the path if necessary
    subprocess.run(['node', 'server.js'])

if __name__ == '__main__':
    # Start Flask app in a separate process
    flask_process = subprocess.Popen(['python', 'app.py'], cwd='python-backend')

    # Give Flask some time to start
    time.sleep(2)

    # Start Node.js server in a separate process
    node_process = subprocess.Popen(['node', 'server.js'], cwd='chatbot-backend')

    # Open the index.html file in the default web browser
    webbrowser.open('http://localhost:5000/index.html')

    try:
        # Wait for both processes to complete
        flask_process.wait()
        node_process.wait()
    except KeyboardInterrupt:
        # If interrupted, terminate both processes
        flask_process.terminate()
        node_process.terminate()
