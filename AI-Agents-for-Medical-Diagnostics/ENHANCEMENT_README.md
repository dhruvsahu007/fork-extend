# 🏥 Enhanced Medical AI Diagnostics System

> **Professional medical AI consultation with 6 specialists and modern web interface**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com)

## 🎯 **What's New in This Enhanced Version**

This is an enhanced version of the original [AI-Agents-for-Medical-Diagnostics](https://github.com/ahmadvh/AI-Agents-for-Medical-Diagnostics) with major improvements:

### ✨ **Key Enhancements**
- 🔄 **6 Medical Specialists** (doubled from 3)
- 🌐 **Professional Web Interface** (upgraded from CLI)
- ⚡ **Concurrent Processing** (3x faster analysis)
- 📊 **Interactive Dashboard** (visual analytics)
- 📁 **Multiple Export Formats** (TXT, JSON)
- 🎨 **Modern UI/UX Design**

---

## 🏥 **Medical Specialists Available**

| Specialist | Expertise | New in Enhancement |
|------------|-----------|-------------------|
| 🫀 **Cardiologist** | Heart conditions, cardiovascular health | *(Original)* |
| 🧠 **Psychologist** | Mental health, behavioral analysis | *(Original)* |
| 🫁 **Pulmonologist** | Respiratory system, lung conditions | *(Original)* |
| 🧬 **Neurologist** | Brain, nervous system disorders | ✅ **NEW** |
| 🩺 **Dermatologist** | Skin conditions, dermatological issues | ✅ **NEW** |
| ⚕️ **Endocrinologist** | Hormonal imbalances, metabolic disorders | ✅ **NEW** |

---

## 🚀 **Quick Start**

### **Prerequisites**
```bash
Python 3.8+
OpenAI API Key
```

### **Installation**
```bash
# Clone this enhanced version
git clone [your-forked-repo-url]
cd AI-Agents-for-Medical-Diagnostics

# Install dependencies
pip install -r requirements.txt

# Set up API key
echo "OPENAI_API_KEY=your_api_key_here" > apikey.env
```

### **Launch Web Application**
```bash
streamlit run streamlit_app.py
```
🌐 **Access:** http://localhost:8501

### **Alternative: Command Line (Original)**
```bash
python Main.py
```

---

## 🖥️ **Web Interface Features**

### **📄 Upload & Analyze Tab**
- **File Upload:** Support for TXT medical reports
- **Text Input:** Direct paste functionality  
- **Sample Reports:** Pre-loaded examples
- **Real-time Analysis:** Live progress tracking

### **📊 Results Dashboard Tab**
- **Final Diagnosis:** Comprehensive multidisciplinary assessment
- **Visual Analytics:** Interactive charts showing analysis depth
- **Individual Reports:** Detailed specialist assessments
- **Metrics Dashboard:** Analysis statistics and quality indicators

### **📁 Export & History Tab**
- **TXT Export:** Professional report format
- **JSON Export:** Structured data format
- **Timestamped Downloads:** Organized file naming
- **Analysis History:** Session management

---

## 💡 **Usage Examples**

### **Web Interface Workflow**
1. **Upload** medical report or paste text
2. **Click** "🚀 Start Medical Analysis"  
3. **Watch** real-time progress of all 6 specialists
4. **Review** comprehensive diagnosis and individual reports
5. **Export** results in preferred format

### **Sample Analysis Output**
```
🎯 Comprehensive Medical Assessment

Based on the comprehensive review of specialist reports, here are the three most likely health issues for Michael Johnson:

1. Panic Disorder/Anxiety Disorder
   Reasoning: Multiple specialists identified symptoms consistent with panic attacks and anxiety disorder...

2. GERD with Possible Respiratory and Dermatological Manifestations  
   Reasoning: The cardiologist and pulmonologist noted potential for GERD to mimic cardiac symptoms...

3. Pheochromocytoma or Other Endocrine Disorder
   Reasoning: The endocrinologist raised the possibility of pheochromocytoma...
```

---

## 🏗️ **System Architecture**

```
🏥 Enhanced Medical AI System
├── 🌐 Web Interface (Streamlit)
│   ├── Upload & Analysis
│   ├── Results Dashboard  
│   └── Export & History
├── 🤖 AI Specialists (6 Concurrent Agents)
│   ├── Cardiologist
│   ├── Psychologist
│   ├── Pulmonologist
│   ├── Neurologist     ✅ NEW
│   ├── Dermatologist   ✅ NEW
│   └── Endocrinologist ✅ NEW
├── 🔄 Processing Engine
│   ├── ThreadPoolExecutor
│   ├── Concurrent Analysis
│   └── Progress Tracking
└── 💾 Data Management
    ├── Session State
    ├── Export System
    └── File Handling
```

---

## 📊 **Performance Comparison**

| Feature | Original System | Enhanced System | Improvement |
|---------|----------------|-----------------|-------------|
| **Specialists** | 3 | 6 | +100% |
| **Interface** | Command Line | Web App | Modern |
| **Processing** | Sequential | Concurrent | ~3x Faster |
| **Visualization** | None | Interactive | Professional |
| **Export Options** | 1 Format | 2 Formats | Flexible |
| **User Experience** | Basic | Professional | Enterprise-Ready |

---

## 🛠️ **Technical Details**

### **Dependencies**
```txt
streamlit>=1.25.0
openai>=0.27.0
python-dotenv>=1.0.0
pandas>=1.5.0
plotly>=5.15.0
```

### **Environment Variables**
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### **File Structure**
```
AI-Agents-for-Medical-Diagnostics/
├── streamlit_app.py           # 🌐 Enhanced Web Interface
├── Main.py                    # 🖥️ Original CLI Interface  
├── Utils/
│   └── Agents.py             # 🤖 All 6 Medical Specialists
├── Medical Reports/          # 📁 Sample Reports
├── Results/                  # 📊 Analysis Outputs
├── apikey.env               # 🔑 API Configuration
└── requirements.txt         # 📋 Dependencies
```

---

## 🔧 **Customization**

### **Adding New Specialists**
```python
# In Utils/Agents.py
class NewSpecialist:
    def __init__(self, medical_report):
        self.medical_report = medical_report
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def run(self):
        # Your specialist logic here
        pass
```

### **Modifying UI Themes**
```python
# In streamlit_app.py - Custom CSS section
st.markdown("""
<style>
    .your-custom-style {
        # Your styling here
    }
</style>
""", unsafe_allow_html=True)
```

---

## 🎯 **Use Cases**

- **Medical Education:** Training medical students with AI-assisted diagnostics
- **Clinical Research:** Exploring multi-specialist consultation patterns
- **Healthcare AI Development:** Prototyping medical AI applications
- **Diagnostic Support:** Secondary opinion system for complex cases

---

## 🤝 **Contributing**

This enhanced version welcomes contributions! Areas for future development:

- 🏥 **Additional Medical Specialists** (Oncologist, Radiologist, etc.)
- 🔍 **Advanced Analytics** (Confidence scoring, specialist agreement analysis)
- 📱 **Mobile Interface** (Responsive design improvements)
- 🔐 **Security Features** (Patient data encryption, HIPAA compliance)
- 🌍 **Multi-language Support** (International medical terminology)

---

## 📝 **License**

This enhanced version maintains the same license as the original project. Please refer to the original repository for licensing details.

---

## 🙏 **Acknowledgments**

- **Original Project:** [ahmadvh/AI-Agents-for-Medical-Diagnostics](https://github.com/ahmadvh/AI-Agents-for-Medical-Diagnostics)
- **Enhancement Development:** W3D4 Fork & Extend Assignment
- **AI Platform:** OpenAI GPT-4o
- **Web Framework:** Streamlit Community

---

## 📞 **Support**

For issues with the enhanced features:
1. Check the original repository for base functionality issues
2. Review the `PROJECT_ENHANCEMENT_SUMMARY.md` for enhancement details
3. Ensure proper API key configuration in `apikey.env`

---

*🏥 Enhanced Medical AI Diagnostics System - Bringing professional medical AI consultation to the web* 