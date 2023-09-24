import requests

def search_apple_music_tracks():
    # Get the search term from the user
    search_term = input("Enter a search term: ")

    # Define the API URL with the search term
    url = f"https://itunes.apple.com/search?entity=song&limit=10000&term={search_term}"

    # Send a GET request to the iTunes API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if there are results in the response
        if "results" in data:
            # Extract and print the track names
            for result in data["results"]:
                track_name = result.get("trackName", "N/A")
                artist_name = result.get("artistName", "N/A")
                print(f"Track: {track_name} - Artist: {artist_name}")
        else:
            print("No results found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    search_apple_music_tracks()
