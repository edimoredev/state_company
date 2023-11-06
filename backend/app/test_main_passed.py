from fastapi.testclient import TestClient
from fastapi import status, HTTPException

from main import app

client = TestClient(app)

"""_Unit Test EndPoint Owner passed_
"""
def test_create_owner():
    # Define test data
    owner_data = {
        "id_owner": 6,  # Provide unique owner data for testing
        "name": "John Doe",
        "address": "Mz1 cs 12",
        "photo": "2",
        "birthday": "12-04-1992"
        # Add other fields as required by your OwnerModel
    }

    # Make a POST request to the create_owner route
    response = client.post("/owner/", json=owner_data)

    # Assert that the response status code is 201 (Created) for a successful creation
    assert response.status_code == status.HTTP_201_CREATED

    # Assert the response JSON matches the expected format (OwnerModel)
    assert response.json() == owner_data

def test_create_owner_existing_owner():
    # Define test data for an owner that already exists
    existing_owner_data = {
        "id_owner": 1,
        "name": "Edison Monreno Capera",
        "address": "Mz1 cs 12",
        "photo": "2",
        "birthday": "12-04-1992"
        # Add other fields as required by your OwnerModel
    }

    # Make a POST request to the create_owner route with existing owner data
    response = client.post("/owner/", json=existing_owner_data)

    # Assert that the response status code is 404 (Not Found) because owner already exists
    assert response.status_code == 404

    # Assert the response contains the "Owner already exists" message
    assert response.json() == {"detail": "Owner already exists"}

def test_get_owner():
    """_function get all owners
    """
    # Realiza una solicitud GET a la ruta /owner/
    response = client.get("/owner/")
    # Verifica que la respuesta tenga el código de estado 200
    assert response.status_code == status.HTTP_200_OK
    # Verifica que la respuesta sea una lista
    data = response.json()
    assert isinstance(data, list)
    # Verifica que la respuesta contenga al menos un elemento
    assert len(data) > 0
    # Verifica la estructura de los elementos en la lista
    for item in data:
        assert "id_owner" in item
        assert "name" in item
        assert "address" in item
        assert "photo" in item
        assert "birthday" in item

def test_get_owner_by_id():
    """_function get only one owner
    """
    owner_id = 1  # Replace with a valid ID in your database
    response = client.get(f"/owner/{owner_id}")
    # Verify that the response has a status code of 200
    assert response.status_code == status.HTTP_200_OK
    # Replace with the actual data you expect in the response
    expected_data = {
        "id_owner": 1,
        "name": "Edison Monreno Capera",
        "address": "Mz1 cs 12",
        "photo": "2",
        "birthday": "12-04-1992"
    }
    response_data = response.json()  # Get the JSON content of the response
    # Verify that the response is a non-empty list
    assert isinstance(response_data, list)
    assert len(response_data) == 1  # There should be a single owner in the list
    # Compare the first element in the list with the expected data
    assert response_data[0] == expected_data

