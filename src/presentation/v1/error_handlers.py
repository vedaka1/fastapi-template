from typing import cast

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from starlette.types import ExceptionHandler

from src.domain.common.exceptions import ApplicationException


async def application_exception_handler(request: Request, exc: ApplicationException) -> JSONResponse:
    return JSONResponse(content={'status_code': exc.status_code, 'message': exc.message}, status_code=exc.status_code)


async def unknown_exception_handler(request: Request, exc: Exception) -> Response:
    return JSONResponse(content={'status_code': 500, 'message': 'Unknown error occured'}, status_code=500)


def init_exc_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ApplicationException, cast(ExceptionHandler, application_exception_handler))
    app.add_exception_handler(Exception, cast(ExceptionHandler, unknown_exception_handler))
