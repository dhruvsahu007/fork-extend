from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

class Agent:
    def __init__(self, medical_report=None, role=None, extra_info=None):
        self.medical_report = medical_report
        self.role = role
        self.extra_info = extra_info or {}
        # Initialize the prompt based on role and other info
        self.prompt_template = self.create_prompt_template()
        # Initialize the model
        self.model = ChatOpenAI(temperature=0, model="gpt-4o")

    def create_prompt_template(self):
        if self.role == "MultidisciplinaryTeam":
            # Handle the multidisciplinary team case
            template = f"""
                Act like a multidisciplinary team of healthcare professionals.
                You will receive medical analyses from 6 different specialists: Cardiologist, Psychologist, Pulmonologist, Neurologist, Dermatologist, and Endocrinologist.
                Task: Review all specialist reports, analyze them comprehensively, and come up with a list of 3 most likely health issues for the patient.
                Consider how different specialist findings might relate to each other and provide a holistic assessment.
                Return a list of bullet points of 3 possible health issues and for each issue provide the reasoning based on the specialist reports.
                
                Cardiologist Report: {self.extra_info.get('cardiologist_report', '')}
                Psychologist Report: {self.extra_info.get('psychologist_report', '')}
                Pulmonologist Report: {self.extra_info.get('pulmonologist_report', '')}
                Neurologist Report: {self.extra_info.get('neurologist_report', '')}
                Dermatologist Report: {self.extra_info.get('dermatologist_report', '')}
                Endocrinologist Report: {self.extra_info.get('endocrinologist_report', '')}
            """
            return PromptTemplate.from_template(template)
        else:
            # Handle individual specialist agents
            templates = {
                "Cardiologist": """
                    Act like a cardiologist. You will receive a medical report of a patient.
                    Task: Review the patient's cardiac workup, including ECG, blood tests, Holter monitor results, and echocardiogram.
                    Focus: Determine if there are any subtle signs of cardiac issues that could explain the patient's symptoms. Rule out any underlying heart conditions, such as arrhythmias or structural abnormalities, that might be missed on routine testing.
                    Recommendation: Provide guidance on any further cardiac testing or monitoring needed to ensure there are no hidden heart-related concerns. Suggest potential management strategies if a cardiac issue is identified.
                    Please only return the possible causes of the patient's symptoms and the recommended next steps.
                    Medical Report: {medical_report}
                """,
                "Psychologist": """
                    Act like a psychologist. You will receive a patient's report.
                    Task: Review the patient's report and provide a psychological assessment.
                    Focus: Identify any potential mental health issues, such as anxiety, depression, or trauma, that may be affecting the patient's well-being.
                    Recommendation: Offer guidance on how to address these mental health concerns, including therapy, counseling, or other interventions.
                    Please only return the possible mental health issues and the recommended next steps.
                    Patient's Report: {medical_report}
                """,
                "Pulmonologist": """
                    Act like a pulmonologist. You will receive a patient's report.
                    Task: Review the patient's report and provide a pulmonary assessment.
                    Focus: Identify any potential respiratory issues, such as asthma, COPD, or lung infections, that may be affecting the patient's breathing.
                    Recommendation: Offer guidance on how to address these respiratory concerns, including pulmonary function tests, imaging studies, or other interventions.
                    Please only return the possible respiratory issues and the recommended next steps.
                    Patient's Report: {medical_report}
                """,
                "Neurologist": """
                    Act like a neurologist. You will receive a patient's report.
                    Task: Review the patient's report and provide a neurological assessment.
                    Focus: Identify any potential neurological issues, such as headaches, dizziness, cognitive impairment, seizures, or nervous system disorders that may explain the patient's symptoms.
                    Recommendation: Suggest neurological tests such as MRI, CT scans, EEG, or neuropsychological testing. Provide guidance on potential treatments or referrals to neurology subspecialists.
                    Please only return the possible neurological causes and the recommended next steps.
                    Patient's Report: {medical_report}
                """,
                "Dermatologist": """
                    Act like a dermatologist. You will receive a patient's report.
                    Task: Review the patient's report and provide a dermatological assessment.
                    Focus: Identify any potential skin conditions, rashes, lesions, or dermatological manifestations of systemic diseases that may be relevant to the patient's symptoms.
                    Recommendation: Suggest dermatological examinations, biopsies, or treatments. Consider how skin conditions might relate to underlying medical conditions.
                    Please only return the possible dermatological issues and the recommended next steps.
                    Patient's Report: {medical_report}
                """,
                "Endocrinologist": """
                    Act like an endocrinologist. You will receive a patient's report.
                    Task: Review the patient's report and provide an endocrinological assessment.
                    Focus: Identify any potential hormonal imbalances, metabolic disorders, diabetes, thyroid issues, or endocrine system problems that may explain the patient's symptoms.
                    Recommendation: Suggest hormone level tests, glucose monitoring, thyroid function tests, or other endocrine evaluations. Provide guidance on metabolic management.
                    Please only return the possible endocrine causes and the recommended next steps.
                    Patient's Report: {medical_report}
                """
            }
            if self.role and self.role in templates:
                template = templates[self.role]
                return PromptTemplate.from_template(template)
            else:
                raise ValueError(f"Unknown role: {self.role}")
    
    def run(self):
        print(f"{self.role} is running...")
        prompt = self.prompt_template.format(medical_report=self.medical_report)
        try:
            response = self.model.invoke(prompt)
            return response.content
        except Exception as e:
            print("Error occurred:", e)
            return None

# Define specialized agent classes
class Cardiologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Cardiologist")

class Psychologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Psychologist")

class Pulmonologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Pulmonologist")

class Neurologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Neurologist")

class Dermatologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Dermatologist")

class Endocrinologist(Agent):
    def __init__(self, medical_report):
        super().__init__(medical_report, "Endocrinologist")

class MultidisciplinaryTeam(Agent):
    def __init__(self, cardiologist_report, psychologist_report, pulmonologist_report, 
                 neurologist_report, dermatologist_report, endocrinologist_report):
        extra_info = {
            "cardiologist_report": cardiologist_report,
            "psychologist_report": psychologist_report,
            "pulmonologist_report": pulmonologist_report,
            "neurologist_report": neurologist_report,
            "dermatologist_report": dermatologist_report,
            "endocrinologist_report": endocrinologist_report
        }
        super().__init__(role="MultidisciplinaryTeam", extra_info=extra_info)
