import json
from fastapi.testclient import TestClient

from app.main import app 

client = TestClient(app)


def test_read_if_no_value_main():
    response = client.get("/", json={'detail': [{'loc': ['query', 'height'], 'msg': 'field required', 'type': 'value_error.missing'}, {'loc': ['query', 'weight'], 'msg': 'field required', 'type': 'value_error.missing'}]})
    assert response.status_code == 422
    assert response.json() == {
        'detail': [{'loc': ['query', 'height'], 
        'msg': 'field required', 'type': 'value_error.missing'}, 
        {'loc': ['query', 'weight'], 
        'msg': 'field required', 'type': 
        'value_error.missing'}]}

def test_read_if_string_input_main():
    response = client.get("/?height=test&weight=test", json={'detail': [{'loc': ['query', 'height'], 'msg': 'value is not a valid float', 'type': 'type_error.float'}, {'loc': ['query', 'weight'], 'msg': 'value is not a valid float', 'type': 'type_error.float'}]})
    assert response.status_code == 422
    assert response.json() == {
        'detail': [{'loc': ['query', 'height'], 
        'msg': 'value is not a valid float', 
        'type': 'type_error.float'}, 
        {'loc': ['query', 'weight'], 
        'msg': 'value is not a valid float', 
        'type': 'type_error.float'}]}