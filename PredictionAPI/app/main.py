import logging
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Import routers
from app.prediction import router as prediction_router

logging.basicConfig(level=logging.DEBUG)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="DstMlOpsCrypto Prediction API",
    description="API for crypto predictions using ML models",
    version="1.0.0",
    openapi_tags=[{"name": "predictions", "description": "Prediction operations"}],
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
async def root():
    return {"message": "Welcome to the Prediction API"}

app.include_router(prediction_router.router, prefix="/predict", tags=["predictions"])