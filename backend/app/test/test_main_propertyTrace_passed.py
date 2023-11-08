from fastapi.testclient import TestClient
from fastapi import status
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from app.main import app

client = TestClient(app)

"""_Unit Test EndPoint Owner passed_
"""
def test_create_propertyTrace():
    # Define test data
    propertyTrace_data = {
        "id_property_trace": 100, # Provide unique propertyTrace data for testing
        "date_sale": "2-11-2023",
        "name": "test_100",
        "value": 100,
        "tax": 1.1,
        "id_property": 1,
        # Add other fields as required by your PropertyTraceModel
    }

    # Make a POST request to the create_owner route
    response = client.post("/propertyTrace/", json=propertyTrace_data)

    if response.status_code == status.HTTP_404_NOT_FOUND:
        assert response.json() == {"detail": "Property does not exists"}
    else:
        # Assert that the response status code is 201 (Created) for a successful creation
        assert response.status_code == status.HTTP_201_CREATED

        # Assert the response JSON matches the expected format (PropertyTraceModel)
        assert response.json() == propertyTrace_data

def test_create_propertyTrace_existing_propertyTrace():
    # Define test data for an propertyTrace that already exists
    existing_propertyTrace_data = {
        "id_property_trace": 1,
        "date_sale": "2-11-2023",
        "name": "trace1",
        "value": 500,
        "tax": 1.1,
        "id_property": 1,
        # Add other fields as required by your PropertyTraceModel
    }

    # Make a POST request to the create_propertyTrace route with existing propertyTrace data
    response = client.post("/propertyTrace/", json=existing_propertyTrace_data)

    # Assert that the response status code is 404 (Not Found) because propertyTrace already exists
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Assert the response contains the "propertyTrace already exists" message
    assert response.json() == {"detail": "PropertyTrace already exists"}

def test_get_propertyTrace():
    """Function to get all propertyTrace
    """
    # Make a GET request to the /propertyTrace/ route
    response = client.get("/propertyTrace/")
    # Verify that the response has a status code of 200
    assert response.status_code == status.HTTP_200_OK
    # Verify that the response is a list
    data = response.json()
    assert isinstance(data, list)
    # Verify that the response contains at least one element
    assert len(data) > 0
    # Verify the structure of the elements in the list
    for item in data:
        assert "id_property_trace" in item
        assert "date_sale" in item
        assert "name" in item
        assert "value" in item
        assert "tax" in item
        assert "id_property" in item

def test_get_propertyTrace_by_id():
    """_function get only one propertyTrace
    """
    id_property_trace = 1  # Replace with a valid ID in your database
    response = client.get(f"/propertyTrace/{id_property_trace}")
    # Verify that the response has a status code of 200
    assert response.status_code == status.HTTP_200_OK
    # Replace with the actual data you expect in the response
    expected_data = {
        "id_property_trace": 1,
        "date_sale": "2-11-2023",
        "name": "trace1",
        "value": 500,
        "tax": 1.1,
        "id_property": 1,
    }
    response_data = response.json()  # Get the JSON content of the response
    # Verify that the response is a non-empty list
    assert isinstance(response_data, list)
    assert len(response_data) == 1  # There should be a single owner in the list
    # Compare the first element in the list with the expected data
    assert response_data[0] == expected_data

