import requests

BASE = "http://127.0.0.1:8000"

# 1) Register
payload = {
    "email": "Kaufmanian49@gmail.com",
    "password": "password123"
}
r = requests.post(f"{BASE}/auth/register", json=payload)
print("REGISTER", r.status_code, r.text)

# 2) Login
r = requests.post(f"{BASE}/auth/login", json=payload)
print("LOGIN   ", r.status_code, r.text)
token = r.json().get("access_token")

# 3) Create a project
headers = {"Authorization": f"Bearer {token}"}
project_payload = {"name": "My First Project", "description": "Testing"}
r = requests.post(f"{BASE}/projects", json=project_payload, headers=headers)
print("CREATE PROJECT", r.status_code, r.text)

# 4) List projects
r = requests.get(f"{BASE}/projects", headers=headers)
print("LIST PROJECTS ", r.status_code, r.text)
