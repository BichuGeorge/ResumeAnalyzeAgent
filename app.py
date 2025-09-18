from route.api import resume_analysis_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(resume_analysis_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)