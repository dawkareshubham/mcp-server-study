import requests

CHESS_API_BASE = "https://api.chess.com/pub"

headers = {
    "accept": "application/json",
    "User-Agent": "MCP-Chess-Client/1.0"
}

def get_player_profile(username):
    """Fetches the player profile from Chess.com API."""
    url = f"{CHESS_API_BASE}/player/{username}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_player_stats(username):
    """Fetches the player stats from Chess.com API."""
    url = f"{CHESS_API_BASE}/player/{username}/stats"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()