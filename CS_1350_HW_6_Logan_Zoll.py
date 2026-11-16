from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def pay_stub(self):
        return f"{self.name} (ID: {self.employee_id}): ${self.calculate_pay():.2f}"

    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        raise ValueError(f"{name} can't be negative")


class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.validate_positive(annual_salary, "annual_salary")
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 24

    def description(self):
        return f"Salaried: {self.name}"


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.validate_positive(hourly_rate, "hourly_rate")
        self.validate_positive(hours_worked, "hours_worked")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        regular_hours = min(self.hours_worked, 40)
        overtime_hours = max(self.hours_worked - 40, 0)
        return (self.hourly_rate * regular_hours + self.hourly_rate * 1.5 * overtime_hours)

    def description(self):
        return f"Hourly: {self.name}"


class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id)
        self.validate_positive(base_salary, "base_salary")
        self.validate_positive(sales, "sales")
        self.validate_positive(commission_rate, "commission_rate")
        if commission_rate > 1.0:
            raise ValueError("can't be negative")
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def calculate_pay(self):
        return self.base_salary + (self.sales * self.commission_rate)

    def description(self):
        return f"Commission: {self.name}"


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_payroll(self):
        return sum(emp.calculate_pay() for emp in self.employees)

    def print_all_stubs(self):
        for emp in self.employees:
            print(emp.pay_stub())


if __name__ == "__main__":
    alice = SalariedEmployee("Alice Johnson", "E001", 84000)
    bob = HourlyEmployee("Bob Smith", "E002", 25.00, 45)
    carol = CommissionEmployee("Carol Davis", "E003", 2000, 50000, 0.05)

    print("Employee Descriptions:")
    for emp in [alice, bob, carol]:
        print(f"  {emp.description()}")

    print("\nPay Stubs:")
    for emp in [alice, bob, carol]:
        print(f"  {emp.pay_stub()}")

    payroll = Payroll()
    payroll.add_employee(alice)
    payroll.add_employee(bob)
    payroll.add_employee(carol)

    print(f"\nTotal Payroll: ${payroll.total_payroll():.2f}")

    print("\nTesting validation:")
    try:
        bad = SalariedEmployee("Bad", "E999", -50000)
    except ValueError as e:
        print(f"  Caught: {e}")

    try:
        bad = CommissionEmployee("Bad", "E999", 1000, 5000, 1.5)
    except ValueError as e:
        print(f"  Caught: {e}")






class Song:
    total_songs = 0

    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds
        Song.total_songs += 1

    def display(self):
        return f"{self.title} - {self.artist} ({self.format_duration(self.duration_seconds)})"

    @classmethod
    def from_string(cls, s):
        title, artist, duration = s.split(" | ")
        return cls(title, artist, cls.parse_duration(duration))

    @classmethod
    def get_total_songs(cls):
        return cls.total_songs

    @staticmethod
    def format_duration(seconds):
        return f"{seconds // 60}:{seconds % 60:02d}"

    @staticmethod
    def parse_duration(duration_str):
        minutes, seconds = duration_str.split(":")
        return int(minutes) * 60 + int(seconds)


class Playlist:
    total_playlists = 0

    def __init__(self, name):
        Playlist.total_playlists += 1
        self.playlist_id = f"PL_{Playlist.total_playlists:03d}"
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_duration(self):
        return sum(song.duration_seconds for song in self.songs)

    def display(self):
        return (f"Playlist: {self.name} ({len(self.songs)} songs, "
                f"{Song.format_duration(self.total_duration())})")

    @classmethod
    def get_total_playlists(cls):
        return cls.total_playlists


class LibraryManager:
    @staticmethod
    def create_playlist_from_strings(name, song_strings):
        playlist = Playlist(name)
        for s in song_strings:
            playlist.add_song(Song.from_string(s))
        return playlist

    @staticmethod
    def format_library_report(playlists):
        lines = ["Library Report"]
        total_songs = 0
        for playlist in playlists:
            lines.append(f"Playlist: {playlist.name}")
            for i, song in enumerate(playlist.songs, start=1):
                lines.append(f"  {i}. {song.display()}")
            lines.append(f"  Duration: {Song.format_duration(playlist.total_duration())}")
            lines.append("")
            total_songs += len(playlist.songs)
        lines.append(f"Total Songs: {total_songs}")
        lines.append("")
        return "\n".join(lines)


