import os
import sys
from pathlib import Path
import threading
import time
import requests
import webview

# Django server URL
DJANGO_URL = "http://127.0.0.1:8000"

def resource_path(relative_path):
    """Get the absolute path to the resource, handling PyInstaller environment."""
    if getattr(sys, 'frozen', False):  # If running as a PyInstaller bundle
        base_path = sys._MEIPASS  # Temporary directory where PyInstaller extracts files
    else:
        base_path = Path(__file__).parent
    return os.path.join(base_path, relative_path)

def start_django_server():
    """Start the Django development server."""
    # Locate the Django project directory dynamically
    project_dir = resource_path("marg")
    os.chdir(project_dir)
    
    # Run migrations and start the Django server
    os.system("python manage.py migrate")
    os.system("python manage.py runserver")

def wait_for_server(url, timeout=30):
    """Wait for the server to become available."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.ConnectionError:
            pass
        time.sleep(1)  # Wait 1 second before retrying
    return False

if __name__ == "__main__":
    # Start the Django server in a separate thread
    server_thread = threading.Thread(target=start_django_server)
    server_thread.daemon = True
    server_thread.start()

    # Wait for the server to start
    if wait_for_server(DJANGO_URL):
        # Open the webview window once the server is ready
        webview.create_window("GRMARG", DJANGO_URL)
        webview.start()
    else:
        print("Django server did not start within the timeout period.")
