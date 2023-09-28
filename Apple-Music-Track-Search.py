import requests

def search_apple_music_tracks():
    # Prompt the user to provide at least one term (artist name, collection name, or track name)
    print("Please provide at least one of the following:")
    artist_name = input("Enter the artist name (or leave blank for any artist): ")
    collection_name = input("Enter the collection name (or leave blank for any collection): ")
    track_name = input("Enter the track name (or leave blank for any track): ")

    # Check if at least one term is provided
    if not (artist_name or collection_name or track_name):
        print("At least one term (artist name, collection name, or track name) is required.")
        return

    # Construct the search term based on the user inputs
    search_term = ""
    if artist_name:
        search_term += f"{artist_name}"
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
                # Extract track name, artist name, and collection name from the result
                track_name_result = result.get("trackName", "{trackName}")
                artist_name_result = result.get("artistName", "{artistName}")
                collection_name_result = result.get("collectionName", "{collectionName}")
                
                # Print the track details
                print(f"Track: {track_name_result} - Artist: {artist_name_result} - Collection: {collection_name_result}")
        else:
            print("No results found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    search_apple_music_tracks()
