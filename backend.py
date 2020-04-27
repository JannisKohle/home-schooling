id_meanings = {"AC": "Account", "CO": "Course", "EX": "Exercise",
               "EV": "Event", "SU": "Survey", "IN": "Invatation", "CH": "Chat"}

reverse_id_meanings = {v: k for k, v in zip(id_meanings.keys(), id_meanings.values())}


def create_id(type):  # type = 'Account' or 'Event' ...
    pass


class App():
    class Account():
        def __init__(self, name, password, id):
            self.name = name
            self.password = password
            self.id = id

    class Course():
        def __init__(self, name, id, teachers, students):
            self.name = name
            self.id = id
            self.teachers = teachers
            self.students = students

    class Exercise():
        def __init__(self, name, course, id, description, creator, for_students):
            self.name = name
            self.course = course
            self.id = id
            self.description = description
            self.creator = creator
            self.for_students = for_students

    class Event():
        def __init__(self, name, course, id, description, creator, for_people):
            self.name = name
            self.course = course
            self.id = id
            self.description = description
            self.creator = creator
            self.for_people = for_people

    class Survey():
        def __init__(self, name, course, id, description, creator, for_people):
            self.name = name
            self.course = course
            self.id = id
            self.description = description
            self.creator = creator
            self.for_people = for_people

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
