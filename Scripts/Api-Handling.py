############################################################
# API HANDLING IN PYTHON (BASIC → ADVANCED)
# Learn APIs, requests, JSON, error handling step by step
############################################################

############################################################
# 1. WHAT IS API?
# API = Application Programming Interface
# It allows communication between systems
# Example: App → API → Server → Response
############################################################


############################################################
# 2. INSTALL REQUIRED LIBRARY
############################################################

# Run in terminal:
# pip install requests


############################################################
# 3. BASIC GET REQUEST
############################################################

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("\n--- Basic GET ---")
print("Status Code:", response.status_code)  # 200 = success
print("Response Text:", response.text[:100])  # raw text


############################################################
# 4. JSON RESPONSE
############################################################

data = response.json()  # convert JSON → Python dict

print("\n--- JSON Data ---")
print(data)
print("Title:", data["title"])


############################################################
# 5. QUERY PARAMETERS
############################################################

params = {
    "userId": 1
}

res = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

print("\n--- Query Params ---")
print(res.json()[:2])  # first 2 records


############################################################
# 6. POST REQUEST (SEND DATA)
############################################################

payload = {
    "title": "New Post",
    "body": "This is content",
    "userId": 1
}

res = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

print("\n--- POST Request ---")
print(res.status_code)
print(res.json())


############################################################
# 7. PUT REQUEST (UPDATE)
############################################################

update_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated body"
}

res = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data)

print("\n--- PUT Request ---")
print(res.json())


############################################################
# 8. DELETE REQUEST
############################################################

res = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print("\n--- DELETE Request ---")
print("Status:", res.status_code)


############################################################
# 9. HEADERS (IMPORTANT)
############################################################

headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

res = requests.get(url, headers=headers)

print("\n--- Headers ---")
print(res.status_code)


############################################################
# 10. ERROR HANDLING
############################################################

try:
    res = requests.get("https://wrong-url.com")

    res.raise_for_status()  # raises error if not 200

except requests.exceptions.RequestException as e:
    print("\nError occurred:", e)


############################################################
# 11. TIMEOUT
############################################################

try:
    res = requests.get(url, timeout=2)
    print("\nTimeout Success")
except requests.exceptions.Timeout:
    print("Request timed out")


############################################################
# 12. SESSION (ADVANCED)
############################################################

# Keeps connection alive (faster for multiple calls)

session = requests.Session()

session.get(url)
session.get(url)

print("\n--- Session Used ---")


############################################################
# 13. DOWNLOAD FILE
############################################################

file_url = "https://jsonplaceholder.typicode.com/posts"

res = requests.get(file_url)

with open("data.json", "w") as f:
    f.write(res.text)

print("\nFile downloaded as data.json")


############################################################
# 14. LOOP THROUGH API DATA
############################################################

res = requests.get("https://jsonplaceholder.typicode.com/posts")

posts = res.json()

print("\n--- Loop Data ---")
for post in posts[:3]:
    print(post["id"], post["title"])


############################################################
# 15. BEST PRACTICE FUNCTION
############################################################

def fetch_api(url):
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("API Error:", e)
        return None


data = fetch_api(url)
print("\n--- Function Output ---")
print(data)


############################################################
# END NOTE
############################################################

# APIs are used in:
# - Data ingestion
# - ETL pipelines
# - Microservices
# - Web apps

print("\n🎉 API Handling Learning Completed!")