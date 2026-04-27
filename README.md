# 🏙️ Smart City Traffic & Emergency Response AI System

An AI-powered traffic management system for smart cities.

## 🚀 Features
- 🚗 Route planning for civilian drivers (BFS)
- 🚑 Emergency vehicle priority routing (A*)
- 🚦 Traffic signal coordination (CSP)
- 📋 Policy validation (Knowledge Base)
- 🧠 Priority prediction (ANN)

## 🛠️ Installation

### 1. Clone Repository
git clone https://github.com/Hadia665/traffic_controller.git
cd TrafficController

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run Application
streamlit run app.py

## 🧠 AI Modules
| Module | Technique | Purpose |
|--------|-----------|---------|
| Search | BFS, UCS, A* | Route finding |
| Knowledge Base | FOL, Rules | Policy validation |
| CSP | Backtracking, MRV, LCV | Signal timing |
| ANN | Neural Network | Priority prediction |

## 📊 Request Categories
| Category | Modules Used |
|----------|-------------|
| Route_Request | Search |
| Policy_Check | Knowledge Base |
| Control_Allocation | KB + CSP |
| Emergency_Response | ANN + KB + CSP + Search |
| Integrated | All Modules |
