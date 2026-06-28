from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.routes import user_route,learningSteps_route,challenges_route,habitLog_route,auth_route,dashboard_route,ai_route
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_route.router)
app.include_router(learningSteps_route.router)
app.include_router(challenges_route.router)
app.include_router(habitLog_route.router)
app.include_router(auth_route.router)
app.include_router(dashboard_route.router)
app.include_router(ai_route.router)