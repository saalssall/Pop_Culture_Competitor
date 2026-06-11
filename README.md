# Pop Culture Competitor

A Python-based GUI application that aggregates trending pop culture data from multiple online sources and allows users to view, compare, and save their favorite rankings to a local database.

## Overview

**Pop Culture Competitor** is an interactive desktop application created as an academic assignment for QUT's IFB104 course ("Building IT Systems"). It demonstrates the integration of web scraping, HTML pattern matching, database management, and GUI design using Python's standard library.

The application fetches real-time data from three different pop culture sources, displays the top 3 items in each category, and allows users to save their favorites to an SQLite database for future reference.

## Features

- **Multi-Source Data Aggregation**: Scrapes trending content from three different online sources:
  - **Netflix Top 10**: US TV Guide's trending TV shows with runtime information
  - **MyAnimeList**: Top airing animes with scores
  - **Official Charts**: Most popular songs with artist information

- **Interactive GUI**: Built with Tkinter, featuring:
  - Radio buttons to select data sources
  - Buttons to view top 3 items
  - Direct links to original data sources
  - Real-time message display

- **SQLite Database Integration**: Save top 3 rankings to a local database (`saved_rankings.db`) for tracking favorites over time

- **Web Scraping**: Uses regular expressions to extract data from HTML pages via URL requests

- **Error Handling**: Robust connection error handling and user feedback

## Requirements

- **Python 3.x**
- Only standard library modules:
  - `tkinter` - GUI framework
  - `sqlite3` - Database management
  - `urllib` - Web requests
  - `re` - Regular expressions
  - `webbrowser` - Open URLs in default browser
  - `sys` - System functions

*Note: No external dependencies required. All modules are included in standard Python installations.*

## Project Files

| File | Description |
|------|-------------|
| `Pop_Culture_Competitor_v1.py` | Latest version with full functionality including database operations and URL handling |
| `Pop_Culture_Competitor_v0.py` | Initial version with core GUI and web scraping features |
| `saved_rankings.db` | SQLite database storing saved rankings |
| `image2.gif` | Header image displayed in the application |
| `README.md` | This documentation file |

## Usage

1. **Run the application**:
   ```bash
   python Pop_Culture_Competitor_v1.py
   ```

2. **Select a data source** using the radio buttons:
   - US TV Guide's Trending TV Shows
   - Top Airing Animes on MyAnimeList
   - Most Popular Songs on Official Charts

3. **View rankings**:
   - Click "Show top three" to display the current top 3 items
   - Data is fetched directly from online sources in real-time

4. **Visit data sources**:
   - Click "Show data source" to open the original website in your default browser

5. **Save to database**:
   - Click "First", "Second", or "Third" buttons to save individual rankings to the local database

## Technical Details

### Data Extraction
The application uses regular expressions to extract specific information from HTML pages:
- TV show titles and runtimes
- Anime titles and scores
- Song titles and artists

### Database Schema
The `saved_rankings.db` contains a `rankings` table with the following fields:
- Data source (where the ranking came from)
- Rank position (1st, 2nd, or 3rd)
- Item identifier (title, song, etc.)
- Item property (runtime, score, artist, etc.)

### Color Scheme
- **v1.0**: Seagreen background
- **v0.0**: Dark orange background

## Version History

- **v1.0** - Full implementation with complete database operations, comprehensive error handling, and all three data sources fully functional
- **v0.0** - Initial prototype with basic GUI and web scraping features

## Academic Context

This project was developed as part of QUT's IFB104 assessment, demonstrating:
- Python programming fundamentals
- HTML and web scraping techniques
- Regular expression pattern matching
- SQLite database management
- GUI design with Tkinter
- Error handling and user experience design

## Notes

- Requires an active internet connection to fetch real-time data
- Data availability depends on the status of source websites
- Database file is created automatically on first save operation
- All source code was written from scratch following academic integrity guidelines

## Author

Hamidullah Rezae  
QUT Student - IFB104 (Semester 2, 2024)

---

*This project uses only standard Python 3 libraries and contains no external dependencies.*
