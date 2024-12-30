from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import movies, tvseries, genres, releases

app = FastAPI()

# Define the allowed origins (You can specify your front-end domains or use '*' for all origins)
origins = [
    "http://localhost:5173",  # For local development
    "http://localhost:3000",  # If your front-end is on port 3000 (e.g., React app)
    "https://api-movie-peach.vercel.app/",  # Replace with your actual production domain
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows only the listed domains (or '*' for all)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Register routes
app.include_router(movies.router, prefix="/movies", tags=["Movies"])
app.include_router(tvseries.router, prefix="/tvseries", tags=["TV Series"])
app.include_router(genres.router, prefix="/genres", tags=["Genres"])
app.include_router(releases.router, prefix="/releases", tags=["Releases"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie API"}
