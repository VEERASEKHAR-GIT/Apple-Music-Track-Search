import requests

def search_apple_music_tracks():
    artist_name = input("Enter the artist name: ")
    collection_name = input("Enter the collection name (or leave blank for any collection): ")
    track_name = input("Enter the track name (or leave blank for any track): ")

    # Construct the search term based on the user inputs
    search_term = artist_name
    if collection_name:
        search_term += f"+{collection_name}"
    if track_name:
        search_term += f"+{track_name}"

    # Define the API URL with the constructed search term
    url = f"https://itunes.apple.com/search?entity=song&limit=10000&term={search_term}"

    # Send a GET request to the iTunes API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if there are results in the response
        if "results" in data:
            # Extract and print the track names, artist names, and collection names
            for result in data["results"]:
                track_name_result = result.get("trackName", "{trackName}")
                artist_name_result = result.get("artistName", "{artistName}")
                collection_name_result = result.get("collectionName", "{collectionName}")
                print(f"Track: {track_name_result} - Artist: {artist_name_result} - Collection: {collection_name_result}")
        else:
            print("No results found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    search_apple_music_tracks()
