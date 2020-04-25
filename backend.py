id_meanings = {"AC": "Account", "CO": "Course", "IN": "Invatation", "CH": "Chat"}

reverse_id_meanings = {v: k for k, v in zip(id_meanings.keys(), id_meanings.values())}


def create_id(type):  # type = 'Account' or 'Course' ...
    pass


class Account():
    def __init__(self, name, password, id):
        self.name = name
        self.password = password
        self.id = id


class Course():
    def __init__(self, name, id, teachers, students):  # chats generating in __init__()
        self.name = name
        self.id = id
        self.teachers = teachers
        self.students = students


class Invatation():
    def __init__(self, id, from_user, to_user, course, role):
        self.id = id
        self.from_user = from_user
        self.to_user = to_user
        self.course = course
        self.role = role


class Chat():
    def __init__(self, name, id, course, members):
        self.name = name
        self.id = id
        self.course = course
        self.members = members
