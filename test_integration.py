import subprocess
import time
from client import TranslationClient

def start_server():
    return subprocess.Popen(["python", "server.py"])

def integration_test():
    server_process = start_server()
    time.sleep(2)

    client = TranslationClient("http://localhost:5000")
    status = client.get_status()
    print("Final Translation Status:", status)

    server_process.terminate()

if __name__ == "__main__":
    integration_test()
