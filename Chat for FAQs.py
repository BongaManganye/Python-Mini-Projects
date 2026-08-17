# Chat for FAQs

faqs = {
    "What is Lkibra Academy?": "Lkhibra Academy is an online learning platform.",
    "What courses are available?": "Python, Data Science, AI, and more!",
    "How do I enroll?": "Visit our website and sign up for a course."
}

while True:
    question = input("Ask a question: ")
    if question.lower() == "exit":
        break
    print(faqs.get(question, "Sorry, I don't understand that question."))
