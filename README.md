# 🚀 Job Tracker App: Cloud-Native DevOps Journey

[![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

## 📌 Project Overview
A production-simulated **Job Tracker Application** designed to solve the chaos of job hunting. This project demonstrates a full journey from local development to a cloud-architected environment on AWS, focusing on **Infrastructure as Code (IaC)**, **Network Security**, and **Containerization**.

## 🛠️ Tech Stack & AWS Services Used

| Category | Technology / Service |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JS (Served via **CloudFront** & **S3**) |
| **Backend** | Python (**Flask**), **Docker**, **NGINX** (Reverse Proxy) |
| **Database** | **Amazon RDS** (PostgreSQL/MySQL) |
| **Networking** | **VPC**, Public/Private Subnets, **IGW**, Route Tables, **NACLs** |
| **Security** | **AWS Secrets Manager**, **IAM Roles**, **CloudFront OAC** |
| **Infrastructure** | **Terraform** |
| **DevOps/CI-CD** | **GitHub Actions**, **Amazon ECR**, **SSM Agent** |

---

## 📊 Documentation & Architecture
To understand how this project is built for both cost-efficiency and professional scalability, explore the following:

*   **[🏗️ Architectural Diagram](./docs/architecture/README.md)** - Visual breakdown of components, security layers, and data flow.
*   **[🏢 Enterprise vs. Free Tier Analysis](./docs/architecture/enterprise-settings.md)** - How this project scales to a corporate level.
*   **[📅 Daily Progress Log](./docs/daily-log.md)** - A transparent record of challenges faced and lessons learned.

## 🚀 Key Features
- **Containerized Microservices:** Backend runs in Docker for environment parity.
- **Secure Secret Management:** Database credentials are never hardcoded; they are fetched via AWS Secrets Manager.
- **Zero-Open-Port Security:** Managing EC2 via AWS Systems Manager (SSM) instead of opening SSH (Port 22).

---
## 🗂️ Project Structure
```
job-tracker-app/
├── docs/
│   ├── architecture/
│   │   ├── README.md               # Detailed Diagram Breakdown
│   │   └── enterprise-settings.md   # Professional vs. Free Tier Comparison
│   └── daily-log.md                 # ALL days progress in one file
├── frontend/           # HTML/CSS/JS (S3 Hosted)
├── backend/            # Flask API (Dockerized)
├── infrastructure/     # Terraform (IaC)
└── README.md           # Main Entrance (The "Recruiter" View)
```

## 🛠️ Current Status

🚧 Project in progress — updating daily as I learn and build.

---

## 🤝 Connect With Me

(Add your LinkedIn later)

