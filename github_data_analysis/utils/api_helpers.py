import requests
import os

def get_repository_info(owner, repo_name):     
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'} if token else {}
    print("Making request with headers:", headers)
    url = f"https://api.github.com/repos/{owner}/{repo_name}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching repository data: {e}")
        return None
