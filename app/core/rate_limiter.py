# from fastapi import Request, HTTPException
# from app.core.redis_client import redis_client

# async def rate_limit(request: Request, call_next):

#     ip = request.client.host
#     key = f"rate_limit:{ip}"

#     current = redis_client.get(key)

#     if current is None:
#         redis_client.set(key, 1, ex=60)
#     else:
#         if int(current) > 10:
#             raise HTTPException(
#                 status_code=429,
#                 detail="Too many requests"
#             )
#         redis_client.incr(key)

#     response = await call_next(request)
#     return response


from fastapi import Request, HTTPException
from app.core.redis_client import redis_client

async def rate_limit(request: Request, call_next):

    ip = request.client.host
    key = f"rate_limit:{ip}"

    current = redis_client.incr(key)

    if current == 1:
        redis_client.expire(key, 60)

    if current > 10:
        raise HTTPException(
            status_code=429,
            detail="Too many requests"
        )

    response = await call_next(request)
    return response