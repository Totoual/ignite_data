import asyncio
import os
from contextlib import asynccontextmanager
import logging
import uvicorn
import uvloop
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from assessment.config.fastapi import FastApiConfig
from assessment.models.sessionmaker import sessionmanager
from assessment.routes import medication_request

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: F811
    sessionmanager.init(host=FastApiConfig.SQLALCHEMY_DATABASE_URI)
    yield
    if sessionmanager.engine is not None:
        await sessionmanager.close()


def init_app():

    app = FastAPI(
        title="IgniteData Assessment",
        lifespan=lifespan,
    )

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    configure_routes(app)

    return app


def configure_routes(app: FastAPI):
    app.include_router(medication_request.router, tags=["Medication Request"])


def main():
    uvloop.install()
    app = init_app()
    PORT = int(os.getenv("UVICORN_PORT", 8000))
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT)


if __name__ == "__main__":
    main()
else:
    app = init_app()
