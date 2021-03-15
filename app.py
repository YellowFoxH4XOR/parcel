from fastapi import FastAPI, Query
from helpers.bluedart import fetch_details_from_bludart
from helpers.dtdc import fetch_details_from_dtdc
app = FastAPI()


@app.get("/bluedart/{id}")
async def bluedart(id):
    status = fetch_details_from_bludart(id)
    return {"status": status}


@app.get("/dtdc/")
async def dtdc(
    id: str,
    type_: str = Query("AWB/Consignment Number",
    enum=["AWB/Consignment Number", "Reference Number"])
):
    status = fetch_details_from_dtdc(id, type_)
    return {"status": status}