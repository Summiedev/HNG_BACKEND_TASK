HNG12 Backend Task API

This is a simple Flask API for the HNG12 backend track. It returns a JSON response containing the registered email, the current datetime in ISO 8601 format, and the GitHub repository URL.

🚀 Setup Instructions

1️⃣ Clone the repository

git clone https://github.com/yourusername/your-repo.git

2️⃣ Navigate into the project directory

cd your-repo

3️⃣ Create a virtual environment (Optional but recommended)

python -m venv venv
source venv/bin/activate  
venv\Scripts\activate 

4️⃣ Install dependencies

pip install -r requirements.txt

5️⃣ Run the application

python app.py

6️⃣ Access the API locally

Visit http://127.0.0.1:5000/ in your browser or use Postman/cURL.

📌 API Documentation

Base URL:

<your-public-url>

Endpoint:

GET /

Response Format (200 OK):

{
  "email": "apatirasummie@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Summiedev"
}

🛠 Example Usage

Using Insomnia or Postman

GET <your-public-url>

Using Python Requests:

import requests

response = requests.get("<your-public-url>")
print(response.json())

📌 Deployment

Hosting platform: Render, Vercel, Railway, Heroku, or any cloud service.

Public API URL: Your Public API URL


🌍 CORS Handling

CORS is enabled to allow cross-origin requests, ensuring the API is accessible from different domains.

📌 Version Control & Documentation

GitHub Repository: View Source Code

Repository Visibility: Public

Documentation: This README file contains all necessary details.

🔗 Hire Python Developers

Looking for skilled Python developers? Check out HNG Tech Python Developers.

https://hng.tech/hire/python-developers

