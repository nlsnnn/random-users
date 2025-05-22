from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import UsersException


def register_error_handlers(app: FastAPI):
    @app.exception_handler(UsersException)
    def handle_users_error(request: Request, exc: UsersException):
        return JSONResponse(
            content={"message": exc.message}, status_code=exc.status_code
        )
