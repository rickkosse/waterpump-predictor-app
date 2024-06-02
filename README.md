
# Tanzanian Water Wells Prediction

## Overview

Access to clean water is a significant challenge in Tanzania. This project leverages data from existing water wells across the country to identify those in need of repair. By using this data-driven approach, we aim to assist the Tanzanian government in optimizing resources and ensuring that more citizens have access to clean water.

The primary objective is to develop a predictive model that can accurately identify wells requiring maintenance, reducing the time and costs associated with manually inspecting and identifying malfunctioning wells.

## Project Structure

```
waterpump-predictor-app/
│
├── Dockerfile
├── .dockerignore
├── README.md
├── requirements.txt
├── app.py
├── data/
│   ├── train_data.csv
│   ├── target_data.csv
│   └── X_data.csv
├── tanzania.geojson
├── templates/
│   └── index.html
├── static/
│   └── js/
│       └── map.js
├── deployment.yaml
└── service.yaml
```

## Setup and Installation

### Prerequisites

- Docker
- Kubernetes (optional, for deployment)

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/rickkosse/waterpump-predictor-app.git
cd waterpump-predictor-app
```

2. **Build the Docker image:**

```bash
docker build -t waterpump-predictor .
```

3. **Run the Docker container:**

```bash
docker run -p 5000:5000 waterpump-predictor
```

4. **Access the application:**

Open your web browser and navigate to `http://localhost:5000`.

## Usage

- Click on a location on the map to see the prediction of the functionality of a water pump at that location.

## Deployment to Kubernetes

1. **Push the Docker image to a container registry:**

```bash
docker tag waterpump-predictor yourdockerhubusername/waterpump-predictor:latest
docker push yourdockerhubusername/waterpump-predictor:latest
```

2. **Apply the Kubernetes deployment and service:**

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

3. **Check the status of the pods and services:**

```bash
kubectl get pods
kubectl get services
```

4. **Access the application:**

If using Minikube, you can access the service with:

```bash
minikube service waterpump-predictor-service
```

Otherwise, access the application using the external IP provided by your cloud provider.

## Data

The `data` directory contains the following files:

- `train_data.csv`: Training data for the model.
- `target_data.csv`: Target labels for the training data.
- `X_data.csv`: Additional data used in the application.

## Code Description

- `app.py`: Main Flask application file.
- `Dockerfile`: Docker configuration file.
- `.dockerignore`: Files and directories to ignore in the Docker build process.
- `requirements.txt`: Python dependencies.
- `tanzania.geojson`: GeoJSON file containing the geographical data for Tanzania.
- `templates/index.html`: HTML template for the Flask application.
- `static/js/map.js`: JavaScript file for handling the map interactions.
- `deployment.yaml`: Kubernetes deployment configuration.
- `service.yaml`: Kubernetes service configuration.

## Contributing

Feel free to fork this project and submit pull requests. Any contributions, suggestions, or improvements are welcome.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Data provided by [Tanzania Water Resources Management](https://www.tanzaniawrm.org/)
- GeoJSON data from [GeoBoundaries](https://www.geoboundaries.org/)
