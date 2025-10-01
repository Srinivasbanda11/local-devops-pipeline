from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DevOps Pipeline API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to DevOps Pipeline API", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/api/items")
async def get_items():
    return {"items": ["item1", "item2", "item3"]}
