""" 
    Спроектировать мини‑систему для школы, которая:
        хранит учеников, предметы и оценки (журнал);
        считает статистику по оценкам (средние баллы по предмету и ученику);
        отправляет уведомления (просто пишет в консоль) если средний бал по ученику становится < 3.5
        Требования:

        Разделить ответственность (отдельно: журнал, статистика, уведомления, мониторинг).
        Возможность добавлять новые типы уведомлений и алгоритмы статистики без изменения существующего кода.
        Высокоуровневые сервисы зависят от абстракций, а не от конкретных классов.
"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class Student:
    name: str
    student_id: int


@dataclass
class Grade:
    student: Student
    subject: str
    value_grade: float


class Statistics(ABC):
    @abstractmethod
    def get_average_grade(self, grades: list[float]) -> float: ...


class MeanStatistics(Statistics):
    def get_average_grade(self, grades: list[float]) -> float:
        return sum(grades) / len(grades)


@dataclass
class Journal:
    list_of_grades: list[Grade] = field(default_factory=list[Grade])

    def add_grade(self, student: Student, subject: str, value: float) -> None:
        grade = Grade(student, subject, value)
        self.list_of_grades.append(grade)

    def get_grades_by_student(self, student: Student) -> list[float]:
        result: list[float] = []

        for grade in self.list_of_grades:
            if grade.student == student:
                result.append(grade.value_grade)
        return result

    def get_subject_all_grades(self, subject: str) -> list[float]:
        result: list[float] = []

        for grade in self.list_of_grades:
            if grade.subject == subject:
                result.append(grade.value_grade)
        return result

    def get_students_list(self) -> list[Student]:
        result: list[Student] = []

        for grade in self.list_of_grades:
            if grade.student not in result:
                result.append(grade.student)
        return result
