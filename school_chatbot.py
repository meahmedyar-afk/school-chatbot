# School Information FAQ Chatbot
# Author: Your Name
# Description: A rule-based chatbot that answers common school-related questions

def school_chatbot():
    print("🤖 Welcome to the School Information Chatbot")
    print("Type 'exit' or 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        # Greeting
        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I help you with school information?")

        # School timings
        elif "time" in user_input or "timing" in user_input:
            print("Bot: School timings are from 8:00 AM to 2:30 PM, Monday to Friday.")

        # Admissions
        elif "admission" in user_input or "apply" in user_input:
            print("Bot: Admissions are open from March to May. You can apply online or visit the school office.")

        # Fees
        elif "fee" in user_input or "fees" in user_input:
            print("Bot: The fee structure depends on the grade. Please contact the school office for exact details.")

        # Subjects
        elif "subject" in user_input or "courses" in user_input:
            print("Bot: We offer Math, Science, English, Computer Science, and Social Studies.")

        # Contact details
        elif "contact" in user_input or "phone" in user_input or "email" in user_input:
            print("Bot: You can contact us at +123-456-7890 or email school@example.com.")

        # Exit
        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day 😊")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I didn't understand that.")
            print("Bot: You can ask about timings, admissions, fees, subjects, or contact information.\n")


# Run the chatbot
if __name__ == "__main__":
    school_chatbot()
