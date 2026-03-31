# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram

![Use Case Diagram](usecase_diagram.png)

### Flowchart of the main workflow
flowchart TB
    Student["Student"] --> UC1["Login as Student"]
    ...
    Admin["Admin"] --> UC19["Logout and Save"]

    subgraph StudentFlow ["Student Main Menu Flow"]
        UC1 --> UC2 --> UC3 --> UC4 --> UC5 --> UC6 --> UC7 --> UC8 --> UC9
    end

    subgraph AdminFlow ["Admin Main Menu Flow"]
        UC10 --> UC3 --> UC11 --> UC12 --> UC13 --> UC14 --> UC15 --> UC16 --> UC17 --> UC18 --> UC19
    end
### Prompts
