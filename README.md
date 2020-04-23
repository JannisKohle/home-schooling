# home-schooling

## Description:

This program helps schools or other organizations toteach people something online. I got that idea
when I was thinking about how bad the system is my school is using for home schooling.
So I wanted to create something better:

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

- Account: name, password, id, courses (with role = teacher/student), inbox (new invatations / if somebody joined
  your course / a student submitted solution / ...)

- Course: name, id, teachers, students, chats

- Invatation: from_user, to_user, course (id), role (teacher or student)

- Chat: name, id, course (id), people (list of people who can see and write in this chat)

*Invatations should be Inbox in the picture*

![classes-diagram](diagram.png)
