# Reverse Tax Calculator

A small Python (Tkinter) desktop app for individual entrepreneurs (IP) in Kazakhstan.
It calculates the contract amount needed so that, after tax is withheld,
you end up with the exact net amount you want.

## Why

IP entrepreneurs pay tax on income (e.g. 15%). If you want to receive a
specific net amount "in hand," you need to know what gross amount to put
in the contract. This app calculates it instantly.

## Formula

Contract Amount = Net Amount / (1 − Tax % / 100)

Example: you want 100,000 ₸ net, tax rate 15% →
Contract Amount = 100,000 / 0.85 ≈ 117,647 ₸

## Features

- Input the desired net amount
- Input the tax/withholding percentage
- Automatically calculates the required contract amount
- Reset button — clears all fields

## Tech Stack

- Python
- Tkinter (GUI)

## How to Run

```bash
"python emae.py"
```

## Instal .exe
```bash
click "Обратный процент.exe"
```

## Installation

```bash
https://github.com/OmegA23260/OmegA/blob/main/Instructions
```
