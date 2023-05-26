# I will implement an expert system for employee performance evaluation using the rule-based approach.

# The rules for this system are based on the following factors:

# Attendance
# Punctuality
# Communication skills
# Job knowledge
# Quality of work
# Initiative
# Adaptability
# Dependability
class ExpertSystem:
    def __init__(self):
        self.attendance = 0
        self.punctuality = 0
        self.communication = 0
        self.job_knowledge = 0
        self.quality = 0
        self.initiative = 0
        self.adaptability = 0
        self.dependability = 0

    def evaluate(self):
        if self.attendance < 70:
            return "Poor attendance"
        elif self.punctuality < 70:
            return "Poor punctuality"
        elif self.communication < 70:
            return "Poor communication skills"
        elif self.job_knowledge < 70:
            return "Lack of job knowledge"
        elif self.quality < 70:
            return "Poor quality of work"
        elif self.initiative < 70:
            return "Lack of initiative"
        elif self.adaptability < 70:
            return "Lack of adaptability"
        elif self.dependability < 70:
            return "Lack of dependability"
        else:
            return "Excellent performance"

    def ask_question(self, factor):
        print("Please rate your performance for the following factor (out of 100):", factor)
        rating = int(input())
        if rating < 0 or rating > 100:
            print("Invalid rating, please enter a number between 0 and 100")
            self.ask_question(factor)
        else:
            setattr(self, factor, rating)

if __name__ == "__main__":
    es = ExpertSystem()

    es.ask_question("attendance")
    es.ask_question("punctuality")
    es.ask_question("communication")
    es.ask_question("job_knowledge")
    es.ask_question("quality")
    es.ask_question("initiative")
    es.ask_question("adaptability")
    es.ask_question("dependability")

    print("Evaluation result:", es.evaluate())
