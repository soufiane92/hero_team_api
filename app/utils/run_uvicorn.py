import uvicorn

from app.utils.logger import get_logger

logger = get_logger("::UVICORN::")

if __name__ == "__main__":
    uvicorn.run(
        app="app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
