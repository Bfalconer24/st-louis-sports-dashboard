# St. Louis Sports Insight Dashboard

## Overview

The St. Louis Sports Insight Dashboard is a modular Python application for collecting, storing, analyzing, and interpreting sports data.

The system combines external API data, a local SQLite database, statistical analysis, visualization, and AI-generated scouting reports into a single workflow.

## Objectives

The project is built around practical engineering problems:

-   Collect structured data from external APIs
-   Design and maintain a relational data layer
-   Transform raw data into useful analytical information
-   Generate visual representations of sports data
-   Apply AI to structured scouting analysis
-   Build modular Python components that can be tested and extended independently
-   Maintain a documented development history with Git



## Technology

- Python
- Requests
- SQLite
- Pandas
- Matplotlib
- OpenAI API
- python-dotenv
- Git


## System Architecture

```text
TheSportsDB API
       │
       ▼
Data Collection
       │
       ▼
SQLite Database
       │
       ├── Teams
       ├── Players
       ├── Events
       └── AI_Reports
              │
       ┌──────┴──────┐
       ▼             ▼
   Analytics      AI Reports
       │             │
       ▼             ▼
Visualization     Dashboard
       │
       ▼
     assets/
```

## Current Capabilities

### Data Collection

The application retrieves sports data from TheSportsDB, including:

- Teams
- Players
- Events
- Leagues
- Venues
- Player positions
- Player nationalities




### Database

SQLite provides the local persistence layer.

Current tables:

| Table        | Purpose                                 |
| ------------ | --------------------------------------- |
| `Teams`      | Stores team information |
| `Players`    | Stores player information and API identifiers |
| `Events`     | Stores scheduled and completed sporting events |
| `AI_Reports` | Stores generated scouting reports |

Player and event records use API-provided identifiers to maintain stable records and reduce duplicate entries.

### Analytics

The analytics layer uses Pandas to query and transform database records and Matplotlib to produce visualizations.

Current outputs include:

-   Players by position
-   Players by nationality
-   Events by league
-   Sports events over time

Generated visualizations are stored in `assets/`.

### AI Scouting

The application can generate structured scouting reports containing:

-  Strengths
-  Weaknesses
-  Overall evaluation
-  Report metadata

Reports are persisted in the `AI_Reports` table in SQLite and can be retrieved through the dashboard.

### Dashboard

`dashboard.py` provides the primary interactive console interface for accessing the project's data and AI functionality.

## Project Structure

```text
st-louis-sports-dashboard/
│
├── ai_reports.py
├── analytics.py
├── api_fetch.py
├── dashboard.py
├── database_events.py
├── database_players.py
├── database_teams.py
├── data_table.py
├── events_fetch.py
│
├── assets/
│   ├── events_by_league.png
│   ├── events_over_time.png
│   ├── nationality_distribution.png
│   └── position_distribution.png
│
├── Engineering_Notebook.md
├── README.md
├── requirements.txt
├── .gitignore
└── sports.db
```

## Data Pipeline

The core workflow is:

```text
API
 ↓
JSON
 ↓
SQLite
 ↓
SQL Queries
 ↓
Pandas
 ↓
Analysis
 ↓
Matplotlib / AI
 ↓
Dashboard / Assets
```

This separation allows the data layer, analytical layer, and presentation layer to evolve independently.

## Running the Application

### Install Dependencies

```powershell
pip install -r requirements.txt
```

### Run the Dashboard

```powershell
python dashboard.py
```

### Run the Analytics Pipeline

```powershell
python analytics.py
```

The analytics pipeline generates the current visualization assets in `assets/`.

## Engineering Practices

The project is developed incrementally with Git. Individual commits represent meaningful changes to the application's architecture, data layer, analytics, and documentation.

The `Engineering_Notebook.md` file records the reasoning and development process behind the implementation.

## Development Roadmap

Future work includes:

- Expand sports and league coverage
- Improve relational database relationships
- Increase data volume and refresh capabilities
- Add more advanced SQL analysis
- Integrate analytics directly into the dashboard
- Expand AI scouting capabilities
- Improve validation and error handling
- Add automated testing
- Improve application presentation
- Automate recurring data collection

## Status

The project currently has a functioning API → SQLite → analytics → visualization pipeline, an interactive dashboard, and persisted AI scouting reports.

The remaining work is focused on integration, robustness, testing, and refinement.

<!-- GitHub Actions automation enabled -->
