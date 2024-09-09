from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Таблиця для зв'язку студентів та курсів (Many-to-Many)
student_course = Table('student_course', Base.metadata,
Column('student_id', Integer, ForeignKey('students.id')),
Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=student_course, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', secondary=student_course, back_populates='courses')

# Створення бази даних
engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

# 2. Виконання базових операцій
# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()

# Додавання нового студента та курсу
def add_student(name):
    new_student = Student(name=name)
    session.add(new_student)
    session.commit()
    return new_student

def add_course(name):
    new_course = Course(name=name)
    session.add(new_course)
    session.commit()
    return new_course

# Додавання студента до курсу
def enroll_student_to_course(student_id, course_id):
    student = session.query(Student).filter_by(id=student_id).first()
    course = session.query(Course).filter_by(id=course_id).first()
    student.courses.append(course)
    session.commit()

# Приклад використання
student = add_student('John Doe')
course = add_course('Mathematics')
enroll_student_to_course(student.id, course.id)

# 3. Запити до бази даних
# Отримання студентів, зареєстрованих на певний курс
def get_students_in_course(course_id):
    course = session.query(Course).filter_by(id=course_id).first()
    return course.students

# Отримання курсів, на які зареєстрований певний студент
def get_courses_for_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    return student.courses

# Приклад використання
students_in_math = get_students_in_course(course.id)
courses_for_john = get_courses_for_student(student.id)


# 4. Оновлення та видалення даних
# Оновлення даних про студента
def update_student(student_id, new_name):
    student = session.query(Student).filter_by(id=student_id).first()
    student.name = new_name
    session.commit()

# Видалення студента з бази даних
def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    session.delete(student)
    session.commit()

# Приклад використання
update_student(student.id, 'Jane Doe')
delete_student(student.id)
