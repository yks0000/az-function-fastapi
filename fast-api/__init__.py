import logging

import azure.functions as func
from fastapp.api import app
import nest_asyncio

nest_asyncio.apply()


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req, context)
