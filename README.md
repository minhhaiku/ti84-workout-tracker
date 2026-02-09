# TI-84 Workout Tracker

A simple workout tracking app for the **TI-84 Plus CE Python calculator**.

## Features
- Log exercises with sets, reps, and weight
- View all saved workouts
- Clear workout history
- Data persists using calculator lists
## Advanced Features

### Calorie Tracking
Calories burned per workout are stored in `L5`.

### Progressive Overload
Estimated 1RM is calculated using the Epley formula and stored in `L6`.
The app compares recent sessions to detect strength increases.

### Exporting Data
Use TI Connect CE to export lists `L1`–`L6` as CSV files.

## Files
- `workout.py` — main program

## Installation
1. Connect calculator to computer
2. Open TI Connect CE
3. Transfer `workout.py` to calculator
4. Run from the Python menu

## Data Storage
- `L1` — Exercise name
- `L2` — Sets
- `L3` — Reps
- `L4` — Weight

## Notes
- Designed for TI-84 Python CE limitations
- No external libraries required
