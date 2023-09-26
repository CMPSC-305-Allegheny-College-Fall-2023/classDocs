Queries: 04_19Sept2023

sqlite> .schema
CREATE TABLE Department (
id TEXT NOT NULL PRIMARY KEY,
dept TEXT NOT NULL,
roomNum INTEGER NOT NULL
);
CREATE TABLE Tea (
id TEXT NOT NULL PRIMARY KEY,
tea INTEGER NOT NULL,
sandwich TEXT NOT NULL
);
CREATE TABLE Session (
id TEXT NOT NULL PRIMARY KEY,
session INTEGER NOT NULL,
material TEXT NOT NULL
);


1. Single table: Show me all rows from each of the tables, individually.

```
SELECT * from Department;
SELECT * from Session;
SELECT * from Tea;
```

2. Two tables: Show me the name, dept and whether the person will have tea.

```
Select Tea.id, Department.Dept, Tea.tea FROM Tea, Department where Tea.ID == Department.ID;
```

3. Show me the name and dept of each person who will have a Ruban.

```
Select Tea.id, Department.Dept, Tea.tea FROM Tea, Department where Tea.ID == Department.ID AND Tea.sandwich == "Ruban";
```

4. Three tables: Show me the sandwich type and the session room number of each person.

```
Select Tea.id, Tea.sandwich, Session.session FROM Tea, Session WHERE Tea.id == Session.ID;
```

5. Show the ID, sandwich type, session material and department room number.

```
Select Tea.id, Tea.sandwich, Session.material, Department.roomNum FROM Tea, Session, Department WHERE Tea.id == Session.ID AND Tea.id == Department.id ;
```

6. Three tables: Show the ID, sandwich type, session material and department room number.

```
Select Session.id,Tea.sandwich, Session.Material, Department.roomNum FROM Session, Tea, Department  WHERE Session.id == Tea.ID AND Session.ID == Department.ID;
```

7. Three tables: Show me all the ID, Material, Tea and Sandwich and department room number.

```
Select Session.id, Session.Material, Tea.tea, Tea.sandwich, Department.Dept FROM Session, Tea, Department  WHERE Session.id == Tea.ID AND Session.ID == Department.ID;
```

8. Three tables: Show me the ID, Material, Tea and Sandwich and department room number for each person who will have a Ruban.

```
Select Session.id, Session.Material, Tea.tea, Tea.sandwich, Department.Dept FROM Session, Tea, Department  WHERE Session.id == Tea.ID AND Session.ID == Department.ID AND Tea.sandwich == "Ruban";
```

9. Three tables: Show me the ID, Material, Tea and Sandwich and department room number for each person who will be presenting a “pres”.

```
Select Session.id, Session.Material, Tea.tea, Tea.sandwich, Department.Dept FROM Session, Tea, Department  WHERE Session.id == Tea.ID AND Session.ID == Department.ID AND Session.material =="pres";
```