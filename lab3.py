import requests

def search_github_repositories(query, sort='stars', order='desc', per_page=10):
    url = 'https://api.github.com/search/repositories'
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer YOUR_GITHUB_PERSONAL_ACCESS_TOKEN'
    }
    params = {
        'q': query,
        'sort': sort,
        'order': order,
        'per_page': per_page
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()['items']
    else:
        print(f"Error: {response.status_code}")
        return []

def main():
    query = input("Enter the search query: ")
    repositories = search_github_repositories(query)

    if repositories:
        print(f"Found {len(repositories)} repositories:")
        for repo in repositories:
            print(f"Name: {repo['name']}, Stars: {repo['stargazers_count']}, URL: {repo['html_url']}")
    else:
        print("No repositories found.")

if __name__ == '__main__':
    main()
