from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import property_route

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(property_route.propertyRouter)
# app.include_router(typeTransactions.typeTransactionRouter)
# app.include_router(accounts.accountRouter)
# app.include_router(transactions.transactionRouter)
