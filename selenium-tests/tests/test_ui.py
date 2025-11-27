import requests
import time

BASE = 'http://web:5000'

def test_index_available():
    """Test Case 1: Verify homepage is accessible"""
    print("Running Test Case 1: Homepage availability")
    max_retries = 5
    for i in range(max_retries):
        try:
            r = requests.get(f'{BASE}/', timeout=5)
            assert r.status_code == 200
            assert 'Simple Flask app' in r.text
            print("✓ Test Case 1 PASSED: Homepage is accessible")
            return
        except requests.exceptions.RequestException as e:
            if i < max_retries - 1:
                print(f"Retry {i+1}/{max_retries}: Waiting for app to start...")
                time.sleep(2)
            else:
                raise

def test_create_and_list_message():
    """Test Case 2: Verify message creation and retrieval"""
    print("\nRunning Test Case 2: Message creation and retrieval")
    
    # Create a message
    r = requests.post(f'{BASE}/messages', json={'text': 'selenium test message'})
    assert r.status_code == 201
    data = r.json()
    assert 'id' in data
    assert data['text'] == 'selenium test message'
    print("✓ Message created successfully")

    # List messages
    r2 = requests.get(f'{BASE}/messages')
    assert r2.status_code == 200
    messages = r2.json()
    found = any(m['text'] == 'selenium test message' for m in messages)
    assert found
    print("✓ Test Case 2 PASSED: Message found in list")