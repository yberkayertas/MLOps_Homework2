import requests
import time

def test_container_health():
    """Smoke Test: Yayındaki konteynere gerçek bir HTTP isteği atar."""
    url = "http://localhost:8000/health"
    
    # Servisin hazır olması için deneme döngüsü
    for _ in range(5):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                assert response.json() == {"status": "healthy"}
                return
        except requests.exceptions.ConnectionError:
            time.sleep(2)
            
    assert False, "Service did not respond in time (Smoke Test Failed)"
    