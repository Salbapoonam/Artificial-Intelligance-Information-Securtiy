class MedicalExpertSystem:
    def __init__(self):
        self.fever = False
        self.cough = False
        self.breathing_difficulty = False
        self.sore_throat = False
        self.fatigue = False
        self.headache = False
        self.body_ache = False
        self.diarrhea = False
        self.vomiting = False
        self.loss_of_smell_taste = False
        self.travel_history = False
        self.contact_with_patient = False

    def evaluate(self):
        if self.fever and self.cough and self.breathing_difficulty:
            return "You may have COVID-19. Please contact your healthcare provider for further instructions."
        elif self.fever and self.sore_throat and self.body_ache and self.fatigue:
            return "You may have the flu. Please contact your healthcare provider for further instructions."
        elif self.vomiting and self.diarrhea and self.fever and self.body_ache:
            return "You may have gastroenteritis. Please contact your healthcare provider for further instructions."
        elif self.loss_of_smell_taste and self.headache and self.sore_throat:
            return "You may have a sinus infection. Please contact your healthcare provider for further instructions."
        elif self.travel_history or self.contact_with_patient:
            return "You may have been exposed to an infectious disease. Please contact your healthcare provider for further instructions."
        else:
            return "Your symptoms do not match any known infectious diseases. However, if you have concerns about your health, please contact your healthcare provider."

    def ask_question(self, symptom):
        print("Do you have the following symptom? (yes or no):", symptom)
        answer = input().lower()
        if answer == "yes":
            setattr(self, symptom, True)
        elif answer == "no":
            setattr(self, symptom, False)
        else:
            print("Invalid response, please enter 'yes' or 'no'")
            self.ask_question(symptom)

if __name__ == "__main__":
    es = MedicalExpertSystem()

    es.ask_question("fever")
    es.ask_question("cough")
    es.ask_question("breathing_difficulty")
    es.ask_question("sore_throat")
    es.ask_question("fatigue")
    es.ask_question("headache")
    es.ask_question("body_ache")
    es.ask_question("diarrhea")
    es.ask_question("vomiting")
    es.ask_question("loss_of_smell_taste")
    es.ask_question("travel_history")
    es.ask_question("contact_with_patient")

    print("Evaluation result:", es.evaluate())
