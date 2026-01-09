from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction_integration():
    test_input = "high_cardinality_user_99"
    response = client.get(f"/predict?input_string={test_input}")
    
    assert response.status_code == 200
    data = response.json()
    assert "hash_index" in data
    assert isinstance(data["hash_index"], int)
    