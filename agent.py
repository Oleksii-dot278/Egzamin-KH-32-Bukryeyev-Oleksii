import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod


from google_adk import Agent, tool 

load_dotenv()



class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    @abstractmethod
    def get_role(self) -> str:
        pass

class Student(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__grades = [] 
        
    def add_grade(self, grade: float):
        self.__grades.append(grade)
        
    def average(self) -> float:
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)
        
    def min_grade(self) -> float:
        if not self.__grades:
            return 0.0
        return min(self.__grades)
        
    def max_grade(self) -> float:
        if not self.__grades:
            return 0.0
        return max(self.__grades)
        
    def get_role(self) -> str:
        return f"Student (Name: {self.name})"

class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject
        
    def get_role(self) -> str:
        return f"Teacher of {self.subject}"
        
    def evaluate(self, student: Student, grade: float):
        student.add_grade(grade)




@tool
def calculate_grade(name: str, scores: list[float]) -> dict:
    """
    Інструмент для розрахунку успішності.
    Приймає ім'я студента та список його оцінок.
    Повертає словник зі статистикою та літерною оцінкою.
    """
    student = Student(name=name, age=18)
    
    for score in scores:
        student.add_grade(score)
        
    avg = student.average()
    min_g = student.min_grade()
    max_g = student.max_grade()
    
    if avg >= 90:
        letter = "A"
    elif avg >= 75:
        letter = "B"
    elif avg >= 60:
        letter = "C"
    else:
        letter = "F"
        
    return {
        "student": student.name,
        "average": round(avg, 2),
        "min": min_g,
        "max": max_g,
        "letter_grade": letter
    }



SYSTEM_PROMPT = """
Ти є освітнім асистентом. Твоє завдання — використовувати інструмент calculate_grade 
для розрахунку середнього бала та визначення рейтингу студента. 
На основі отриманих результатів давай поради щодо покращення успішності. 
Відповідай завжди українською мовою. Будь ввічливим та мотивуючим.
"""


root_agent = Agent(
    name="StudentSuccessAgent",
    instructions=SYSTEM_PROMPT,
    tools=[calculate_grade]
)
