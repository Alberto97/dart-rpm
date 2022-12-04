import requests

dart_latest_sdk_url = "https://storage.googleapis.com/dart-archive/channels/stable/release/latest/VERSION"

response = requests.get(dart_latest_sdk_url)
data = response.json()
version = data["version"]
print(version, end='')
