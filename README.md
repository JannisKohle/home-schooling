# home-schooling

## Description:

This is a Home Schooling App built with:

- Frontend: Electron

- Backend: Python

- Database: ???

## How to use it:

There is a desktop app. In the app you first have to choose a folder on your computer, in which you
clone all of your courses. You can even have subdirectories in that folder, for different areas.

Every account can create a course. If you create the course, you can invite other people to it. You can decide
if they are a teacher or student. As the course leader, you can of course remove other people (teachers and
students) and you can even delete the whole course.

Cloning a course will create a course folder (the program asks you where) with two subdirectories:
submissions and content

## The App:

The first time you open the app, you have to press the SIGN IN or SIGN UP button.

If you open the app after that, you can go to three different sections:

- **MY COURSES**: here you can see a list of all your courses

- **INBOX**: here you can see all new invatations you got, new exercises / events / ... in a course

- **MY CALENDAR**: here you can see a calendar with all of your courses' events (it automatically updates if ther's a new event)

- **SETTINGS**: just some settings

On the left side of the screen you can also navigate to your most opened courses.

If you open a course, you can navigate to **CONTENT**, **EXERCISES**, **EVENTS**, **CHATS**, **SURVEYS** and if you are the course
leader, also **SETTINGS**.

### Things Teachers can do:

- invite students

- invite teachers

- change/add/delete folders and files

- see/correct students' solutions

- create new chat (automatically created chats: one for every student (to all the teachers), one for all the students and one for all
the teachers)

- create new exercise

- create new event

- create new survey

- talk in chats

### Things Students can do:

- submit solutions for exercises

- see teacher's correction of solutions

- take part in survey

- talk in some chats

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

In the courses like drumming or math there are two subdirectories: submissions and content



## How I code the backend:

### Classes:

- **Account:** name | password | id | courses (with role = teacher/student; IDs) | inbox (new invatations / if somebody joined
  your course / a student submitted solution / ...)

- **Course:** name | id | color (probably rgb) | teachers | students | chats (IDs) | leader (creator; id)

- **Exercise:** name | course (id) | description | id | creator (id) | for_students (students' IDs; only students)

- **Event**: name | id | course (id) | description | creator (id) | for_people (people's IDs; students OR/AND teachers)

- **Survey**: name | id | description | course (id) | creator (id) | for_people (people's IDs; students OR/AND teachers)

- **Invatation:** id | from_user (id) | to_user (id) | course (id) | role (teacher or student)

- **Chat:** name | id | course (id) | people (list of people who can see and write in this chat; IDs)



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

- EX87527 -> EX = Exercise

- DA29596 -> DA = Event

- SU64024 -> SU = Survey

- IN34825 -> IN = Invatation

- CH29464 -> CH = Chat


## What's stored where?

All the users, courses and things like invatations / chats are stored in a database.
What's stored on the user's computer, is if the user is logged in, the user's data ...
