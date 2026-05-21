from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="UCE TalentPath API",
    description="Backend API for UCE TalentPath ATS system",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "UCE TalentPath Backend running successfully"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "backend"
    }



