import json
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.controller.query_controller import query_router
from app.data.data_loader import load_data_in_memory, unload_data_from_memory


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_data_in_memory()
    yield
    unload_data_from_memory()


def create_app() -> FastAPI:
    app = FastAPI(lifespan = lifespan)
    app.include_router(query_router)
    return app


def print_routes(app):
    print("Registered Routes:")
    for route in app.routes:
        print(f"Path: {getattr(route, 'path')}, Methods: {getattr(route, 'methods')}")

service_app = create_app()

# for local development only
if __name__ == "__main__":
    uvicorn.run(service_app, host="0.0.0.0", port=8000, reload=False)
