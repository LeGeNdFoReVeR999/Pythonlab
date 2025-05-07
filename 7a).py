class InvalidPercentageError(Exception):
    pass

class LessPercentageError(Exception):
    pass

class CheckPercentage:
    def __init__(self, cutoff, max_score):
        self.cutoff = cutoff
        self.max_score = max_score

    def enroll_student(self, name, percentage):
        try:
            if percentage < 0 or percentage > 100:
                raise InvalidPercentageError(
                    f"Invalid percentage for {name}: {percentage}%. Must be between 0 and 100."
                )
            elif percentage < self.cutoff:
                raise LessPercentageError(
                    f"{name} cannot enroll: percentage {percentage}% is less than the cutoff value {self.cutoff}%."
                )
            elif percentage > self.max_score:
                raise InvalidPercentageError(
                    f"{name} cannot enroll: percentage {percentage}% exceeds the maximum allowed {self.max_score}%."
                )
            else:
                print(f"{name} successfully enrolled with {percentage}%.")
        except (InvalidPercentageError, LessPercentageError) as e:
            print(f"Enrollment Error: {e}")

# --- Usage ---
cutoff_percentage = 50
max_score = 90

enrollment_checker = CheckPercentage(cutoff_percentage, max_score)

students = {
    "Anuj": 80,
    "Bhavik": 90,
    "Akash": 65,
    "David": 40,
    "Bob": 35,
    "Ethan": 5,
    "Sneha": 95   # This one exceeds max_score and will raise error
}

for name, percentage in students.items():
    enrollment_checker.enroll_student(name, percentage)
