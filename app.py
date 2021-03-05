from fastapi import FastAPI
from helpers.bluedart import fetch_details_from_bludart
app = FastAPI()


@app.get("/bluedart/{id}")
async def bluedart(id):
    status = fetch_details_from_bludart(id)
    return {"status": status}