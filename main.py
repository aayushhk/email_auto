from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import email_routes, search_routes, slack_routes

app = FastAPI(title="Email Sync and AI Response System", version="1.0")

# CORS Middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include different feature routes
app.include_router(email_routes.router, prefix="/emails", tags=["Emails"])
app.include_router(search_routes.router, prefix="/search", tags=["Search"])
app.include_router(slack_routes.router, prefix="/webhooks", tags=["Webhooks"])

@app.get("/")
def health_check():
    return {"status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
