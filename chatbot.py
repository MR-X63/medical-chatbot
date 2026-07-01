from groq import Groq

class MedicalChatbot:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.chat_history = []
        self.system_prompt = """You are a medical assistant chatbot. Your job:

1. Ask clarifying questions if symptoms are vague.
2. Once you have enough info, give a possible diagnosis (2-3 likely conditions, NOT certain).
3. Rate severity as: Mild, Moderate, or Serious.
4. Suggest which medical specialty to consult (e.g., General Physician, Cardiologist, ENT, Dermatologist, Neurologist, etc.)
5. ALWAYS end with: This is not a medical diagnosis. Please consult a real doctor.

Keep responses concise and clear. After giving the diagnosis, end your message with this exact tag on its own line:
SPECIALTY: <specialty name>
"""

    def send_message(self, user_message):
        self.chat_history.append({"role": "user", "content": user_message})

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": self.system_prompt}] + self.chat_history,
            max_tokens=1024
        )

        reply = response.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": reply})
        return reply
