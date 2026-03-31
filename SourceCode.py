import json

# Knowledge base (enhanced responses)
responses = {

    "attendance": 
    "• Try to maintain at least 75% attendance, as it is mandatory in most colleges.\n"
    "• Low attendance can lead to being debarred from exams.\n"
    "• Attending classes regularly also helps in better understanding concepts.\n"
    "• Tip: Even if you miss classes, make sure to cover those topics the same day.",


    "exam": 
    "• Avoid last-minute preparation. Start early and stay consistent.\n"
    "• Focus on understanding concepts instead of rote learning.\n"
    "• Practice previous year questions and important topics.\n"
    "• During exams:\n"
    "  - Manage your time properly\n"
    "  - Attempt easy questions first\n"
    "  - Stay calm and confident",


    "cgpa": 
    "• Focus on internal marks (assignments, quizzes, attendance).\n"
    "• Study regularly instead of just before exams.\n"
    "• Try to improve each subject step by step.\n"
    "• Even a small increase in each subject can boost overall CGPA.",


    "assignment": 
    "• Complete assignments on time — they carry important marks.\n"
    "• Don’t just copy, try to understand what you are writing.\n"
    "• Keep your work neat and well-presented.\n"
    "• Tip: Start early to avoid last-minute stress.",


    "placement": 
    "• Start preparation early, don’t wait for final year.\n"
    "• Focus on:\n"
    "  - Technical skills (coding, core subjects)\n"
    "  - Communication skills\n"
    "  - Projects and internships\n"
    "• Practice aptitude and coding regularly.\n"
    "• Mock interviews can help build confidence.",


    "python": 
    "• To improve Python skills, focus on these core topics:\n"
    "  - Variables and Data Types\n"
    "  - Loops (for, while)\n"
    "  - Functions\n"
    "  - Lists, Tuples, Dictionaries\n"
    "  - File Handling\n"
    "• Practice small programs daily.\n"
    "• Try building mini projects like calculator, chatbot, etc.\n"
    "• Consistency is more important than speed.",


    "stress": 
    "• Stress is normal, especially during exams.\n"
    "• Try these activities to reduce stress:\n"
    "  - Take short breaks between study sessions\n"
    "  - Go for a walk or do light exercise\n"
    "  - Listen to music\n"
    "  - Talk to friends or family\n"
    "  - Practice deep breathing\n"
    "• Avoid overthinking and focus on one task at a time.",


    "time management": 
    "• Divide your day into time blocks:\n"
    "  - Morning: Study difficult subjects (2–3 hours)\n"
    "  - Afternoon: Practice and revision (2 hours)\n"
    "  - Evening: Light study or assignments (1–2 hours)\n"
    "• Take short breaks (5–10 minutes) after every 1 hour of study.\n"
    "• Prioritize important tasks first.\n"
    "• Avoid distractions like excessive phone usage.\n"
    "• A simple timetable can make a big difference.",


    "motivation": 
    "• Motivation may not always stay, but discipline will.\n"
    "• Focus on consistency rather than perfection.\n"
    "• Remember:\n"
    "  - 'Small steps every day lead to big results.'\n"
    "  - 'Your future depends on what you do today.'\n"
    "  - 'Don’t stop when you’re tired, stop when you’re done.'\n"
    "• Keep reminding yourself why you started.",


    "sleep": 
    "• Try to get at least 6–8 hours of sleep daily.\n"
    "• Effects of proper sleep:\n"
    "  - Better concentration\n"
    "  - Improved memory\n"
    "  - Better mood\n"
    "• Lack of sleep can cause:\n"
    "  - Low focus\n"
    "  - Stress and fatigue\n"
    "• Avoid using phone before sleep for better rest.",


    "health": 
    "• Good health is very important for academic performance.\n"
    "• Follow these basic tips:\n"
    "  - Eat balanced meals\n"
    "  - Stay hydrated\n"
    "  - Exercise regularly (even 15–20 minutes is enough)\n"
    "  - Avoid junk food regularly\n"
    "• Take care of both physical and mental health.",


    "friends": 
    "• Friends play an important role in college life.\n"
    "• Good friends can motivate and support you.\n"
    "• Be careful of peer pressure:\n"
    "  - Positive: Encourages growth and improvement\n"
    "  - Negative: Leads to distractions and bad habits\n"
    "• Choose friends who support your goals.",


    "goal": 
    "• Having a goal gives direction to your efforts.\n"
    "• Examples:\n"
    "  - Improving CGPA\n"
    "  - Learning a new skill\n"
    "  - Getting placed in a good company\n"
    "• Break your goal into smaller steps.\n"
    "• Track your progress regularly.",


    "failure": 
    "• Failure is not the end, it is part of the learning process.\n"
    "• Learn from your mistakes and improve.\n"
    "• Remember:\n"
    "  - 'Failure is the stepping stone to success.'\n"
    "  - 'Every expert was once a beginner.'\n"
    "• Don’t lose confidence, keep trying.",


    "confidence": 
    "• Confidence comes from preparation and practice.\n"
    "• Avoid both extremes:\n"
    "  - Underconfidence → self-doubt\n"
    "  - Overconfidence → careless mistakes\n"
    "• Stay balanced and believe in your abilities.\n"
    "• The more you practice, the more confident you become."
}

history = []

# Save history
def save_history():
    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)

# View history
def view_history():
    try:
        with open("history.json", "r") as f:
            data = json.load(f)
            print("\n📜 Chat History:\n")
            for item in data:
                print("You:", item["user"])
                print("Bot:", item["bot"])
                print()
    except:
        print("No history found.")

# Chatbot
def chatbot():
    print("\n🤖 Welcome to Student Help Chatbot")
    print("Type 'help' to see topics or 'exit' to go back to menu.\n")

    try:
        while True:
            user_input = input("You: ").lower()

            if user_input == "exit":
                print("Bot: Returning to main menu...\n")
                break

            elif user_input == "help":
                print("\nAvailable topics:")
                for key in responses.keys():
                    print("-", key)
                print()

            else:
                found = False
                for key in responses:
                    if key in user_input:
                        reply = responses[key]
                        print("Bot:\n", reply)
                        history.append({"user": user_input, "bot": reply})
                        save_history()
                        found = True
                        break

                if not found:
                    reply = "Sorry, I don't understand that. Try 'help' to see topics."
                    print("Bot:", reply)
                    history.append({"user": user_input, "bot": reply})
                    save_history()

    finally:
        save_history()

# Main Menu
while True:
    print("\n===== MENU =====")
    print("1. Start Chatbot")
    print("2. View Chat History")
    print("3. Help")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        chatbot()

    elif choice == "2":
        view_history()

    elif choice == "3":
        print("\nThis chatbot helps students with academic and personal guidance.")
        print("Type keywords like 'exam', 'attendance', 'stress', 'motivation', etc.")

    elif choice == "4":
        print("Exiting program...")
        save_history()
        break

    else:
        print("Invalid choice. Try again.")
