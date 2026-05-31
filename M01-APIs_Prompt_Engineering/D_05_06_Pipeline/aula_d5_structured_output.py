import os
from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Initialize our secure workspace shield
load_dotenv()

# ==============================================================================
# PYDANTIC DATA CONTRACT (The Firewall Blueprint)
# ==============================================================================
class SEOValidationReport(BaseModel):
    suggested_title: str = Field(
        description="An optimized, click-worthy SEO title under 60 characters."
    )
    primary_keywords: List[str] = Field(
        description="A list of the top 3 high-value technical keywords extracted from the text."
    )
    readability_score: int = Field(
        description="An objective readability score from 1 to 100 based on structural complexity."
    )
    improvement_justification: str = Field(
        description="A concise technical explanation of why these modifications improve indexing."
    )

# ==============================================================================
# STRUCTURED ENGINE EXECUTION
# ==============================================================================
def extract_structured_metadata(raw_content: str) -> str:
    # Implicitly grabs GEMINI_API_KEY from memory
    client = genai.Client()
    
    print("🧠 Forcing Gemini to bind its output matrix to the Pydantic Schema...")
    
    # We pass our Pydantic model directly into the response_schema configuration
    config = types.GenerateContentConfig(
        system_instruction="You are an elite MLOps Data Engineer. Analyze the input data and populate the schema exactly.",
        temperature=0.1,  # Low temperature guarantees strict compliance
        response_mime_type="application/json",
        response_schema=SEOValidationReport,
    )
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"Analyze this raw text:\n\n{raw_content}",
        config=config
    )
    
    # This is guaranteed to be 100% pure JSON matching our model keys exactly
    return response.text

if __name__ == "__main__":
    # Sample unformatted log/text simulation
    sample_text = """
    We just finished deploying our python isolation layer on our Linux Ubuntu workstation. 
    The script connected successfully to the local WordPress REST API and pushed a draft post with ID 11778. 
    We used standard environment variables to secure the application tokens and keep the global profile clean.
    """
    
    json_output = extract_structured_metadata(sample_text)
    
    print("\n" + "="*20 + " STRUCTURAL ENGINE REQUISIÇÃO CONCLUÍDA " + "="*20)
    print(json_output)
    print("="*80)