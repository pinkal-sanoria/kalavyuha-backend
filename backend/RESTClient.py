from Server.init import app
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# Add CORS middleware to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now (can restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)

def runServer():
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as ex:
        print(f"Error: {ex}")