from chatbot import MedicalChatbot
from hospitals import get_hospitals
import re

def extract_specialty(reply_text):
    match = re.search(r"SPECIALTY:\s*(.+)", reply_text)
    if match:
        return match.group(1).strip()
    return None

def main():
    api_key = input("Enter your Groq API key: ")
    bot = MedicalChatbot(api_key)
    
    print("\n Medical Chatbot (type quit to exit)\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Bot: Take care!")
            break
        
        reply = bot.send_message(user_input)
        print(f"\nBot: {reply}\n")
        
        specialty = extract_specialty(reply)
        
        if specialty:
            city = input("Enter your city to find hospitals (or press Enter to skip): ")
            city = city if city.strip() else None
            
            hospitals = get_hospitals(specialty, city)
            
            if hospitals:
                print(f"\nRecommended hospitals for {specialty}:")
                for h in hospitals:
                    print(f"  - {h['name']} ({h['city']}) - {h['phone']}")
            else:
                print(f"\nNo hospitals found for {specialty} in {city}.")
            print()

if __name__ == "__main__":
    main()
