from fastapi.testclient import TestClient
from fastapi import status
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from app.main import app

client = TestClient(app)

"""_Unit Test EndPoint PropertyImage passed_
"""

# def test_create_propertyImage():
#     # Define los datos de prueba
#     propertyImage_data = {
#         "id_property_image": 100,
#         "enable": True,
#         "id_property": 100,
#     }
    

#     # Abre el archivo de prueba para cargar
#     with open(os.getcwd() + "\\test_img.jpg", "rb") as file:
#         # Realiza una solicitud POST con los datos y el archivo
#         response = client.post(
#             "/propertyImage/",
#             data=propertyImage_data,
#             files={"image": ("test_img.jpg", file, "image/jpeg")},
#         )
    
#     # Verifica el código de respuesta y los datos de respuesta
#     assert response.status_code == 201  # El código de estado 201 indica éxito en la creación
#     response_data = response.json()
#     # Puedes agregar más aserciones para verificar los datos de respuesta según tu modelo de salida
#     assert "id_property_image" in response_data
#     assert response_data["id_property_image"] == 100

# def test_create_propertyImage():
#     # Define el modelo PropertyImageModel
#     propertyImage_data = {
#         "id_property_image": 100,
#         "enable": True,
#         "id_property": 100,
#     }

#     # Define la ruta al archivo de prueba
#     file_path = os.path.join(os.path.dirname(__file__), "test_img.jpg")

#     # Abre el archivo de prueba para cargar
#     with open(file_path, "rb") as file:
#         # Realiza una solicitud POST con el modelo y el archivo
#         files = {
#             "image": ("test_img.jpg", file, "image/jpeg"),
#         }
#         response = client.post("/propertyImage/", files=files, data=propertyImage_data)

#     # Verifica el código de respuesta y los datos de respuesta
#     assert response.status_code == 200
#     response_data = response.json()
#     assert "propertyImage" in response_data
#     assert response_data["propertyImage"] == propertyImage_data
#     assert "filename" in response_data
#     assert response_data["filename"] == "test_img.jpg"

# def test_create_propertyImage():
#     # Ruta de la imagen de prueba
#     ruta = os.getcwd()+ "\\test_image.jpg"
    
#     # Abre el archivo en modo binario y lee su contenido
#     with open(ruta, "rb") as image_file:
#         image_data = image_file.read()

#     # Define los datos de prueba para el modelo PropertyImageModel
#     propertyImage_data = {
#         "id_property_image": 100,  # Proporciona un valor único para id_property_image
#         "enable": True,
#         "id_property": 1,
#     }
    
#     # Define los archivos adjuntos, en este caso, la imagen
#     files = {"image": ("test_image.jpg", image_data, "image/jpeg")}
    
#     # Realiza una solicitud POST para crear una nueva propiedad de imagen
#     response = client.post(
#         "/propertyImage/",
#         data=propertyImage_data,
#         files=files
#     )

#     if response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY:
#         assert response.json() == {"detail": "No se insertaron datos"}
#     else:
#         # Valida que el código de estado sea 201 (Created) para una creación exitosa
#         assert response.status_code == 201

#         # Valida que la respuesta JSON coincida con los datos de propiedad de imagen enviados
#         assert response.json() == propertyImage_data

# def test_get_propertyImage():
#     """Function to get all propertiesImage
#     """
#     # Make a GET request to the /propertyImage/ route
#     response = client.get("/propertyImage/")
#     # Verify that the response has a status code of 200
#     assert response.status_code == status.HTTP_200_OK
#     # Verify that the response is a list
#     data = response.json()
#     assert isinstance(data, list)
#     # Verify that the response contains at least one element
#     assert len(data) > 0
#     # Verify the structure of the elements in the list
#     for item in data:
#         assert "id_property_image" in item
#         assert "enable" in item
#         assert "id_property" in item
#         assert "file_name" in item

# def test_get_propertyImage_by_id():
#     """_function get only one propertyImage
#     """
#     id_property_image = 1  # Replace with a valid ID in your database
#     response = client.get(f"/propertyImage/{id_property_image}")
#     # Verify that the response has a status code of 200
#     assert response.status_code == status.HTTP_200_OK
#     # Replace with the actual data you expect in the response
#     expected_data = {
#         "id_property_image": 1,  # Provide unique propertyImage data for testing
#         "enable": True,
#         "id_property": 1,
#         "file_name": "word.png"
#     }
#     response_data = response.json()  # Get the JSON content of the response
#     # Verify that the response is a non-empty list
#     assert isinstance(response_data, list)
#     assert len(response_data) == 1  # There should be a single owner in the list
#     # Compare the first element in the list with the expected data
#     assert response_data[0] == expected_data
