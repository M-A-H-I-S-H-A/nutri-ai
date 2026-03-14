from groq import Groq

client = Groq(api_key="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")

def analyze_health(profile, symptoms):

    prompt = f"""
You are a vitamin deficiency detection assistant.

User medical profile:
{profile}

User symptoms:
{symptoms}

Your task:
Determine the SINGLE most likely vitamin deficiency.

Rules:
- Return ONLY ONE deficiency
- Choose the most probable deficiency
- Do not list multiple options
- Do not explain
- Only output the vitamin name

Output format:

Deficiency:
Vitamin B12
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content                        

