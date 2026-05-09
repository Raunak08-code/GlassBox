# 🚀 System Monitoring CLI Tool

A lightweight Python-based system monitoring tool that tracks CPU and memory usage in real time using a command-line interface.

This project demonstrates practical concepts of:
- System monitoring
- File handling
- Logging architecture
- Docker containerization
- CLI tool development
- Runtime error handling
- Config-driven applications

---

# 📌 Features

✅ Real-time CPU monitoring  
✅ Memory usage tracking  
✅ CSV metric logging  
✅ TXT event logging  
✅ JSON configuration support  
✅ Graceful shutdown handling  
✅ Docker support  
✅ CLI-based execution  
✅ Threshold-based warning system  

---

# 🛠️ Tech Stack

- Python 3.10
- psutil
- argparse
- csv
- json
- Docker

---

# 📂 Project Structure

```plaintext
System-Monitoring-CLI-Tool/
│
├── config/
│   └── config.json
│
├── logs/
│
├── src/
│   ├── cli.py
│   ├── monitor.py
│   ├── logger.py
│   ├── metrics.py
│   └── config_loader.py
│
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Configuration

Example `config.json`:

```json
{
    "interval": 5,
    "cpu_threshold": 80,
    "log_file": "logs/system.log",
    "csv_file": "logs/metrics.csv"
}
```

---

# ▶️ Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/System-Monitoring-CLI-Tool.git
```

Move into project folder:

```bash
cd System-Monitoring-CLI-Tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
python src/cli.py start
```

---

# 🐳 Docker Usage

Build Docker image:

```bash
docker build -t system-monitor .
```

Run container:

```bash
docker run system-monitor
```

---

# 📊 Example Output

```plaintext
CPU: 32% | MEMORY: 51%
CPU: 44% | MEMORY: 53%
WARNING: CPU usage crossed 80%
```

---

# 📝 Example Logs

```plaintext
[2026-05-09 11:20:01] Monitoring Started Successfully
[2026-05-09 11:20:08] WARNING: CPU usage crossed 80%
[2026-05-09 11:20:15] Monitoring Stopped
```

---

# 🧠 Key Engineering Concepts Learned

- File handling in Python
- Runtime logging systems
- Exception handling
- Graceful shutdown handling
- Docker containerization
- Monitoring architecture
- CLI application development
- Config-based system design

---

# 🚀 Future Improvements

- Disk monitoring
- Network monitoring
- Docker container monitoring
- Live terminal dashboard
- Email alerts
- Multi-threaded monitoring
- Linux daemon support
- Prometheus integration

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Raunak Pandey

B.Tech CSE (AI)