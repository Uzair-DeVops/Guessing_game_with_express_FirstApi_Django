from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Add CORS middleware to handle cross-origin requests
origins = [
    "http://localhost",  # Allow frontend on localhost
    "http://localhost:3000",  # If the frontend might be on this port
    "http://127.0.0.1:5501",  # Allow frontend on this specific origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows these origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Pydantic model to handle input data

class GuessRequest(BaseModel):
    number: int

# Generate a random number
random_number = random.randint(0, 99)

@app.post("/guess")
async def guess_number(guess: GuessRequest):
    if guess.number < random_number:
        message = "Too low!"
    elif guess.number > random_number:
        message = "Too high!"
    else:
        message = "You guessed it!"
    
    return JSONResponse(content={"message": message, "number": random_number})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)