if __name__ == "__main__":
    print()
    s1 = Song("Bohemian Rhapsody", "Queen", 354)
    s2 = Song("Imagine", "John Lennon", 187)
    print("Individual Songs:")
    print(f"  {s1.display()}")
    print(f"  {s2.display()}")

    s3 = Song.from_string("Hotel California | Eagles | 6:31")
    print(f"  {s3.display()}")

    print(f"\nFormat 245 seconds: {Song.format_duration(245)}")
    print(f"Parse '4:05': {Song.parse_duration('4:05')} seconds")

    playlist = Playlist("Classic Rock")
    playlist.add_song(s1)
    playlist.add_song(s2)
    playlist.add_song(s3)
    print(f"\n{playlist.display()}")

    chill_songs = [
        "Weightless | Marconi Union | 8:09",
        "Electra | Airstream | 5:51",
        "Mellomaniac | DJ Shah | 7:34"
    ]
    chill = LibraryManager.create_playlist_from_strings("Chill Vibes", chill_songs)
    print(f"{chill.display()}")

    print(f"\n{LibraryManager.format_library_report([playlist, chill])}")

    print(f"Total songs created: {Song.get_total_songs()}")
    print(f"Total playlists created: {Playlist.get_total_playlists()}")





class GradeBook:
    def __init__(self, course_name):
        self.course_name = course_name
        self._grades = {}

    def __str__(self):
        return f"GradeBook: {self.course_name} ({len(self)} students)"

    def __repr__(self):
        return f"GradeBook('{self.course_name}')"

    def __len__(self):
        return len(self._grades)

    def __getitem__(self, student):
        if student not in self._grades:
            raise KeyError(student)
        return self._grades[student]

    def __setitem__(self, student, grade):
        if not 0 <= grade <= 100:
            raise ValueError("Must be between 0 and 100")
        self._grades[student] = grade

    def __contains__(self, student):
        return student in self._grades

    def __iter__(self):
        return iter(self._grades)

    def __bool__(self):
        return len(self._grades) > 0

    @property
    def average(self):
        if not self._grades:
            return 0.0
        return sum(self._grades.values()) / len(self._grades)

    def __add__(self, other):
        result = GradeBook(f"{self.course_name} + {other.course_name}")
        for student in self:
            result[student] = self[student]
        for student in other:
            if student not in result or other[student] > result[student]:
                result[student] = other[student]
        return result

    def __iadd__(self, other):
        for student in other:
            if student not in self or other[student] > self[student]:
                self[student] = other[student]
        return self

    def __mul__(self, factor):
        result = GradeBook(f"{self.course_name} (curved)")
        for student in self:
            result[student] = min(100, round(self[student] * factor, 2))
        return result

    def __eq__(self, other):
        return abs(self.average - other.average) < 0.01

    def __lt__(self, other):
        return self.average < other.average

    def __le__(self, other):
        return self.average < other.average or self == other

if __name__ == "__main__":
    print()
    cs101 = GradeBook("CS 101")

    cs101["Alice"] = 92
    cs101["Bob"] = 78
    cs101["Carol"] = 88
    cs101["David"] = 95

    print(cs101)
    print(repr(cs101))

    print(f"Alice's grade: {cs101['Alice']}")

    print(f"Bob enrolled? {'Bob' in cs101}")
    print(f"Eve enrolled? {'Eve' in cs101}")

    print(f"Class size: {len(cs101)}")

    print("Students:")
    for student in cs101:
        print(f"  {student}: {cs101[student]}")

    empty = GradeBook("Empty")
    print(f"cs101 has students? {bool(cs101)}")
    print(f"empty has students? {bool(empty)}")

    print("\nValidation test:")
    try:
        cs101["Eve"] = 150
    except ValueError as e:
        print(f"  Caught: {e}")

    print("\n=== Part B: Arithmetic ===")
    math201 = GradeBook("Math 201")
    math201["Alice"] = 85
    math201["Bob"] = 90
    math201["Eve"] = 76

    combined = cs101 + math201
    print(f"\n{combined}")
    print("Merged grades:")
    for student in combined:
        print(f"  {student}: {combined[student]}")

    curved = math201 * 1.1
    print(f"\n{curved}")
    print("Curved grades:")
    for student in curved:
        print(f"  {student}: {curved[student]}")

    big_curve = math201 * 1.5
    print(f"\nBig curve — Bob's grade: {big_curve['Bob']}")

    print(f"CS 101 average: {cs101.average:.2f}")
    print(f"Math 201 average: {math201.average:.2f}")
    print(f"CS 101 == Math 201? {cs101 == math201}")
    print(f"Math 201 < CS 101? {math201 < cs101}")
    print(f"Math 201 <= CS 101? {math201 <= cs101}")

    classes = [math201, cs101, curved]
    classes.sort()
    print("\nSorted by average:")
    for gb in classes:
        print(f"  {gb} — avg: {gb.average:.2f}")
