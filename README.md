# Apple Music Track Search
## Author: Veerasekhar Patibandla

This Python script, **Apple Music Track Search**, utilizes the iTunes API to facilitate seamless exploration and discovery of music tracks. Users can easily search for their preferred tracks and uncover new melodies with a simple search term. The script retrieves song names and artist details from the vast Apple Music database, enhancing the music discovery experience.

## How to Use:
1. Run the script `apple_music_track_search.py`.
2. Enter a search term when prompted.
3. View the list of tracks and their respective artists based on the search term.

## Code Explanation:
The script begins by prompting the user to input a search term. It constructs a URL with the search term and sends a GET request to the iTunes API. Upon receiving a successful response (status code 200), it parses the JSON response and extracts track names along with their respective artist names. The results are then displayed to the user.

## Sample Output:**Love**
Track: Love Story - Artist: Taylor Swift
Track: Somebody to Love - Artist: Queen
Track: Endless Love - Artist: Lionel Richie & Diana Ross

## Dependencies:
- Python 3.x
- `requests` library

# Run the Script:
python apple_music_track_search.py
