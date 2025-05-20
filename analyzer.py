import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text, job_description):
    prompt = f"""
You are a professional resume reviewer and career advisor.

Evaluate the following resume in the context of the job description provided. Provide a detailed, structured analysis covering the points below.

---

### Job Description:
{job_description}

### Resume Content:
{resume_text}

---

###  Return the following:
1. **ATS Score tailored to job description (out of 100)**  
   - Provide a numerical score.  
   - Clearly state the key factors contributing to the score (e.g., keyword match, formatting, experience alignment).  
   - Mention specific areas where the resume could improve to boost the ATS score.

2. ** SWOT Analysis** (in bullet points)  
   - Strengths  
   - Weaknesses  
   - Opportunities  
   - Threats

3. ** Top 5 Missing Keywords**  
   - Bullet points of important keywords missing from the resume that are present or implied in the job description.

4. ** Suggestions for Improvement**  
   - Actionable steps to enhance the resume's content, alignment with the job, and professionalism.

5. ** Formatting Tips**  
   - Advice on improving the layout, structure, and presentation of the resume.


6. ** Percentage Chances of getting selected for internship/job**
    - Calculate the chances of selection of the candidate based on the {resume_text} for the {job_description} based on the study made in SWOT Analysis and proper study of probabilities. Give some bullet points (Maximum 3) to improve in the resume to increase this percentage of getting selected for the job.


Keep the tone professional, direct, and easy to read. Use bullet points and short paragraphs where appropriate.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional resume reviewer and career advisor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    return response.choices[0].message.content
