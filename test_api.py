import requests
import json

def test_api():
    url = "http://localhost:8080/analyze"
    headers = {"Content-Type": "application/json"}
    data = {"message": "I am feeling happy today"}
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api() 