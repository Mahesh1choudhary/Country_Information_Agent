from fastapi import APIRouter, Body, Response, HTTPException, Depends
from typing import Annotated

from app.commons.service_logger import setup_logger
from app.controller.dependency.dependency_functions import get_query_service
from app.service.query_service import QueryService
from app.commons.query_model import Query

query_router = APIRouter(prefix="/query")
logger = setup_logger()


@query_router.post(path="", status_code=200)
async def generate_query_response(query:Annotated[Query, Body()],
                            query_service: QueryService = Depends(get_query_service),):
    try:
        return await query_service.generate_query_response(query)
    except Exception as exc:
        logger.error(f"error in response generation: {exc}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
