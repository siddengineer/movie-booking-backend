import time
import uuid
from fastapi import Request

async def request_logging_middleware(request: Request, call_next):

    request_id = str(uuid.uuid4())

    start_time = time.time()

    print(f"[REQUEST START] {request.method} {request.url} | ID: {request_id}")

    response = await call_next(request)

    process_time = round((time.time() - start_time) * 1000, 2)

    print(f"[REQUEST END] {request.method} {request.url} | ID: {request_id} | {process_time}ms")

    response.headers["X-Request-ID"] = request_id

    return response