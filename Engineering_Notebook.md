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