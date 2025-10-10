# Quiz Game - Python Mini Project

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("\nWelcome to the Python Quiz Game!\n")
        for idx, q in enumerate(self.questions, 1):
            print(f"Q{idx}: {q.question}")
            for i, option in enumerate(q.options, 1):
                print(f"{i}. {option}")
            while True:
                try:
                    choice = int(input("Your answer (1-4): "))
                    if choice < 1 or choice > len(q.options):
                        print("Please enter a valid option (1-4).")
                        continue
                    break
                except ValueError:
                    print("Invalid input! Enter a number between 1-4.")
            if q.options[choice-1].lower() == q.answer.lower():
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q.answer}\n")
        self.show_result()

    def show_result(self):
        print(f"Your final score: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("🏆 Excellent! Perfect score!")
        elif self.score >= len(self.questions) // 2:
            print("👍 Good job! Keep practicing.")
        else:
            print("💡 Keep practicing to improve your score!")

# List of quiz questions
questions_list = [
    Question("Which keyword is used to define a function in Python?", 
             ["func", "def", "function", "define"], "def"),
    Question("What does OOP stand for?", 
             ["Object-Oriented Programming", "Open Online Programming", "Output Over Python", "Operator Object Process"], 
             "Object-Oriented Programming"),
    Question("Which operator is used for exponentiation in Python?", 
             ["^", "**", "%", "//"], "**"),
    Question("Which data type is immutable in Python?", 
             ["List", "Dictionary", "Tuple", "Set"], "Tuple"),
    Question("Which method adds an item to the end of a list?", 
             ["append()", "add()", "insert()", "extend()"], "append()")
]

# Start the quiz
quiz = Quiz(questions_list)
quiz.start()
