# Gasification_Thermodynamic_Optimization_En

This repository contains a Python script (`gasification_opt.py`) for automated thermodynamic calculation and optimization of the gasification process. The project determines the optimal gasification temperature and analyzes the influence of process parameters on statistical weight and energy balance.

---

## Features

- Calculate mass and energy balances for the gasification process
- Iteratively find the optimal gasification temperature with minimal energy balance error
- Compute synthesis gas composition (CO, CO₂, H₂, H₂O, N₂)
- Output key process parameters and statistical weight
- Easily adapt to different input data

---

## Main Scripts

- **`gasification_opt_RC.py`** — Main script with pure math and formulas.  
- **`gasification_opt_Debug.py`** — Extended debug script with detailed intermediate output.

---

## Installation

Python 3.x and notihng more, just pure math and formulas 

---

## Usage

Just run **`gasification_opt.py`** with your input data.

---

## Input Parameters

All input parameters (temperatures, mass flows, composition, etc.) are defined at the beginning of the script and can be modified as needed.

---

## Output

Upon execution, the script prints:

- Optimal gasification temperature
- Energy balance error
- Inlet and outlet temperatures
- Average temperature
- Statistical weight of the process
- Main process parameters

---

# Gasification_Thermodynamic_Optimization_Ru

Этот репозиторий содержит Python-скрипт (`gasification_opt.py`) для автоматизированного термодинамического расчёта и оптимизации процесса газификации. Проект определяет оптимальную температуру газификации и анализирует влияние параметров процесса на статистический вес и энергетический баланс.

---

## Возможности

- Расчёт материального и энергетического балансов процесса газификации
- Итеративный поиск оптимальной температуры газификации с минимальной погрешностью энергобаланса
- Расчёт состава синтез-газа (CO, CO₂, H₂, H₂O, N₂)
- Вывод ключевых параметров процесса и статистического веса
- Легкая адаптация под различные входные данные

---

## Основные скрипты

- **`gasification_opt_RC.py`** — Основной скрипт с чистой математикой и формулами.  
- **`gasification_opt_Debug.py`** — Расширенная версия с детализированным промежуточным выводом.

---

## Установка

Требуется Python 3.x, больше ничего — только чистая математика и формулы.

---

## Использование

Просто запустите **`gasification_opt.py`** с вашими входными данными.

---

## Входные параметры

Все входные параметры (температуры, массовые потоки, состав и т.д.) задаются в начале скрипта и могут быть изменены по необходимости.

---

## Результат

После выполнения скрипт выводит:

- Оптимальную температуру газификации
- Погрешность энергетического баланса
- Температуры на входе и выходе
- Среднюю температуру
- Статистический вес процесса
- Основные параметры процесса
