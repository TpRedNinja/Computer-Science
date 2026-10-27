# Java ATM Simulator — Assignment & Grading Rubric

**Target:** 45–60 minutes  
**Core score:** 100 points  
**Optional bonus:** +15 points

## Part 1 — `BankAccount` class (30 points)

- [ ] Create a `BankAccount` class with a private `double` balance and a private `String` account-holder name.
- [ ] Use a constructor to initialize both variables.
- [ ] Implement methods to deposit money, withdraw money, and display the balance.
- [ ] Accept deposits only when the amount is greater than $0.
- [ ] Accept withdrawals only when the amount is greater than $0 and no more than the available balance.
- [ ] On success, print a confirmation, the transaction amount, and the updated balance.
- [ ] On failure, print an appropriate error message and leave the balance unchanged.

## Part 2 — ATM menu (30 points)

Create a separate `Driver` (or `Main`) class with `main()`. Display this menu repeatedly until the user exits:

```text
===== JAVA ATM =====
1. View Balance
2. Deposit Money
3. Withdraw Money
4. Account Information
5. Exit
```

- [ ] Read input using `Scanner`.
- [ ] Keep the menu running using a loop until option 5 is selected.
- [ ] Use `switch` or `if`/`else if` for the menu choices.
- [ ] Display an error for an invalid choice.
- [ ] Show the account holder's name and balance for option 4.

## Part 3 — Input validation (20 points)

- [ ] Reject withdrawals larger than the balance.
- [ ] Reject zero or negative transaction amounts.
- [ ] Reject menu selections outside the available options (e.g., `9`).
- [ ] Handle letters or other nonnumeric input where a number is expected, without crashing.
- [ ] Continue running after invalid input.

## Part 4 — Code quality (20 points)

- **10 points:** Object-oriented design: private fields, constructor, useful methods.
- **5 points:** Readability, formatting, meaningful variable names.
- **5 points:** Organized code with minimal unnecessary repetition.

## Optional bonus challenges (+15 points)

- [ ] **PIN authentication (+5):** Require a four-digit PIN and deny access after three incorrect attempts.
- [ ] **Transaction history (+5):** Store and display the last five successful transactions (an array is fine).
- [ ] **Transfer money (+5):** Create a second `BankAccount` and implement transfers between accounts.

## Grading summary

| Category | Points |
| --- | ---: |
| BankAccount class | 30 |
| ATM menu | 30 |
| Input validation | 20 |
| Code quality | 20 |
| **Core total** | **100** |
| Optional bonus | +15 |
| **Possible total** | **115** |

## Submission notes

Submit your `.java` files or paste the source code for grading. Arrays, lists, and file writing are **not required** for the core 100 points. Looking up Java syntax and documentation is allowed. `System.err.println()` is fine for error messages. No reference solution is included.
