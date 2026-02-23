# AdvancedGenerativeAI_Feb23
# VTU Internship – Domain Based System Design
Language Used: Python

---

## Student Name
Sagar C

## Internship Domain
Domain-Based Application Development

---

## Task 1: Metro Fare Calculation System

### Domain
Transportation Domain

---

### Problem Statement
The objective of this task is to design a Metro Ticketing System that calculates the fare for passengers based on the number of stations traveled, travel time category, and predefined fare rules. The system simulates a real-world transportation pricing application using multiple inputs and decision-based logic.

---

### System Requirements
The system should be able to:
1. Accept the number of stations traveled
2. Use a predefined base fare
3. Identify the travel type (Peak / Non-Peak hours)
4. Calculate the total fare
5. Apply a daily fare cap if the calculated fare exceeds the maximum limit

---

### Business Rules
- Base Fare: ₹20
- Additional Fare: ₹5 per station
- Peak Hour Charges: 20% extra on the total fare
- Maximum Daily Fare Cap: ₹100

---

### Logic Explanation
The system begins by assigning a base fare. Additional charges are calculated based on the number of stations traveled. Conditional logic checks whether the journey occurs during peak hours and applies extra charges accordingly. Finally, a cap is enforced to ensure the fare does not exceed the daily limit.

---

### Output
- Final payable fare
- Peak hour charges applied (Yes/No)
- Daily fare cap applied (Yes/No)

---

### Concepts Used
- Functions
- Conditional Statements
- Arithmetic Operations
- Rule-based decision logic

---

### Learning Outcome
- Gained understanding of transportation fare calculation systems
- Implemented multiple rules in a single application
- Learned how real-world software systems produce decision-based outputs

---

## Task 2: Gaming Player Performance Ranking System

### Domain
Gaming Domain

---

### Problem Statement
The objective of this task is to design a Gaming Leaderboard System that evaluates a player’s performance across multiple matches. The system calculates the total score, assigns a rank, and determines whether the player qualifies as a professional player.

---

### System Requirements
The system should be able to:
1. Accept scores from multiple matches
2. Calculate the total score
3. Assign player rank
4. Identify professional players

---

### Ranking Rules

| Total Score | Rank |
|------------|------|
| ≥ 1200     | Diamond |
| ≥ 900      | Gold |
| ≥ 600      | Silver |
| < 600      | Bronze |

---

### Professional Player Criteria
- Total Score ≥ 1000 indicates a Professional Player

---

### Logic Explanation
Scores from multiple matches are aggregated using loops. Conditional logic assigns the appropriate rank based on the total score. An additional condition flags professional players based on the defined threshold.

---

### Output
- Total score
- Player rank
- Professional player status

---

### Concepts Used
- Lists
- Loops
- Conditional Statements
- Functions
- Decision-based output modeling

---

### Learning Outcome
- Designed a real-world gaming performance evaluation system
- Combined multiple rules and inputs in a single application
- Understood classification and status-based output generation

---

## Conclusion
These tasks demonstrate how domain-based applications are designed using multiple inputs, business rules, and conditional logic. The systems closely resemble real-world software engineering workflows and decision-making processes.
