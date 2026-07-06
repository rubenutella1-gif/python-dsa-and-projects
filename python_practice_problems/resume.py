from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# File name for PDF (it will save in your current folder)
pdf_file = "Rubenu_Tella_Resume.pdf"

# Create document
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Resume content
resume_content = """
<para align=center><b><font size=14>Rubenu Tella</font></b></para>
<para align=center>Nandigama, Andhra Pradesh | your-email@gmail.com | +91-XXXXXXXXXX | LinkedIn/GitHub</para>
<para spaceb=20></para>

<b>Career Objective</b><br/>
Enthusiastic and detail-oriented B.Tech IT graduate (2025, CGPA 8.2) seeking an entry-level role in software development or data/AI domains. 
Passionate about coding, problem-solving, and building innovative solutions. Strong foundation in Python, Web Development, and Databases, 
with hands-on project experience in Deep Learning and NLP.<br/><br/>

<b>Education</b><br/>
B.Tech in Information Technology<br/>
XYZ College of Engineering, Andhra Pradesh (2021–2025)<br/>
CGPA: 8.2/10<br/><br/>

<b>Technical Skills</b><br/>
- Programming: Python, Java (basics), HTML, CSS<br/>
- Libraries/Frameworks: Pandas, NumPy, Flask<br/>
- Databases: MySQL (basics)<br/>
- Cloud: AWS (beginner)<br/>
- Other Tools: Jupyter Notebook, Visual Studio Code, Git<br/><br/>

<b>Academic Project</b><br/>
Threat Detection for Live Event Safety using NLP and Deep Learning<br/>
- Developed a system to analyze live audio input and detect potential threats in real-time.<br/>
- Implemented Deep Learning (RNN, LSTM) models for speech and NLP analysis.<br/>
- Built a Flask-based web interface for real-time monitoring.<br/>
- Outcome: Improved accuracy of threat detection in noisy environments.<br/><br/>

<b>Internships & Certifications</b><br/>
- Cloud Computing Virtual Internship – AWS Academy, Eduskills<br/>
- AI-ML Virtual Internship – Google for Developers, India Edu Program<br/>
- Android Developer Virtual Internship – Google for Developers, India Edu Program<br/><br/>

<b>Achievements</b><br/>
- Successfully completed multiple online certifications in Python, AI-ML, and Cloud.<br/>
- Participated in college-level hackathons and technical seminars.<br/><br/>

<b>Strengths</b><br/>
- Quick learner with strong problem-solving ability.<br/>
- Good communication and teamwork skills.<br/>
- Adaptable to new technologies and environments.<br/><br/>

<b>Declaration</b><br/>
I hereby declare that the above information is true to the best of my knowledge and belief.<br/><br/>

Date: ____________<br/>
Place: ____________<br/><br/>

(Signature)<br/>
Rubenu Tella
"""

# Add content to PDF
story.append(Paragraph(resume_content, styles["Normal"]))
doc.build(story)

print(f"✅ Resume saved as {pdf_file}")