Here is the improved version of your `README.md` in the proper format:

```markdown
# API Movie Project

A FastAPI application for managing data related to movies, TV series, genres, and releases.

## Requirements
- Python 3.8 or higher
- FastAPI
- Uvicorn
- Pandas

## Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/api-movie.git
   cd api-movie
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   uvicorn api.main:app --reload
   ```

## API Overview

The project contains the following data:

- **Movies**: 300 entries
- **TV Series**: 59 entries

### Available Endpoints

#### Movies
- `GET /movies` - Retrieve a list of all movies.
- `GET /movies/{id}` - Retrieve details of a movie by its ID.
- `GET /movies/grouped_by_year` - Get movies grouped by release year.
- `GET /movies/grouped_by_rating` - Get movies grouped by rating.
- `GET /movies/search?title=<title>` - Search for movies by title.

#### TV Series
- `GET /tvseries` - Retrieve a list of all TV series.
- `GET /tvseries/{id}` - Retrieve details of a TV series by its ID.
- `GET /tvseries/search?title=<title>` - Search for TV series by title.

## Additional Information

Feel free to explore the API documentation provided by FastAPI at `/docs` once the server is running.
```
