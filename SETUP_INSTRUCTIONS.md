# 🚀 Quick Setup Instructions

## 📋 **Prerequisites**
- Python 3.8+
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))

## ⚡ **Quick Start**

### **1. Clone the Repository**
```bash
git clone https://github.com/dhruvsahu007/fork-extend.git
cd fork-extend/AI-Agents-for-Medical-Diagnostics
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Configure API Key**
```bash
# Copy the example file
cp apikey.env.example apikey.env

# Edit apikey.env and add your OpenAI API key:
# OPENAI_API_KEY=your_actual_api_key_here
```

### **4. Run the Web Application**
```bash
streamlit run streamlit_app.py
```

🌐 **Access:** http://localhost:8501

### **5. Alternative: Run Original CLI**
```bash
python Main.py
```

## 🏥 **Features**
- **6 Medical AI Specialists** (Cardiologist, Psychologist, Pulmonologist, Neurologist, Dermatologist, Endocrinologist)
- **Professional Web Interface** with real-time progress tracking
- **Concurrent Processing** for fast analysis
- **Interactive Dashboard** with visual analytics
- **Multiple Export Formats** (TXT, JSON)

## 🔧 **Troubleshooting**
- **API Key Issues:** Make sure `OPENAI_API_KEY` is set in `apikey.env`
- **Dependencies:** Ensure all packages from `requirements.txt` are installed
- **Port Issues:** If port 8501 is busy, Streamlit will use the next available port

---
*Enhanced Medical AI Diagnostics System - Fork & Extend Project*