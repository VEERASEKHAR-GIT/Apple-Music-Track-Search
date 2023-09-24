# Apple Music Track Search

**Author:** Veerasekhar Patibandla

This Python script, **Apple Music Track Search**, leverages the iTunes API to provide a seamless exploration and discovery experience for music tracks. Users can effortlessly search for tracks based on track name, artist name, or collection name. The script retrieves essential details such as track names, artist names, and collection names from the vast Apple Music database, enhancing the music discovery experience.

## How to Use

1. **Run the script `apple_music_track_search.py`.** This command will execute the script.

2. **Enter a search term when prompted.** The script will ask the user to input a search term (e.g., "Love", "Weezer"). This term will be used to search for tracks based on track name, artist name, or collection name.

3. **View the list of tracks and their respective details based on the search term.** After the user provides a search term, the script will retrieve and display a list of tracks and their associated information that match the search term.

## Code Explanation

The script operates as follows:

- It begins by prompting the user to input a search term, which can be a track name, artist name, or collection name.
- Subsequently, it constructs a URL using the provided search term and sends a GET request to the iTunes API.
- After successfully receiving a response (status code 200), the script parses the JSON response.
- It then extracts crucial details such as track names, artist names, and collection names from the response.
- Finally, it presents this information to the user.

## Sample Output

Here's an example of how the script's output might look based on a search term (e.g., "Love"):

```
Search term: Ar rahman
- Track: Jai Ho - Artist: A.R. Rahman, Sukhwinder Singh, Tanvi Shah, Mahalakshmi Iyer & Vijay Prakash - Collection: Slumdog Millionaire (Music from the Motion Picture)
- Track: Tum Se Hi - Artist: Mohit Chauhan - Collection: Jab We Met (Original Motion Picture Soundtrack)
- Track: Rehna Tu - Artist: A.R. Rahman - Collection: Delhi-6 (Original Motion Picture Soundtrack)
- Track: Kun Faya Kun - Artist: A.R. Rahman, Javed Ali & Mohit Chauhan - Collection: Rockstar (Original Motion Picture Soundtrack)
- Track: Khwaja Mere Khwaja - Artist: A.R. Rahman - Collection: Jodhaa Akbar (Original Motion Picture Soundtrack)

```

## Data Details

The script retrieves the following information for each track:

- **Track Name:** The name of the track.
- **Artist Name:** The name of the artist associated with the track.
- **Collection Name:** The name of the collection or album to which the track belongs.

## Dependencies

This script relies on the following dependencies:

- Python 3.x
- `requests` library

## Run the Script

To run the script, use the following command:

```bash
python apple_music_track_search.py
```


Feel free to ask if you have any more questions or need further clarification!
