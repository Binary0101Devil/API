# Postman Endpoints to Excel

## 📌 Overview

This script allows you to extract all API endpoints from a Postman collection and export them into an Excel file for easy reference and documentation. It parses the exported Postman collection JSON and captures each request’s **name, HTTP method, and URL**, including endpoints inside nested folders.

The output is saved as `postman_endpoints.xlsx`, which can be shared across teams, used for audits, or included in API documentation.

---

## 🚀 Features

* Extracts all endpoints from a Postman collection.
* Captures request **Name, Method, and URL**.
* Handles nested folders within the collection.
* Exports the data into an **Excel (.xlsx)** file.

---

## 📂 Input

* A Postman collection exported as JSON (recommended: Collection v2.1).
* Example filename: `MyCollection.postman_collection.json`.

---

## 📤 Output

* An Excel file named **`postman_endpoints.xlsx`** containing:

  * **Name** → Request name from Postman.
  * **Method** → HTTP method (GET, POST, PUT, etc.).
  * **URL** → Full API endpoint URL.

---

## ⚙️ Requirements

* Python 3.8+
* Required libraries:

  ```bash
  pip install pandas openpyxl
  ```

---

## 🛠️ Usage

1. Export your Postman collection:

   * In Postman → **Collections** → **... (three dots)** → **Export** → Choose **Collection v2.1** → Save JSON file.

2. Place the exported file in the same folder as the script.

3. Update the script with your JSON filename if needed:

   ```python
   with open("MyCollection.postman_collection.json", "r", encoding="utf-8") as f:
       data = json.load(f)
   ```

4. Run the script:

   ```powershell
   python3 postman-excel_Endpoints.py
   ```

5. Find your results in **`postman_endpoints.xlsx`**.

---

## ✅ Example Output (Excel)

| Name             | Method | URL                                                                          |
| ---------------- | ------ | ---------------------------------------------------------------------------- |
| Get User Details | GET    | [https://api.example.com/users/{id}](https://api.example.com/users/{id})     |
| Create New Order | POST   | [https://api.example.com/orders](https://api.example.com/orders)             |
| Update Inventory | PUT    | [https://api.example.com/inventory/45](https://api.example.com/inventory/45) |

---

## 📖 License

This project is open for personal and team use.

---

Do you also want me to add a **section for enhancements** (like adding folder grouping, saving CSV, or including headers/body parameters), so it’s future-proof for your repo?
