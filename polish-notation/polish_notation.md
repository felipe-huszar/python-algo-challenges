
# Polish Notation Expression Evaluator (Prefix Notation)

## 🧠 Problem Summary

In Polish notation (also called **prefix notation**), each operator comes **before** its operands.  
Unlike standard infix notation (e.g. `3 + 4`), prefix notation removes the need for parentheses or operator precedence.

---

## 🧾 Input

- A **string** expression in prefix notation, e.g. `"+ 3 4"` or `"* + 2 3 4"`.
- The expression:
  - Is **space-separated**
  - Contains **non-negative integers**
  - Uses **four operators**: `+`, `-`, `*`, and `/` (integer division)

---

## 🎯 Output

- Return the **result as an integer**, after evaluating the expression.

---

## ✅ Example Inputs and Outputs

```python
Input: "+ 3 4"
Output: 7

Input: "* + 2 3 4"
Output: 20
# Explanation: (2 + 3) * 4 = 5 * 4 = 20

Input: "- * 7 4 + 2 3"
Output: 23
# Explanation: (7 * 4) - (2 + 3) = 28 - 5 = 23
```