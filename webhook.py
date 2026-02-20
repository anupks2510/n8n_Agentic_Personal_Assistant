import requests

user_message = "use the tools and send an email to anupksingh2025@gmail.com. His name is Anup tell him that on this sunday we have webinar about the project development of Madhulata Sustainable Solutions and rest detials use on your own even dummy will work."

request_message = {"message": user_message}
url = "https://saniya25.app.n8n.cloud/webhook/a6551e15-71ca-41e8-8f66-86c2e7996a15"  # ← removed -test

response = requests.post(url, json=request_message)
# print(response.status_code)
print(response.text)          # ← add this — very helpful to see error messages
print(response.json)