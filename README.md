# 2.3 Building a Rule-Based AI System with Python

**Name:** David Fulmer

## Part 1: Three Project Ideas

### Idea 1 — Rule-Based PC Diagnostic Assistant
**What it does:**  
The system asks the user to describe a computer problem and then provides basic troubleshooting steps. It can recognize common categories such as power problems, display problems, network problems, slow performance, and overheating.

**How the rules work:**  
The program converts the user's input to lowercase and checks it for predefined keywords. For example, IF the input contains phrases such as "no power" or "won't turn on," THEN it returns power troubleshooting steps. ELSE IF it contains "black screen" or "no display," THEN it follows the display troubleshooting rules.

### Idea 2 — Study Focus Assistant
**What it does:**  
The system recommends a study action based on the student's current problem, such as distraction, fatigue, confusion, or feeling overwhelmed.

**How the rules work:**  
IF the user says they are distracted, THEN the system recommends removing distractions and using a short timed work session. IF the user says they are confused, THEN it recommends breaking the assignment into smaller questions. IF the user says they are tired, THEN it recommends a short break before returning to the task.

### Idea 3 — Construction Job Troubleshooting Assistant
**What it does:**  
The system gives basic recommendations for common construction-project problems such as material shortages, schedule delays, safety concerns, or quality-control issues.

**How the rules work:**  
IF the user reports a material shortage, THEN the system recommends checking inventory, suppliers, and substitute materials. IF the problem is a schedule delay, THEN it recommends identifying the blocking task and adjusting dependent work. IF a safety issue is reported, THEN safety becomes the highest-priority response.

## Selected Project

I chose the **Rule-Based PC Diagnostic Assistant** because computer troubleshooting fits naturally into an IF-THEN rule system. A lot of basic troubleshooting already follows a decision-tree process, so it is a good way to demonstrate how an AI system can appear intelligent without using machine learning.

## Part 2: Rules and Logic

The system uses the following rules:

1. **IF** the input contains phrases such as `no power`, `won't turn on`, `dead`, or `power issue`, **THEN** provide power troubleshooting steps.
2. **ELSE IF** the input contains `black screen`, `no display`, `no signal`, or `monitor`, **THEN** provide display troubleshooting steps.
3. **ELSE IF** the input contains `wifi`, `internet`, `network`, `offline`, or `can't connect`, **THEN** provide network troubleshooting steps.
4. **ELSE IF** the input contains `slow`, `lag`, `freeze`, `stutter`, or `performance`, **THEN** provide performance troubleshooting steps.
5. **ELSE IF** the input contains `overheat`, `too hot`, `fan loud`, `thermal`, or `temperature`, **THEN** provide cooling and temperature troubleshooting steps.
6. **ELSE** provide a general troubleshooting response and ask the user to describe the symptom more specifically.

### Pseudocode

```text
GET problem description from user
CONVERT description to lowercase

IF description matches power keywords
    RETURN power troubleshooting advice
ELSE IF description matches display keywords
    RETURN display troubleshooting advice
ELSE IF description matches network keywords
    RETURN network troubleshooting advice
ELSE IF description matches performance keywords
    RETURN performance troubleshooting advice
ELSE IF description matches thermal keywords
    RETURN thermal troubleshooting advice
ELSE
    RETURN general troubleshooting advice
```

## Part 3: Test Results

### Test 1
**Input:**  
`My computer won't turn on and there are no lights.`

**Result:**  
The system selected the **POWER DIAGNOSIS** rule and recommended checking the power cable, outlet or surge protector, desktop power-supply switch, peripherals, and finally the power supply or motherboard.

### Test 2
**Input:**  
`My Wi-Fi says connected but I have no internet.`

**Result:**  
The system selected the **NETWORK DIAGNOSIS** rule and recommended checking the connection, testing another device, restarting the computer and router, reconnecting to Wi-Fi, and checking the network adapter.

### Test 3
**Input:**  
`The computer is really slow and keeps freezing.`

**Result:**  
The system selected the **PERFORMANCE DIAGNOSIS** rule and recommended checking Task Manager for CPU, memory, disk, and GPU usage, closing unnecessary programs, checking storage, restarting, and investigating any resource that remains near 100%.

## Part 4: Reflection

My rule-based system works by looking for specific words and phrases in the user's description of a computer problem and then matching that input to a predefined troubleshooting rule. The program does not learn from previous users and it does not use a machine-learning model. Instead, it follows a decision structure built with `if`, `elif`, and `else` statements. I used groups of keywords for power, display, networking, performance, and thermal problems. Once one of those rules matches, the program returns a set of troubleshooting steps for that category. If nothing matches, the fallback rule gives general advice and asks for a more specific description.

The biggest challenge while working with the AI assistant was keeping the project truly rule-based instead of making it more complicated than the assignment required. Modern AI tools make it easy to think about natural-language understanding or machine learning, but the point of this project was to understand how earlier AI systems could behave intelligently through explicitly written rules. I also had to think about rule order and overlapping words. For example, a user might describe a computer as both "slow" and "hot," but the program needs to choose one branch first because an `if-elif-else` structure stops after the first matching rule.

Working through the code helped me understand the difference between intelligence that comes from learned patterns and intelligence that comes from human-defined logic. This system is limited because it can only respond to situations I anticipated when I wrote the rules, but that limitation is also what makes the assignment useful. It shows that useful automated decision-making does not require machine learning; it can also come from carefully designed heuristics and decision trees.
