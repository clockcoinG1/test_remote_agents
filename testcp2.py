import requests
import json

def get_agents(base_url, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Editor-Plugin-Version':'copilot-chat/0.11.2023110301'
    }
    url = f'{base_url}/agents'
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json().get('agents', [])
    response.raise_for_status()

def chat_with_agent(base_url, agent_slug, message_content, token):
    url = f'{base_url}/agents/{agent_slug}?chat'
    headers = {
        'Authorization': f'Bearer {token}',
        # ... any other necessary headers
    }
    payload = [{
        'role': 'user',
        'content': message_content,
        'intent': 'conversation'
    }]
    response = requests.post(url, headers=headers, json=payload)
    if response.ok:
        return response.json()
    response.raise_for_status()

def search_code_or_docs(base_url, query, repo, token):
    url = f'{base_url}/skills/codesearch'
    headers = {
        'Authorization': f'Bearer {token}',
        'Copilot-Integration-Id': 'vscode-chat',
        'Accept': 'application/json',
        # ... any other necessary headers
    }
    body = {
        'query': query,
        'scopingQuery': {'repo': repo},
        'similarity': 0.766,
        'limit': 6
    }
    response = requests.post(url, headers=headers, json=body)
    if response.ok:
        return response.json()
    response.raise_for_status()

# Usage:
base_url = 'https://api.githubcopilot.com'
token = 'your_token_here'
agents = get_agents(base_url, token)
chat_response = chat_with_agent(base_url, agents[0]['slug'], 'Hello, Agent!', token)
search_response = search_code_or_docs(base_url, 'find all todos', 'your-repo', token)
