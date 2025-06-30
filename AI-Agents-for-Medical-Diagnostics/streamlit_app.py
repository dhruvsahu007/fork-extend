import streamlit as st
import pandas as pd
import plotly.express as px
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Import our medical agents
from Utils.Agents import Cardiologist, Psychologist, Pulmonologist, Neurologist, Dermatologist, Endocrinologist, MultidisciplinaryTeam

# Load environment variables
load_dotenv(dotenv_path='apikey.env')

# Page configuration
st.set_page_config(
    page_title="🏥 Medical AI Diagnostics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .agent-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #1f77b4;
    }
    .success-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
        border: 2px solid #28a745;
        box-shadow: 0 2px 8px rgba(40, 167, 69, 0.15);
        color: #155724;
        font-size: 16px;
        line-height: 1.6;
    }
    .success-card h4 {
        color: #155724;
        margin-bottom: 15px;
        font-weight: bold;
    }
    .warning-card {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'analysis_complete' not in st.session_state:
    st.session_state.analysis_complete = False
if 'agent_responses' not in st.session_state:
    st.session_state.agent_responses = {}
if 'final_diagnosis' not in st.session_state:
    st.session_state.final_diagnosis = ""

def run_agent_analysis(agent_name, agent):
    """Run individual agent analysis"""
    try:
        response = agent.run()
        return agent_name, response, "success"
    except Exception as e:
        return agent_name, f"Analysis failed: {str(e)}", "error"

def analyze_medical_report(medical_report):
    """Run all 6 medical agents concurrently"""
    
    # Create agents
    agents = {
        "🫀 Cardiologist": Cardiologist(medical_report),
        "🧠 Psychologist": Psychologist(medical_report), 
        "🫁 Pulmonologist": Pulmonologist(medical_report),
        "🧬 Neurologist": Neurologist(medical_report),
        "🩺 Dermatologist": Dermatologist(medical_report),
        "⚕️ Endocrinologist": Endocrinologist(medical_report)
    }
    
    # Progress tracking
    st.subheader("🏥 Medical Specialists Analysis")
    status_placeholder = st.empty()
    overall_progress = st.progress(0, text="Initializing medical analysis...")
    
    # Show agent status
    agent_status = {name: "⏳ Waiting..." for name in agents.keys()}
    
    def update_status_display():
        status_text = "**Analysis Status:**\n\n"
        for agent_name, status in agent_status.items():
            status_text += f"- {agent_name}: {status}\n"
        status_placeholder.markdown(status_text)
    
    update_status_display()
    
    # Run agents concurrently
    responses = {}
    completed_count = 0
    
    with ThreadPoolExecutor(max_workers=6) as executor:
        # Submit all agent tasks
        future_to_agent = {
            executor.submit(run_agent_analysis, name, agent): name 
            for name, agent in agents.items()
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_agent):
            agent_name, response, status = future.result()
            responses[agent_name] = response
            completed_count += 1
            
            # Update status
            if status == "success":
                agent_status[agent_name] = "✅ Complete!"
            else:
                agent_status[agent_name] = "❌ Failed"
            
            update_status_display()
            
            # Update overall progress
            progress_percent = completed_count / len(agents)
            overall_progress.progress(
                progress_percent, 
                text=f"Medical Analysis Progress: {completed_count}/{len(agents)} specialists complete"
            )
    
    # Final team analysis
    st.subheader("🏆 Multidisciplinary Team Analysis")
    team_progress = st.empty()
    
    team_progress.info("🔄 Multidisciplinary team is synthesizing all specialist reports...")
    
    try:
        # Clean agent names for team analysis (remove emojis)
        clean_responses = {
            name.split()[-1]: response 
            for name, response in responses.items()
        }
        
        team_agent = MultidisciplinaryTeam(
            cardiologist_report=clean_responses["Cardiologist"],
            psychologist_report=clean_responses["Psychologist"], 
            pulmonologist_report=clean_responses["Pulmonologist"],
            neurologist_report=clean_responses["Neurologist"],
            dermatologist_report=clean_responses["Dermatologist"],
            endocrinologist_report=clean_responses["Endocrinologist"]
        )
        
        final_diagnosis = team_agent.run()
        
        team_progress.success("✅ Multidisciplinary team analysis complete!")
        overall_progress.progress(1.0, text="🎉 Complete medical analysis finished!")
        
        return responses, final_diagnosis
        
    except Exception as e:
        team_progress.error(f"❌ Team analysis failed: {str(e)}")
        return responses, f"Team analysis failed: {str(e)}"

def create_analysis_summary(responses, final_diagnosis):
    """Create visual summary of the analysis"""
    
    # Create metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("👨‍⚕️ Specialists Consulted", "6", "100% Coverage")
    with col2:
        st.metric("🔬 Analysis Type", "AI-Powered", "Advanced")
    with col3:
        st.metric("⏱️ Analysis Time", "~2-3 min", "Concurrent")
    with col4:
        st.metric("📊 Report Quality", "Comprehensive", "Multi-perspective")
    
    # Create specialist response chart
    st.subheader("📈 Specialist Analysis Overview")
    
    # Count words in each response as a proxy for analysis depth
    analysis_data = []
    for agent_name, response in responses.items():
        word_count = len(str(response).split()) if response else 0
        analysis_data.append({
            "Specialist": agent_name,
            "Analysis Depth (Words)": word_count,
            "Status": "✅ Complete" if word_count > 10 else "⚠️ Limited"
        })
    
    df = pd.DataFrame(analysis_data)
    
    # Create bar chart
    fig = px.bar(
        df, 
        x="Specialist", 
        y="Analysis Depth (Words)",
        color="Status",
        title="Medical Specialist Analysis Depth",
        color_discrete_map={"✅ Complete": "#28a745", "⚠️ Limited": "#ffc107"}
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def main():
    # Header
    st.markdown("<h1 class='main-header'>🏥 Advanced Medical AI Diagnostics System</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #666;'>6 AI Specialists • Concurrent Analysis • Comprehensive Diagnosis</h3>", unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 System Information")
        st.info("**AI Specialists Available:**\n- 🫀 Cardiologist\n- 🧠 Psychologist\n- 🫁 Pulmonologist\n- 🧬 Neurologist\n- 🩺 Dermatologist\n- ⚕️ Endocrinologist")
        
        st.header("📁 Sample Reports")
        if st.button("📋 Load Sample Report"):
            try:
                with open("Medical Reports/Medical Rerort - Michael Johnson - Panic Attack Disorder.txt", "r") as file:
                    sample_report = file.read()
                st.session_state.sample_report = sample_report
                st.success("Sample report loaded!")
            except FileNotFoundError:
                st.error("Sample report not found!")
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["📄 Upload & Analyze", "📊 Results Dashboard", "📁 Export & History"])
    
    with tab1:
        st.header("📄 Medical Report Analysis")
        
        # File upload or text input
        upload_method = st.radio("Choose input method:", ["📁 Upload File", "✏️ Paste Text", "📋 Use Sample"])
        
        medical_report = ""
        
        if upload_method == "📁 Upload File":
            uploaded_file = st.file_uploader(
                "Upload medical report", 
                type=['txt'],
                help="Currently supports TXT files"
            )
            if uploaded_file:
                medical_report = str(uploaded_file.read(), "utf-8")
        
        elif upload_method == "✏️ Paste Text":
            medical_report = st.text_area(
                "Paste medical report here:",
                height=200,
                placeholder="Paste the medical report content here..."
            )
        
        elif upload_method == "📋 Use Sample":
            if 'sample_report' in st.session_state:
                medical_report = st.session_state.sample_report
                st.text_area("Sample medical report:", value=medical_report[:500] + "...", height=150, disabled=True)
            else:
                st.info("Click 'Load Sample Report' in the sidebar first!")
        
        # Analysis button
        if st.button("🚀 Start Medical Analysis", type="primary", disabled=not medical_report):
            if medical_report:
                st.session_state.analysis_complete = False
                
                with st.spinner("Initializing AI medical specialists..."):
                    time.sleep(1)  # Brief pause for UX
                
                # Run analysis
                responses, final_diagnosis = analyze_medical_report(medical_report)
                
                # Store results
                st.session_state.agent_responses = responses
                st.session_state.final_diagnosis = final_diagnosis
                st.session_state.analysis_complete = True
                st.session_state.analysis_timestamp = datetime.now()
                
                st.balloons()  # Celebration animation
                st.success("🎉 Medical analysis complete! Check the Results Dashboard tab.")
    
    with tab2:
        st.header("📊 Medical Analysis Results")
        
        if st.session_state.analysis_complete and st.session_state.agent_responses:
            # Analysis summary
            create_analysis_summary(st.session_state.agent_responses, st.session_state.final_diagnosis)
            
            # Detailed results
            st.subheader("🏆 Final Multidisciplinary Diagnosis")
            st.markdown(f"""
            <div class="success-card">
                <h4>🎯 Comprehensive Medical Assessment</h4>
                {st.session_state.final_diagnosis}
            </div>
            """, unsafe_allow_html=True)
            
            # Individual specialist reports
            st.subheader("👨‍⚕️ Individual Specialist Reports")
            
            col1, col2 = st.columns(2)
            
            specialist_list = list(st.session_state.agent_responses.items())
            
            for i, (agent_name, response) in enumerate(specialist_list):
                with col1 if i % 2 == 0 else col2:
                    with st.expander(f"{agent_name} Report", expanded=False):
                        st.write(response)
        
        else:
            st.info("📋 No analysis results yet. Please analyze a medical report first!")
    
    with tab3:
        st.header("📁 Export & Analysis History")
        
        if st.session_state.analysis_complete:
            # Export options
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📄 Export as TXT"):
                    export_content = f"""
# Medical AI Diagnosis Report
Generated: {st.session_state.analysis_timestamp.strftime('%Y-%m-%d %H:%M:%S')}

## Final Diagnosis
{st.session_state.final_diagnosis}

## Individual Specialist Reports
"""
                    for agent_name, response in st.session_state.agent_responses.items():
                        export_content += f"\n### {agent_name}\n{response}\n"
                    
                    st.download_button(
                        label="⬇️ Download TXT Report",
                        data=export_content,
                        file_name=f"medical_diagnosis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )
            
            with col2:
                if st.button("📊 Export as JSON"):
                    export_data = {
                        "timestamp": st.session_state.analysis_timestamp.isoformat(),
                        "final_diagnosis": st.session_state.final_diagnosis,
                        "specialist_reports": st.session_state.agent_responses
                    }
                    
                    st.download_button(
                        label="⬇️ Download JSON Report", 
                        data=json.dumps(export_data, indent=2),
                        file_name=f"medical_diagnosis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                        mime="application/json"
                    )
            
            with col3:
                if st.button("🔄 Clear Results"):
                    st.session_state.analysis_complete = False
                    st.session_state.agent_responses = {}
                    st.session_state.final_diagnosis = ""
                    st.rerun()
        
        else:
            st.info("📋 No results to export yet. Please complete an analysis first!")

if __name__ == "__main__":
    main() 