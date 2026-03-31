# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram

```mermaid
usecase
    actor Student
    actor Admin

    usecase "Login as Student" as UC1
    usecase "Create Student Profile" as UC2
    usecase "View Course Catalog" as UC3
    usecase "Register for Course" as UC4
    usecase "Drop Course" as UC5
    usecase "View My Schedule" as UC6
    usecase "View Billing Summary" as UC7
    usecase "Edit Profile" as UC8
    usecase "Logout and Save" as UC9

    usecase "Login as Admin" as UC10
    usecase "View Class Roster" as UC11
    usecase "View All Students" as UC12
    usecase "Add New Student" as UC13
    usecase "Edit Student Profile" as UC14
    usecase "Add New Course" as UC15
    usecase "Edit Course" as UC16
    usecase "View Student Schedule" as UC17
    usecase "View Billing Summary (any student)" as UC18
    usecase "Logout and Save" as UC19

    Student --> UC1
    Student --> UC2
    Student --> UC3
    Student --> UC4
    Student --> UC5
    Student --> UC6
    Student --> UC7
    Student --> UC8
    Student --> UC9

    Admin --> UC10
    Admin --> UC3
    Admin --> UC11
    Admin --> UC12
    Admin --> UC13
    Admin --> UC14
    Admin --> UC15
    Admin --> UC16
    Admin --> UC17
    Admin --> UC18
    Admin --> UC19
```

### Flowchart of the main workflow

### Prompts
