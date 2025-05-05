# Sales Commissions Calculator

A Python-based interactive application for calculating sales commissions using different commission models.

## Overview

The Sales Commissions Calculator helps sales managers and representatives calculate commission payouts using three different commission models. The calculator is optimized for quarterly sales cycles while also tracking annual attainment.

## Features

- Interactive menu-based interface
- Support for three different commission models
- Quarterly defaults for sales quotas and compensation
- Automatic tracking of both quarterly and annual attainment
- Input validation for numerical values
- Detailed calculation results
- Option to perform multiple calculations in a single session
- **Persistent settings** - frequently used values are saved between sessions
- Default values for common inputs

## Requirements

- Python 3.x

## Installation

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/sales-commissions-calculator.git
cd sales-commissions-calculator
```

## Usage

Run the application with Python:

```bash
python3 commissions.py
```

Follow the on-screen menu to:
1. Select a commission model
2. Enter the required values (saved values will appear as defaults)
3. View calculation results
4. Perform additional calculations or exit

### Saved Settings

The application saves frequently used values between sessions, including:
- Quarterly variable compensation amount (default: $37,500)
- Quarterly quota amount (default: $187,500)
- Quarterly attainment to date
- Annual attainment to date
- Default fixed rate percentage

You can update these settings at any time using the "Update Saved Settings" option in the main menu.

## Commission Models

### Fixed Rate Commission
Commission is calculated by applying a fixed percentage rate to the revenue amount.

### Variable Rate Commission
The commission rate is determined by dividing the quarterly variable compensation amount by the quarterly quota, then applying this rate to the revenue.

### Leveraged Commission
The commission is calculated by determining the attainment percentage (revenue/quota), then applying this percentage to the quarterly variable compensation amount.

## Project Structure

- `commissions.py`: Main program with menu interface
- `calc.py`: Commission calculation functions
- `formatting.py`: Help text and formatting functions
- `settings.py`: Handles saving and loading of user settings

## License

This project is licensed under the MIT License.

