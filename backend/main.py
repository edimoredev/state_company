from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import propertyImage_route, property_route, owner_route

# Create an instance of the FastAPI application
app = FastAPI()

# Define settings to allow requests from any origin
origins = ["*"]

# Add middleware to enable Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Allow requests from origins specified in 'origins'
    allow_credentials=True,     # Allow including credentials in requests (e.g., cookies)
    allow_methods=["*"],        # Allow any HTTP method (GET, POST, etc.)
    allow_headers=["*"],        # Allow any headers in requests
)

# includes the defined routers
app.include_router(owner_route.ownerRouter)   # Include routes related to owners
app.include_router(property_route.propertyRouter)  # Include routes related to properties
app.include_router(propertyImage_route.propertyImageRouter)# Include routes related to propertyImage

