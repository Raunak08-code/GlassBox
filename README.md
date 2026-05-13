# 🚀 GlassBox

> Real-time observability and monitoring platform built with Python, Prometheus, Grafana, Docker and PostgreSQL. 

GlassBox is a containerized observability platform designed to monitor system health, processes, Docker containers, and infrastructure telemetry in real time. It combines live terminal monitoring with Prometheus metrics scraping and Grafana visualization to create a complete monitoring pipeline.

---

# 📌 Features

## ✅ System Monitoring
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Network statistics tracking

## ✅ Process Monitoring
- Live top process tracking
- CPU usage per process
- Memory usage per process
- Process status monitoring

## ✅ Docker Monitoring
- Running container tracking
- Container CPU usage
- Container memory usage
- Docker integration using Docker SDK

## ✅ Live Dashboard
- Real-time terminal dashboard using Rich
- Dynamic metrics updates
- Process visualization
- Container monitoring display

## ✅ Observability Stack
- Prometheus exporter integration
- Prometheus scraping pipeline
- Grafana dashboards and visualization
- Time-series monitoring

## ✅ Database Integration
- PostgreSQL metrics storage
- Persistent monitoring data
- Historical metric collection

## ✅ Alert System
- CPU threshold alerts
- Memory threshold alerts
- Disk usage alerts
- Logging-based warnings

## ✅ Centralized Logging
- Structured logging system
- Monitoring lifecycle logs
- Warning and error tracking

## ✅ Containerized Deployment
- Dockerized application stack
- Multi-container architecture
- Docker Compose orchestration  

---

# 🏗️ Architecture

```text
+-------------------+
|   GlassBox Agent  |
|-------------------|
| System Metrics    |
| Process Metrics   |
| Docker Metrics    |
+---------+---------+
          |
          v
+-------------------+
| Prometheus Export |
+---------+---------+
          |
          v
+-------------------+
|    Prometheus     |
| Time-Series Store |
+---------+---------+
          |
          v
+-------------------+
|      Grafana      |
| Visualization UI  |
+-------------------+
```

---

# 🛠️ Tech Stack

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| Python         | Core monitoring engine        |
| psutil         | System and process metrics    |
| Rich           | Live terminal dashboard       |
| Docker SDK     | Container monitoring          |
| Prometheus     | Metrics scraping              |
| Grafana        | Dashboard visualization       |
| PostgreSQL     | Persistent metrics storage    |
| Docker Compose | Multi-container orchestration |


---

# 📂 Project Structure

```plaintext
GlassBox/
│
├── alert/
│   ├── __init__.py
│   └── alert_manager.py
│
├── dashboard/
│   ├── __init__.py
│   └── live_dashboard.py
│
├── database/
│   ├── __init__.py
│   └── db_manager.py
│
├── docker_monitoring/
│   ├── __init__.py
│   ├── container_metrics.py
│   └── docker_monitor.py
│
├── exporters/
│   ├── __init__.py
│   └── prometheus_exporter.py
│
├── logs/
│   ├── __init__.py
│   ├── logging_manager.py
│   ├── metrics.csv
│   └── system.logs
│
├── metrics/
│   ├── __init__.py
│   ├── process_metrics.py
│   └── system_metrics.py
│
├── monitoring/
│   ├── __init__.py
│   └── monitor_engine.py
│
├── prometheus/
│   └── prometheus.yml
│
├── src/
│   ├── __init__.py
│   └── cli.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```
---

# 🐳 Multi-Container Stack

GlassBox runs as a containerized observability stack:

| Container	           | Purpose                     |
| -------------------  | -------------------------   |
| glassbox-agent	   | Monitoring engine           |
| glassbox-prometheus  | Metrics scraping            |
| glassbox-grafana	   | Visualization dashboards    |
| glassbox-postgres	   | Persistent storage          |

---

# ▶️ Installation & Setup

### Clone repository:

```bash
git clone https://github.com/Raunak08-code/GlassBox.git

cd GlassBox
```

### Move into project folder:

```bash
python -m venv venv

source venv/bin/activate
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

---

### ▶️ Run GlassBox Locally

```bash
python -m src.cli start
```

---

# 🐳 Run Using Docker Compose

Start Full Stack:

```bash
docker compose up --build
```
Run in Background:

```bash
docker compose up --build -d
```

Stop Stack:

```bash
docker compose down
```

---

# 📊 Access Services

| Services          | URL                            |
| ----------------- | ------------------------------ |
| Prometheus        | http://localhost:9090          |
| Grafana           | http://localhost:3000          |
| Metrics Exporter  | http://localhost:8000/metrics  |

---

# 📈 Grafana Setup

Default Credentials 
```bash
username: admin
passward: admin
```
Add Prometheus Data Source
use:
```bash
http://prometheus:9090
```
# 📡 Prometheus Metrics

GlassBox exports metrics such as:
```bash
system_cpu_usage
system_memory_usage
system_disk_usage
```
These metrics are scraped by Prometheus and visualized in Grafana.

---

# 📸 Screenshots 

Terminal Dashboard
> Add screeshort here

Grafana Dashboard
> Add screensort here

Prometheus Target
> Add screensort here

---

# 🧠 Engineering Concepts Learned

GlassBox demonstrates practical understanding of:
- Observability pipelines
- Metrics collection
- Prometheus exporters
- Time-series monitoring
- Grafana dashboards
- Docker networking
- Multi-container orchestration
- Runtime debugging
- Infrastructure monitoring
- Process telemetry
- Service dependency management
- Structured logging

---

# 🚀 Future Improvements

- Alert notification (slack/Discard/Email)
- Historical analytics dashboard
- Kubernetes monitoring
- Anomaly detection
- Service health APIs
- Distributed tracing integration
- Log aggregation pipline

---

# 🧪 Example Commands

View Running Containers
```bash
docker ps
```

View Container Logs
```bash
docker logs glassbox-agent
```

Check Prometheus Targets
```bash
http://localhost:9090/targets
```
---

# 📌 Version

Current Release:    v1.0

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Raunak Pandey
B.Tech CSE (AI)

# ⭐ GlassBox
A lightweight yet powerful observability platform for real-time infrastructure monitoring, telemetry collection, and system visualization.