# ⚡ NetPulse Pro

NetPulse Pro is a powerful, modern cybersecurity threat detection and response platform built with Django (backend) and React (frontend). It uses AI-enhanced scanning to identify devices within a network and provides actionable insights via a secure, role-based dashboard interface. The app is fully containerized with Docker and ready for scalable deployment via Kubernetes (EKS).

---

## 🚀 Features

- 🔍 **Network Threat Scanning:** Detect active hosts in a subnet using intelligent scanning tools.
- 🧠 **AI-Powered Detection Engine:** Leverages modern AI techniques for smarter threat identification (ongoing).
- 🔐 **Role-Based Access Control:**
  - `Admin` – Full access to scan and manage the platform.
  - `Analyst` – Limited to viewing reports and insights.
- 📊 **Modern React Dashboard:** Built with Vite, Bootstrap, and responsive design for desktop and mobile.
- 📦 **Dockerized Infrastructure:** Backend, frontend, and Nginx all containerized and ready for production.
- ☁️ **Kubernetes Ready:** Designed for deployment on AWS EKS or other cloud providers.

---

## 🗂️ Project Structure

netpulse/
├── backend/ # Django backend
│ └── manage.py
├── frontend/ # React + Vite frontend
│ └── src/
├── nginx.conf # Custom Nginx config for production frontend
├── docker-compose.yml # Multi-service Docker Compose setup
├── Dockerfile # Frontend production Dockerfile
├── Dockerfile.dev # Frontend development Dockerfile (with Vite hot reload)
├── requirements.txt # Python dependencies
├── .env # (ignored) Environment variables
└── README.md # You're here!



---

## 🧑‍💻 Local Development

### Prerequisites

- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- Git

### 1. Clone the repository

```bash
git clone https://github.com/your-username/netpulse.git
cd netpulse
2. Create and connect the Docker network


docker network create netpulse_network
3. Build and run frontend + backend


# Start backend (example only if not dockerized)
cd backend
python manage.py runserver 0.0.0.0:8000

# In another terminal
cd ../frontend
sudo docker compose up --build frontend
Visit http://localhost:3000


🔐 Authentication Roles
Role	Access
Admin	Full access to dashboard + scan
Analyst	View-only access


You can set roles when creating users through the Django admin panel or via the API.

📦 Deployment (Preview)
NetPulse Pro is built for production deployment using:

Docker Compose (for production testing or local staging)

Kubernetes via Amazon EKS (recommended for production)

Upcoming deployment support includes:

CI/CD with GitHub Actions

AWS ECR (Elastic Container Registry)

Helm Charts

HTTPS with custom domain

🧪 Testing
Basic tests (unit & integration) coming soon. AI and scan engine validation will be part of future test suites.


🛠️ Technologies Used
Backend: Django REST Framework, Custom Auth, Subprocess/Nmap

Frontend: React, Vite, Bootstrap

DevOps: Docker, Nginx, Kubernetes (EKS-ready)

Database: SQLite for development (PostgreSQL for production)

🧠 Upcoming Features
AI-enhanced threat classification

Log-based anomaly detection

Notification system (Slack, Email)

PDF & CSV threat reports

Scheduled scans and monitoring alerts

📄 License
MIT License – free to use, modify, and distribute.

🤝 Contributing
Pull requests are welcome! Please:

Fork the repo

Create a feature branch

Commit with clear messages

Submit a PR after testing

👨‍💻 Author
Sam Mochache

