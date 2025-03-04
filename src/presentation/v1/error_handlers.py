from typing import cast

from fastapi import FastAPI, Request
from fastapi.responses import Response
from src.domain.common.exceptions import ApplicationException
from starlette.types import ExceptionHandler


async def application_exception_handler(request: Request, exc: ApplicationException) -> Response:
    return Response(content=exc.message, status_code=exc.status_code)


async def unknown_exception_handler(request: Request, exc: Exception) -> Response:
    return Response(content='Unknown error occured', status_code=500)


def init_exc_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ApplicationException, cast(ExceptionHandler, application_exception_handler))
    app.add_exception_handler(Exception, cast(ExceptionHandler, unknown_exception_handler))
