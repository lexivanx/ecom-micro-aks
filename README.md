# AKS E-Commerce Microservices

## Overview
E-commerce platform with microservices, deployed on AKS

## Architecture

The e-commerce platform is made up of three microservices, each a standalone application that runs in its own Docker container:

- **User Service**: Handles user registration, authentication, and profile management.
- **Product Service**: Manages the product catalog, including product details and inventory.
- **Order Service**: Manages customer orders and coordinates with the User Service and Product Service.

Each microservice is deployed as a separate Helm chart, enabling easy management of application versions and configurations. 

The e-commerce platform also utilizes Azure Functions for processing payments and sending confirmation emails asynchronously. These functions are defined in the [Functions directory](./functions).

## Kubernetes Deployment

The services are deployed to an Azure Kubernetes Service (AKS) cluster using Helm charts found in the [Kubernetes directory](./kubernetes).

## Infrastructure as Code (IaC)

The infrastructure necessary for the e-commerce platform, such as the AKS cluster, Azure Container Registry, Azure Key Vault, Azure Functions, and Azure SQL Database (optional), are provisioned using Azure Resource Manager (ARM) templates found in the [Infrastructure directory](./infrastructure).

## Security
This project incorporates DevSecOps practices. It uses Azure Key Vault for secrets management, ensuring sensitive data isn't stored in the codebase or version control. Infrastructure as Code (IaC) files are scanned for security best practices using Checkov. Docker images are also scanned for known vulnerabilities using tools such as Anchore or Clair.

## CI/CD Pipeline
The [CI/CD pipeline](./.github/workflows/ci-cd.yml) automates the continuous integration and deployment processes for the e-commerce microservices. It ensures that changes to the codebase are built, tested, and deployed in a consistent and reliable manner.

The pipeline is triggered manually and consists of the follwing stages:

1. Build and Security Scans: During this stage, the code is built, and security scans are performed to identify any potential vulnerabilities. The Infrastructure as Code (IaC) files are scanned using Checkov to ensure security best practices. Additionally, the Docker images are scanned using Anchore to detect known vulnerabilities.

2. Deployment to AKS: In this stage, the application is deployed to the Azure Kubernetes Service (AKS) cluster. The Kubernetes manifests defined in the kubernetes directory are applied to the cluster using kubectl. This ensures that the latest version of the microservices is running in the AKS environment.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for more details.
