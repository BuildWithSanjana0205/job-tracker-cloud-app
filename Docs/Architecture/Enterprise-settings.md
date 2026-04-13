# 🏢 Professional vs. Free Tier: Design Analysis

This project is built using **AWS Free Tier** constraints for personal development. However, a recruiter or architect should note that I have designed it to be "Enterprise-Ready." 

### ⚖️ Comparison Table

| Feature | Project Implementation (Free Tier) | Enterprise Standard | Decision Logic |
| :--- | :--- | :--- | :--- |
| **Compute** | Single **t2.micro** EC2 | **Auto Scaling Group (ASG)** | Professional apps use ASGs across multiple AZs for high availability. |
| **Networking** | EC2 in Public Subnet | EC2 in **Private Subnet** | In Prod, compute nodes sit in private subnets; only the **Load Balancer (ALB)** is public. |
| **Load Balancing** | NGINX Reverse Proxy | **Application Load Balancer (ALB)** | ALBs provide native health checks and offload SSL management more efficiently. |
| **Database** | Single RDS Instance | **Multi-AZ RDS** | Critical for disaster recovery and 99.99% uptime in corporate settings. |
| **Storage** | S3 Standard | S3 with **Versioning & Cross-Region Replication** | Protects against accidental deletion and regional AWS outages. |
| **Connectivity** | Internet Gateway (IGW) | **NAT Gateway** | Private instances need NAT Gateways to fetch updates/patches securely without public IPs. |

### 🧠 Why This Project Matters
By choosing these specific AWS services (SSM, OAC, Secrets Manager), I have simulated a **Secure Enterprise Environment** even while staying within the $0/month budget. This proves competency in **Security-First** cloud design.
