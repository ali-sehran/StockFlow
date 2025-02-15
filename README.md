# 📈 StockFlow – Real-time Stock Price Dashboard

**StockFlow** is a **containerized Data Engineering & DevOps project** that:
- ✅ **Fetches real-time stock data** using **Airflow DAGs**
- ✅ **Stores data in PostgreSQL**
- ✅ **Visualizes stock trends** in an **interactive Streamlit dashboard**
- ✅ **Runs fully in Docker** for **easy deployment** 🎯  
- ✅ **Securely accessible via Cloudflare Tunnel** on a personal server

🚀 **Built with modern DevOps & Data Engineering tools for a production-grade workflow.**
🔗 Live Demo: https://saved-stuff-general-collected.trycloudflare.com/
---

## 🔥 Tech Stack Used

| Tool / Tech             | Purpose                                  |
|-------------------------|------------------------------------------|
| 🐳 **Docker**           | Containerized Deployment                 |
| ☁️ **Cloudflare Tunnel** | Secure Remote Access                     |
| 🔄 **Apache Airflow**    | DAG-based Data Pipeline                  |
| 🗄️ **PostgreSQL**        | Database for storing stock prices        |
| 🎨 **Streamlit**        | Frontend Dashboard for visualization     |
| 📊 **Plotly**           | Data visualization in interactive charts |

---

## 🛠 Features

✅ **Real-time Stock Data Fetching** (Using Airflow DAGs)  
✅ **SQL-based Storage** (PostgreSQL)  
✅ **Dynamic Filters** (Date range selection)  
✅ **Interactive Charts** (Powered by Plotly)  
✅ **Fully Dockerized** (Easy deployment & scalability)
✅ **Secure Public Access via Cloudflare Tunnel**  
✅ **Deployed on a Personal Server (Self-Hosted Solution)**  

---

## 🚀 Deployment

### **1️⃣ Initial Setup with Docker Compose**

The **Docker Compose** file initializes the following services:
- **Apache Airflow** for orchestrating the data pipeline.
- **PostgreSQL** for storing the fetched stock data.

To start these services, run:

docker-compose up -d

This will:
- Start **PostgreSQL** for data storage.
- Launch **Apache Airflow** for data pipeline orchestration.

---

### **2️⃣ Build and Run the Streamlit App**

The **Streamlit app** is built using a **Dockerfile**. Follow these steps to build and run the app:

1. Navigate to the project directory:
   cd StockFlow

2. Build the Docker image for the Streamlit app:
   docker build -t stockflow-streamlit .

3. Run the Streamlit app container:
   docker run -d -p 8501:8501 stockflow-streamlit

4. Access the Streamlit dashboard at:
   http://localhost:8501

---

### **3️⃣ Deploy on a Personal Server (Cloudflare Tunnel)**

To securely expose the Streamlit dashboard on a personal server, use **Cloudflare Tunnel**:

1. Install `cloudflared` (Cloudflare Tunnel client) on your server.

2. Run the following command to expose the Streamlit app:
   cloudflared tunnel --url http://localhost:8501

3. This will generate a secure public URL, making StockFlow accessible over the internet.

---

## 📌 Access the Dashboard

Once deployed, access the StockFlow dashboard via:
- **Local Machine**: http://localhost:8501
- **Cloudflare Tunnel**: https://your-subdomain.trycloudflare.com

---

## 🛡 Security & Performance

🔒 **Cloudflare Tunnel** ensures secure, encrypted access to the dashboard.  
🚀 **Dockerized setup** for easy portability & scalability.  
📡 **Self-hosted** on a personal server to avoid third-party hosting costs.  

---

## 🐳 Docker Architecture

- **Docker Compose**:
  - Manages **Apache Airflow** and **PostgreSQL** services.
  - Ensures seamless communication between the data pipeline and database.

- **Dockerfile**:
  - Builds the **Streamlit app** container.
  - Includes all dependencies for the dashboard and visualization.

---

🚀 **StockFlow is now securely deployed via Cloudflare Tunnel on a personal server!** 🎯  
