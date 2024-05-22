# Recycling Reward System

## Overview
This project simulates the core functionalities of an automated collection and reward system for recyclable items. The system accepts various types of recyclable items, calculates rewards based on the item type, and provides a simple command-line interface (CLI) for user interactions.

## Setup and Running the Project

1. Clone the repository:
    ```sh
    git clone https://github.com/bhartimeena/Python.git
    ```
2. Navigate to the project directory:
    ```sh
    cd recycling-reward-system
    ```
3. Run the project:
    ```sh
    python main.py
    ```

## Code Structure

- `main.py`: The main script to run the project.
- `recycling_system.py`: Contains the `RecyclingSystem` class with methods to add items, view total rewards, and reset the system.

## Assumptions and Design Decisions

- The system accepts three types of recyclable items: Type A, Type B, and Type C.
- Each item type has a predefined reward value:
  - Type A: INR0.10
  - Type B: INR0.05
  - Type C: INR0.15
- The CLI allows users to add items, view total rewards, and reset the system.
- The system handles invalid inputs by prompting the user to enter valid options.
