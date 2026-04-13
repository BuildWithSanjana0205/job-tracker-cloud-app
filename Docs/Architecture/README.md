# 🗺️ Architectural Diagram Breakdown

![Architecture Diagram](../../docs/architecture/your-diagram.png)

### The Technical Flow:
1.  **Traffic Entry:** Users access the app via **AWS CloudFront** (HTTPS).
2.  **Frontend:** CloudFront fetches the UI from a private **S3 bucket** using **OAC** (Origin Access Control) for security.
3.  **Backend:** API calls are routed to an **EC2** instance in a **VPC Public Subnet**.
4.  **Compute Security:** The EC2 runs an **NGINX** proxy that directs traffic to a **Dockerized Flask App**.
5.  **Database:** The app fetches credentials from **AWS Secrets Manager** to connect to an **Amazon RDS** (Private).
6.  **CI/CD:** **GitHub Actions** builds the Docker image, pushes it to **Amazon ECR**, and **Terraform** manages the entire lifecycle.
