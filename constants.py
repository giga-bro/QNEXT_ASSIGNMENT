from google.generativeai.types import HarmCategory, HarmBlockThreshold

GEMINI_API_KEY ="AIzaSyDu71baNdUWKxoQrDPTlJAb8U-vvGTtOE4"

SAFETY_OPTIONS = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

MODEL_NAME = "gemini-1.5-flash"

SYSTEM_PROMPT = """
You are a professional information extractor specializing in analyzing corporate financial transcripts. Your task is to process the following transcript and accurately extract key insights in JSON format. Identify and summarize essential points on financial performance, market dynamics, expansion plans, environmental risks, and any recent regulatory or policy changes. Ensure that your summaries are concise, directly related to the specified company, and formatted strictly according to the JSON structure provided below.
"""

INPUT_PROMPT = """
Read provided transcripts and extract key insights into the company’s financial performance, market dynamics, expansion plans, environmental risks, and any recent regulatory or policy changes.
Company Name: {company_name}
Transcript: {transcript_text}

Please respond with a JSON output structured as follows, using concise and accurate language:

{{
    "company_name": "{company_name}",
    "financial_performance": "SHORT SUMMARY OF FINANCIAL PERFORMANCE HERE",
    "market_dynamics": "SHORT SUMMARY OF MARKET DYNAMICS HERE",
    "expansion_plans": "SHORT SUMMARY OF EXPANSION PLANS HERE",
    "environmental_risks": "SHORT SUMMARY OF ENVIRONMENTAL RISKS HERE",
    "regulatory_or_policy_changes": "SHORT SUMMARY OF REGULATORY OR POLICY CHANGES HERE"
}}

Each field should contain a brief, clear summary based solely on the provided transcript text. Aim for precision and avoid including any information not directly related to the transcript content.
"""