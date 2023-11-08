from fastapi.testclient import TestClient
from fastapi import status
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from app.main import app

client = TestClient(app)

"""_Unit Test EndPoint Property passed_
"""
def test_create_property():
    # Define test data
    property_data = {
        "id_property": 100,  # Provide unique property data for testing
        "name": "John Doe",
        "address": "Mz1 cs 12",
        "price": 200.0,
        "code_internal": "12-04-1992",
        "year": 2023,
        "id_owner": 1

        # Add other fields as required by your PropertyModel
    }

    # Make a POST request to the create_property route
    response = client.post("/property/", json=property_data)
    # validate status 422
    if response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY:
        assert response.json() == {"detail": "property not insert"}
    # Assert that the response status code is 201 (Created) for a successful creation
    assert response.status_code == status.HTTP_201_CREATED
    # Assert the response JSON matches the expected format (PropertyModel)
    assert response.json() == property_data

def test_create_property_existing_property():
    # Define test data for an property that already exists
    existing_property_data = {
        "id_property":1,
        "name":"prueba",
        "address":"prueba",
        "price":30000,
        "code_internal":"200",
        "year":2023,
        "id_owner":1
        # Add other fields as required by your PropertyModel
    }

    # Make a POST request to the create_property route with existing property data
    response = client.post("/property/", json=existing_property_data)

    # Assert that the response status code is 404 (Not Found) because property already exists
    assert response.status_code == 404

    # Assert the response contains the "Property already exists" message
    assert response.json() == {"detail": "Property already exists"}

def test_update_property_():
    # Define test data
    property_data = {
        "id_property": 100,  # Provide unique property data for testing
        "name": "John Doe",
        "address": "Mz1 cs 12",
        "price": 3000000.0,
        "code_internal": "A300",
        "year": 2024,
        "id_owner": 1

        # Add other fields as required by your PropertyModel
    }
    # Make a POST request to the create_property route
    response = client.put("/property/", json=property_data)
    if response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY:
        assert response.json() == {"detail": "property not update"}
    # Assert that the response status code is 201 (Created) for a successful creation
    assert response.status_code == status.HTTP_200_OK
    # Assert the response JSON matches the expected format (PropertyModel)
    assert response.json() == property_data

def test_get_property():
    """Function to get all properties
    """
    # Make a GET request to the /property/ route
    response = client.get("/property/")
    # Verify that the response has a status code of 200
    assert response.status_code == status.HTTP_200_OK
    # Verify that the response is a list
    data = response.json()
    assert isinstance(data, list)
    # Verify that the response contains at least one element
    assert len(data) > 0
    # Verify the structure of the elements in the list
    for item in data:
        assert "id_property" in item
        assert "name" in item
        assert "address" in item
        assert "price" in item
        assert "code_internal" in item
        assert "year" in item 
        assert "id_owner" in item

def test_get_property_by_id():
    """_function get only one property
    """
    property_id = 1  # Replace with a valid ID in your database
    response = client.get(f"/property/{property_id}")
    # Verify that the response has a status code of 200
    assert response.status_code == status.HTTP_200_OK
    # Replace with the actual data you expect in the response
    expected_data = {
        "id_property": 1,  # Provide unique property data for testing
        "name": "prueba",
        "address": "prueba",
        "price": 20000,
        "code_internal": "200",
        "year": 2023,
        "id_owner": 1
    }
    response_data = response.json()  # Get the JSON content of the response
    # Verify that the response is a non-empty list
    assert isinstance(response_data, list)
    assert len(response_data) == 1  # There should be a single owner in the list
    # Compare the first element in the list with the expected data
    assert response_data[0] == expected_data
