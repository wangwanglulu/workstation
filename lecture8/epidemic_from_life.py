# -*- coding: utf-8 -*-
'''
Epidemic spread model adapted from Game of Life.
Two visible states:
    '#' = infected
    ' ' = healthy
Hidden variable:
    infection_age[i][j] = how many steps the person has been infected

Ideas:
- A healthy person becomes infected if enough nearby neighbors are infected.
- An infected person recovers after recovery_period steps.
- Recovered people are healthy again, so they can be infected again later.
- We count the number of infected people at each step, so we can compare it
  with healthcare_capacity and see whether overload happens.
'''

import os
import random

width = 30
height = 20
screen = []
infection_age = []

# -------- Adjustable parameters --------
initial_infection_rate = 0.08   # initial proportion of infected people
infection_threshold = 2         # become infected if infected neighbors >= this number
recovery_period = 4             # recover after this many steps
healthcare_capacity = 80        # if infected count > this, overload happens
# --------------------------------------


def Init():
    global screen, infection_age
    screen = []
    infection_age = []

    for _ in range(height):
        line = []
        age_line = []
        for _ in range(width):
            if random.random() < initial_infection_rate:
                line.append('#')
                age_line.append(1)
            else:
                line.append(' ')
                age_line.append(0)
        screen.append(line)
        infection_age.append(age_line)


def PrintScreen():
    for i in range(height):
        for j in range(width):
            print(screen[i][j] + ' ', end='')
        print()



def TryGetCell(i, j):
    i = i % height
    j = j % width
    return screen[i][j]



def GetNearbyCellsCount(i, j):
    num = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            if TryGetCell(i + di, j + dj) == '#':
                num += 1
    return num



def CountInfected():
    total = 0
    for row in screen:
        total += row.count('#')
    return total



def Update():
    global screen, infection_age

    newScreen = []
    newAge = []

    for i in range(height):
        line = []
        age_line = []
        for j in range(width):
            count = GetNearbyCellsCount(i, j)

            if screen[i][j] == '#':
                # infected -> recover after recovery_period steps
                if infection_age[i][j] >= recovery_period:
                    line.append(' ')
                    age_line.append(0)
                else:
                    line.append('#')
                    age_line.append(infection_age[i][j] + 1)
            else:
                # healthy -> infected if enough nearby infected people
                if count >= infection_threshold:
                    line.append('#')
                    age_line.append(1)
                else:
                    line.append(' ')
                    age_line.append(0)

        newScreen.append(line)
        newAge.append(age_line)

    screen = newScreen
    infection_age = newAge



def Start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('== Epidemic Spread Model ==')
    print(f'infection_threshold = {infection_threshold}')
    print(f'recovery_period = {recovery_period}')
    print(f'healthcare_capacity = {healthcare_capacity}')
    print("'#' = infected, blank = healthy")
    print("Press Enter to continue, 'q' to quit.")
    input('Press Enter to start...')

    Init()
    step = 0
    peak_infected = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        infected = CountInfected()
        peak_infected = max(peak_infected, infected)
        overloaded = infected > healthcare_capacity

        print('== Epidemic Spread Model ==')
        print(f'Step: {step}')
        print(f'Current infected: {infected}')
        print(f'Peak infected: {peak_infected}')
        print(f'Healthcare capacity: {healthcare_capacity}')
        print(f'Overloaded now? {"YES" if overloaded else "NO"}')
        print()
        PrintScreen()
        print()
        c = input("Press Enter to update, or 'q' to quit: ")
        if c == 'q':
            break

        Update()
        step += 1

    print('\nEnd')
    print(f'Final peak infected: {peak_infected}')
    if peak_infected > healthcare_capacity:
        print('Conclusion: healthcare overload occurred.')
    else:
        print('Conclusion: healthcare overload did not occur.')


Start()
