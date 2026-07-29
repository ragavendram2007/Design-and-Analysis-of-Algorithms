import random
import sys
import time
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Student:
    roll_no: int
    name: str
    marks: int

    def __repr__(self) -> str:
        return f"Roll No: {self.roll_no} | Name: {self.name} | Marks: {self.marks}"


def generate_students(n: int, start_roll: int = 21001) -> List[Student]:
    if n <= 0:
        raise ValueError("Number of students must be greater than 0")

    students: List[Student] = []
    roll = start_roll
    for i in range(1, n + 1):
        name = f"Student_{i}"
        marks = random.randint(35, 100)
        students.append(Student(roll, name, marks))
        roll += 1
    return students


def interpolation_search(students: List[Student], target_roll: int) -> Tuple[Optional[Student], int]:
    comparisons = 0
    if not students:
        return None, comparisons

    low, high = 0, len(students) - 1

    while low <= high and students[low].roll_no <= target_roll <= students[high].roll_no:
        comparisons += 1

        if low == high:
            if students[low].roll_no == target_roll:
                return students[low], comparisons
            return None, comparisons

        if students[high].roll_no == students[low].roll_no:
            if students[low].roll_no == target_roll:
                return students[low], comparisons
            return None, comparisons

        position = low + int(
            (target_roll - students[low].roll_no) * (high - low)
            / (students[high].roll_no - students[low].roll_no)
        )
        position = max(low, min(high, position))

        if students[position].roll_no == target_roll:
            return students[position], comparisons
        if students[position].roll_no < target_roll:
            low = position + 1
        else:
            high = position - 1

    return None, comparisons


def binary_search(students: List[Student], target_roll: int) -> Tuple[Optional[Student], int]:
    comparisons = 0
    low, high = 0, len(students) - 1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if students[mid].roll_no == target_roll:
            return students[mid], comparisons
        if students[mid].roll_no < target_roll:
            low = mid + 1
        else:
            high = mid - 1

    return None, comparisons


def show_student_stats(students: List[Student]) -> None:
    if not students:
        print("No student data available.")
        return

    marks = [student.marks for student in students]
    print("\nStudent Statistics")
    print("-" * 40)
    print(f"Total Students: {len(students)}")
    print(f"Highest Marks : {max(marks)}")
    print(f"Lowest Marks  : {min(marks)}")
    print(f"Average Marks : {sum(marks) / len(marks):.2f}")


def run_benchmark() -> None:
    sizes = [1000, 5000, 10000, 50000, 100000]
    iterations = 30

    print(f"\n{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} {'IS Comparisons':>16} {'BS Comparisons':>16}")
    print("-" * 85)

    for size in sizes:
        students = generate_students(size)
        target_roll = students[random.randint(0, size - 1)].roll_no

        start = time.perf_counter()
        for _ in range(iterations):
            interpolation_search(students, target_roll)
        is_time = (time.perf_counter() - start) / iterations * 1000

        start = time.perf_counter()
        for _ in range(iterations):
            binary_search(students, target_roll)
        bs_time = (time.perf_counter() - start) / iterations * 1000

        _, comp_is = interpolation_search(students, target_roll)
        _, comp_bs = binary_search(students, target_roll)

        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} {comp_is:>16} {comp_bs:>16}")


def read_input(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except EOFError:
        print("\nNo input received. Exiting gracefully.")
        raise SystemExit(0)


def search_demo(students: List[Student]) -> None:
    print("\nSearch Menu")
    print("-" * 40)
    print("1. Search for an existing roll number")
    print("2. Search for a missing roll number")
    print("3. Search for a custom roll number")
    print("4. Back")

    choice = read_input("Choose an option: ")

    if choice == "1":
        target_roll = students[7345].roll_no
        result, comps = interpolation_search(students, target_roll)
        print_result(target_roll, result, comps)
    elif choice == "2":
        target_roll = 99999
        result, comps = interpolation_search(students, target_roll)
        print_result(target_roll, result, comps)
    elif choice == "3":
        try:
            target_roll = int(read_input("Enter a roll number to search: "))
            result, comps = interpolation_search(students, target_roll)
            print_result(target_roll, result, comps)
        except ValueError:
            print("Please enter a valid integer.")
    else:
        print("Returning to main menu...")


def print_result(target_roll: int, result: Optional[Student], comps: int) -> None:
    if result:
        print(f"✅ Found roll {target_roll} in {comps} comparisons -> {result}")
    else:
        print(f"❌ Roll {target_roll} was not found ({comps} comparisons checked).")


def main() -> None:
    print("=" * 60)
    print("SMART ROLL NUMBER LOOKUP SYSTEM")
    print("=" * 60)

    random.seed(42)
    students = generate_students(10000)

    while True:
        print("\nMain Menu")
        print("-" * 40)
        print("1. Search Student")
        print("2. Show Student Statistics")
        print("3. Run Benchmark")
        print("4. Exit")

        choice = read_input("Choose an option: ")

        if choice == "1":
            search_demo(students)
        elif choice == "2":
            show_student_stats(students)
        elif choice == "3":
            run_benchmark()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()