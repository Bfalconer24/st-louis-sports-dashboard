# Engineering Notebook

## August 3, 2026

### Topic: Pandas

#### What I learned

- `pd.read_sql_query()` loads SQL query results directly into a Pandas DataFrame.
- `value_counts()` counts how many times each unique value appears in a column.
- `len(df)` returns the total number of rows in a DataFrame.
- `print(df.columns)` is useful for checking available columns before using `groupby()` or accessing data.

#### Mistake I made

I tried:

```python
players.groupby("team_name")
```

but my DataFrame only contained:

- player_name
- position
- nationality

This caused:

```
KeyError: 'team_name'
```

#### Lesson

Never assume a DataFrame contains a column.

Always verify:

```python
print(players.columns)
```

before writing analysis.

---

### Project Progress

Completed:

- API integration
- SQLite database
- AI report generation
- AI report storage
- Position analysis
- Nationality analysis
- Saved visualizations

## August 4, 2026

### Topic: Dashboard Structure

### What I learned

- A script runs a fixed sequence of commands.
- An application allows user interaction.
- `input()` allows the user to provide a choice.
- `if / elif / else` controls what happens based on that choice.

### Architecture lesson

analysis.py creates information.

dashboard.py presents information.

Keeping responsibilities separate makes projects easier to expand.

### Progress

- Added dashboard menu
- Added user-controlled options
- Converted dashboard from static output into an interactive program

# Problem:
Dashboard only displayed fixed output.

# Solution:
Added user input and conditional logic.

# Concept learned:
Programs can change behavior based on user decisions.

# Wednesday-August 5 Notes

## Interactive Dashboard

### Objective

Transform the dashboard from a Python script that runs once into an interactive application that remains active until the user chooses to exit.

### Interactive Program Flow

Instead of writing a program that performs one task and immediately closes, I learned how to build a dashboard that continuously waits for user input.

```text
Start Program
      ↓
Display Menu
      ↓
User Makes Selection
      ↓
Perform Requested Task
      ↓
Return to Menu
      ↓
Repeat
      ↓
Exit Only When Requested
```

### The `while` Loop

The dashboard remains active because of a `while` loop.

```python
running = True

while running:
```

The program keeps looping while `running` is `True`.

When the user selects **Exit**, the program executes:

```python
running = False
```

which stops the loop and closes the application.

### Dashboard Architecture

The dashboard acts as the control center of the project.

```text
SQLite Database
        ↓
SQL Query
        ↓
Pandas DataFrame
        ↓
Dashboard
        ↓
User
```

The dashboard retrieves information from the database but does not create or modify AI reports.

---

## Programming Concepts

### Calculate Once, Reuse

Instead of repeatedly calculating the same information, store it once and reuse it.

Example:

```python
position_counts = players["position"].value_counts()
```

Benefits:

- Faster execution
- Cleaner code
- Easier maintenance
- Better organization

### Python Indentation

Python uses indentation to define program structure.

Important rules:

- Code inside a `while` loop must be indented.
- Code inside an `if` statement must be indented.
- Code inside a `for` loop must be indented further.
- Mixing tabs and spaces can produce `IndentationError` or `SyntaxError`.

Unlike many programming languages, indentation is part of Python's syntax.

### Key Concepts Learned

- Interactive console applications
- `while` loops
- Control variables (`running`)
- Menu-driven program flow
- SQLite database retrieval
- Pandas DataFrames
- Reusing calculated data
- Python indentation

---
## Think
> **Build systems, not scripts.**

A script performs one task and exits.

A system remains available, accepts commands, organizes information efficiently, and allows the operator to retrieve intelligence quickly.

The dashboard is becoming the command center for the entire St. Louis Sports Insight Dashboard project.

