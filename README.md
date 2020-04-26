# home-schooling

## Description:

This is a Home Schooling App built with Python and Electron.

## How to use it:

There is a desktop app. In the app you first have to choose a folder on your computer, in which you
clone all of your courses. You can even have subdirectories in that folder, for different areas.

There are accounts and courses. In a course you can have one of the two roles: teacher and student.
In courses, teachers can create exercises and the students can submit the solutions. If you want to
create a course, you have to upload a folder with all the content to the course. Other people in the
course can then clone the course or pull the newest changes to get it to their computer.

Cloning a course will create a course folder (the program asks you where) with two subdirectories:
submissions and content

### Things Teachers can do:

- invite students

- invite teachers

- change/add/delete folders and files

- see/correct students' solutions

- create new chat (there's automatically a chat for every student)

- talk in every chat

### Things Students can do:

- submit solutions for exercises

- see teacher's correction of solutions

- talk in different chats

### Example of course folder:

- my-courses

- - hobbies-courses

- - - drumming

- - - piano

- - sports-courses

- - - football

- - - handball

- - math

- - science

In the courses like drumming or math there are two subdirectories: submissions and content (line 19 / 20)



## How I code the backend:

### Classes:

- **Account:** name | password | id | courses (with role = teacher/student) | inbox (new invatations / if somebody joined
  your course / a student submitted solution / ...)

- **Course:** name | id | teachers | students | chats

- **Exercise:** name | course (id) | description | id | creator (id) | for_students (students' IDs; only students)

- **Date**: name | id | course (id) | description | creator (id) | for_people (people's IDs; students OR/AND teachers)

- **Survey**: name | id | description | course (id) | creator (id) | for_people (people's IDs; students OR/AND teachers)

- **Invatation:** id | from_user | to_user | course (id) | role (teacher or student)

- **Chat:** name | id | course (id) | people (list of people who can see and write in this chat)



## IDs:

As you can see at the section with the classes, every object has an ID. That is better than just having names because
different courses can have the same name. (e.g. there are two schools, both have their own course called 'Mathematics')
BUT there can't be two things with the same name in ONE course.

The IDs look similar to the IDs I use in my Smart Home Repository (github.com/JannisKohle/SmartHome).
It is always two letters at the beginning (type of object) and an integer between 100 and 999. Because
of that, there are only about 800 possible IDs for each type. If lots of people use this platform, that would be pretty
terrible. Of course later, when more people are using the platform, we can change how the IDs work. But then, there
are still the old courses with the old IDs, and it's very hard to change their IDs, because you would have to do that for
every course, then for every user in that course. -> It's a lot easier to just use bigger IDs from the beginning, so
now I am using IDs with two letters and an integer between 10,000 and 99,999.
Actually, right now nobody can really download and *use* this App. But if it is finished one day, it should really work.

### Example IDs:

- AC93759 -> AC = Account

- CO37855 -> CR = Course

- IN34825 -> IN = Invatation

- CH29464 -> CH = Chat
