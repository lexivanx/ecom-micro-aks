# AKS E-Commerce Microservices

## Overview
E-commerce platform with microservices, deployed on AKS

## Architecture

The e-commerce platform is made up of three microservices, each a standalone application that runs in its own Docker container:

- **User Service**: Handles user registration, authentication, and profile management.
- **Product Service**: Manages the product catalog, including product details and inventory.
- **Order Service**: Manages customer orders and coordinates with the User Service and Product Service.

Each microservice is deployed as a separate Helm chart, enabling easy management of application versions and configurations. 

## Kubernetes Deployment

The services are deployed to an Azure Kubernetes Service (AKS) cluster using Helm charts found in the [Kubernetes directory](./kubernetes).

## Infrastructure as Code (IaC)

The infrastructure necessary for the e-commerce platform, such as the AKS cluster, Azure Container Registry, Azure Key Vault, and Azure SQL Database (optional), are provisioned using Azure Resource Manager (ARM) templates found in the [Infrastructure directory](./infrastructure).

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for more details.
