import json
import pandas as pd

# Load Postman collection JSON
with open("collection.json", "r") as f:
    data = json.load(f)

endpoints = []

for item in data["item"]:
    name = item["name"]
    method = item["request"]["method"]
    url = "".join(item["request"]["url"].get("raw", "")) if "url" in item["request"] else ""
    endpoints.append({"Name": name, "Method": method, "URL": url})

# Save to Excel
df = pd.DataFrame(endpoints)
df.to_excel("postman_endpoints.xlsx", index=False)

print("Exported to postman_endpoints.xlsx")
