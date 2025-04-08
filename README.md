# AI CodeSense - Intelligent Code Review Assistant

AI CodeSense is an AI-powered code review assistant that helps developers analyze their code for potential improvements and best practices using GPT-4. It provides a full-stack implementation using **FastAPI (Python) for backend**, **Next.js (TypeScript) for frontend**, and **PostgreSQL for storage**.

---

## Features
- **AI-powered code review** using OpenAI's GPT-4
- **FastAPI backend** for efficient API handling
- **Next.js frontend** with an intuitive UI for submitting code
- **PostgreSQL database** to store code review history
- **Dockerized deployment** for easy scalability
- **Cloud-ready** (AWS, Docker, Kubernetes support)

---



## Setup & Installation

### **1️. Clone the repository**
```sh
git clone https://github.com/anuraghruday/ai-codesense.git
cd ai-codesense
```

### **2️. Setup the Backend**
#### Install dependencies
```sh
cd backend
pip install -r requirements.txt
```
#### Create a `.env` file in `backend/` and add:
```
OPENAI_API_KEY=your_openai_api_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
```
#### Start the FastAPI backend
```sh
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### **3️. Setup the Frontend**
#### Install dependencies
```sh
cd frontend
npm install
```
#### Start the Next.js frontend
```sh
npm run dev
```

### **4️. Database Setup (PostgreSQL)**
Ensure you have PostgreSQL installed and run the schema:
```sh
psql -U your_db_user -d your_db_name -f database/schema.sql
```

---

## Running with Docker
Build and run the application using Docker:
```sh
docker build -t ai-codesense .
docker run -p 8000:8000 ai-codesense
```
Alternatively, use **docker-compose** for running the full stack:
```sh
docker-compose up --build
```

---

## API Endpoints
### `POST /analyze`
#### Request Body:
```json
{
  "code_snippet": "def hello():\n    print('Hello, world!')"
}
```
#### Response:
```json
{
  "review": "Consider adding a docstring to improve code documentation."
}
```

---

## Tech Stack
- **Backend**: FastAPI, OpenAI GPT-4, PostgreSQL
- **Frontend**: Next.js, React, TypeScript
- **Database**: PostgreSQL
- **Cloud & Deployment**: AWS, Docker, Kubernetes

---

## License
This project is licensed under the MIT License.

---

## Contributing
Pull requests are welcome! Please open an issue to discuss before submitting any changes.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature-name`)
5. Open a pull request

---

## Contact
For any inquiries or support, reach out via:
- 📧 Email: anurag.hruday@gmail.com
- 🌐 GitHub: [github.com/anuraghruday](https://github.com/anuraghruday)

---

This **README.md** provides a complete guide to setting up, running, and contributing to AI CodeSense. 🚀🎯
