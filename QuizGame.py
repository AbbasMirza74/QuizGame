def run_quiz():
    questions = [
        {
            "question": "Which is the fastest programming language?",
            "options": ["A. Python", "B. Java", "C. C", "D. Rust"],
            "answer": "C"
        },
        {
            "question": "Which programming language is known as the 'language of the web'?",
            "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
            "answer": "D"
        },
        {
            "question": "What is the time complexity for inserting an element in a balanced binary search tree?",
            "options": ["A. O(1)", "B. O(log n)", "C. O(n log n)", "D. O(n)"],
            "answer": "B"
        },
        {
            "question": "Which data structure uses the Last In First Out (LIFO) principle?",
            "options": ["A. Queue", "B. Stack", "C. Linked List", "D. Array"],
            "answer": "B"
        },
        {
            "question": "In which year was Python first released?",
            "options": ["A. 1991", "B. 1989", "C. 1995", "D. 2000"],
            "answer": "A"
        }
    ]
    
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        while True:
            user_answer = input("Enter your answer (A, B, C, or D): ").upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    print(f"\nQuiz finished! Your final score is {score}/{len(questions)}.")
    if score == len(questions):
        review = "Excellent!"
    elif score >= len(questions) * 0.75:
        review = "Good!"
    elif score >= len(questions) * 0.50:
        review = "Average!"
    else:
        review = "Poor!"
    
    print(f"Your performance review: {review}")

if __name__ == "__main__":
    run_quiz()
