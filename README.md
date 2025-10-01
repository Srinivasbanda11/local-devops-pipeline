# Local DevOps Pipeline

## Overview
A comprehensive full-stack local DevOps project demonstrating modern software development and deployment practices. This project showcases a complete CI/CD pipeline with containerized applications, orchestration, and monitoring capabilities, all designed to run in a local development environment.

## Project Architecture
This project implements a production-grade DevOps workflow featuring:

- **Frontend Application**: Modern web interface built with Node.js
- **FastAPI Backend**: RESTful API services with Python FastAPI framework
- **Database Layer**: PostgreSQL for persistent data storage
- **CI/CD Automation**: Automated build, test, and deployment workflows
- **Container Orchestration**: Kubernetes manifests for scalable deployment
- **Monitoring & Observability**: Prometheus and Grafana for application insights

## Technology Stack

- **Backend**: Python 3.11 with FastAPI
- **Frontend**: Node.js 18 (scaffold ready)
- **Database**: PostgreSQL 15
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana
- **Version Control**: Git

## Project Structure

```
local-devops-pipeline/
├── backend/
│   ├── app/
│   │   └── main.py           # FastAPI application
│   ├── Dockerfile             # Backend container image
│   └── requirements.txt       # Python dependencies
├── frontend/
│   └── Dockerfile             # Frontend container image (scaffold)
├── db/
│   └── docker-compose.yml     # PostgreSQL setup
├── k8s/
│   ├── backend-deployment.yaml      # Backend K8s resources
│   ├── frontend-deployment.yaml     # Frontend K8s resources
│   └── postgres-statefulset.yaml    # Database K8s resources
├── monitoring/
│   ├── docker-compose.yml     # Prometheus + Grafana stack
│   └── prometheus.yml         # Prometheus configuration
├── .github/workflows/         # CI/CD pipeline definitions
└── README.md                  # Project documentation
```

## Components

### Backend Service
- **Technology**: FastAPI with Python 3.11
- **Dependencies**: uvicorn, psycopg2-binary, sqlalchemy, pydantic
- **Features**: RESTful API, database integration, async support
- **Port**: 8000

### Frontend Service
- **Technology**: Node.js 18 Alpine
- **Status**: Scaffold Dockerfile ready for implementation
- **Port**: 3000

### Database
- **Technology**: PostgreSQL 15 Alpine
- **Configuration**: 
  - User: devops
  - Database: devopsdb
  - Port: 5432
- **Storage**: Persistent volume support

### Kubernetes Manifests
- **Backend**: Deployment with 2 replicas + ClusterIP Service
- **Frontend**: Deployment with 2 replicas + NodePort Service
- **Database**: StatefulSet with PVC + ClusterIP Service

### Monitoring Stack
- **Prometheus**: Metrics collection and monitoring
  - Port: 9090
  - Scrapes: backend, postgres, node-exporter
- **Grafana**: Visualization and dashboards
  - Port: 3001
  - Default credentials: admin/admin

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Kubernetes (minikube, k3s, or Docker Desktop)
- kubectl CLI
- Git

### Running the Database
```bash
cd db
docker-compose up -d
```

### Building and Running Backend
```bash
cd backend
docker build -t backend:latest .
docker run -p 8000:8000 backend:latest
```

### Running Monitoring Stack
```bash
cd monitoring
docker-compose up -d
```
Access:
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3001

### Deploying to Kubernetes
```bash
# Apply all manifests
kubectl apply -f k8s/

# Check deployment status
kubectl get pods
kubectl get services
```

## Development Workflow

1. **Local Development**: Use Docker Compose for quick iteration
2. **Testing**: Automated tests run via GitHub Actions
3. **Build**: Docker images built for each service
4. **Deploy**: Kubernetes manifests for production-like environment
5. **Monitor**: Prometheus and Grafana track application health

## CI/CD Pipeline

The project uses GitHub Actions for automated workflows:
- Code linting and validation
- Automated testing
- Docker image building
- Deployment automation

## Monitoring and Observability

- **Prometheus** collects metrics from all services
- **Grafana** provides visualization dashboards
- **Health checks** ensure service availability
- **Logging** for debugging and troubleshooting

## Best Practices Implemented

- ✅ Multi-stage Docker builds for optimized images
- ✅ Environment-based configuration
- ✅ Health checks for all services
- ✅ Persistent storage for stateful services
- ✅ Resource limits and requests in K8s
- ✅ Rolling updates and zero-downtime deployments
- ✅ Monitoring and alerting
- ✅ Infrastructure as Code

## Future Enhancements

- [ ] Implement frontend application
- [ ] Add API authentication and authorization
- [ ] Set up automated testing suite
- [ ] Configure Grafana dashboards
- [ ] Add logging aggregation (ELK/Loki)
- [ ] Implement service mesh (Istio)
- [ ] Add secrets management (Vault)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is for educational and demonstration purposes.
