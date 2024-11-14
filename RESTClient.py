# main.py
from Server.init import app
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Add CORS middleware to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],  # Adjust this as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def runServer():
    try:
        uvicorn.run(app,host='0.0.0.0', port=10000)
    except Exception as ex:
        print(f"Error: {ex}")
