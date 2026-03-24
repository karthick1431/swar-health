from fastapi import FastAPI
import random

app = FastAPI()

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the chicken join a band? Because it had the drumsticks!",
    "I told my computer I needed a break, and now it won't stop sending me ads for vacations."
]

@app.get("/joke")
async def get_joke():
    return {'joke': random.choice(jokes)}
