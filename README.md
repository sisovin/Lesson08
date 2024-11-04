# Lesson 08: loops

## How does this loop work?

value = 1
while value <= 10:
print(value)
if value == 5:
break
value += 1
This loop works as follows:

1. Initialize [`value`] to 1.
2. Enter a `while` loop that continues as long as [`value`] is less than or equal to 10.
3. Inside the loop, print the current value of [`value`].
4. Check if [`value`] is equal to 5. If it is, exit the loop immediately using `break`.
5. If [`value`] is not equal to 5, increment [`value`] by 1.
6. Repeat steps 2-5 until the loop condition is no longer true or the loop is exited via the `break` statement.

In this specific case, the loop will print numbers 1 through 5. When [`value`] reaches 5, the `if` condition triggers the `break` statement, exiting the loop early before [`value`] can reach 10.

## What is the purpose of the `break` statement in a loop?

The `break` statement in a loop is used to exit the loop immediately, regardless of the loop's condition. It is typically used to stop the execution of the loop when a specific condition is met, allowing the program to continue with the next block of code outside the loop. This can be useful for optimizing performance by avoiding unnecessary iterations or for controlling the flow of the program in scenarios where continuing the loop is no longer needed or desired.

## How does this loop work while, after continue?

This loop works as follows:

1. Initialize [`value`] to 1.
2. Enter a `while` loop that continues as long as [`value`] is less than or equal to 10.
3. At the beginning of each iteration, increment [`value`] by 1.
4. Check if [`value`] is equal to 5. If it is, `continue` is executed, which skips the rest of the code in the current iteration and proceeds to the next iteration of the loop. This means [`print(value)`] is skipped when [`value`] is 5.
5. If [`value`] is not equal to 5, print [`value`].
6. Repeat steps 3-5 until [`value`] is greater than 10.
7. Once the loop condition ([`value <= 10`]) is no longer true, the `else` block is executed, printing "Value is now equal to " followed by the current value of [`value`].

Given the `continue` statement, the number 5 is never printed because the [`print(value)`] statement is skipped when [`value`] is 5. The increment happens at the start of the loop, so the first printed number is 2, not 1. The loop prints numbers from 2 to 11, skipping 5. The final value of [`value`] when the loop exits is 11, so the `else` block prints "Value is now equal to 11".

Output:
2
3
4
6
7
8
9
10
11
Value is now equal to 11

## How does this loop work with string array?

names = ["John", "Paul", "George", "Ringo"]
for x in names:
print(x)

**Explanation:**
This loop iterates over the [`names`] array, which contains strings. Here's how it works:

1. Define an array [`names`] with four elements: `"John"`, `"Paul"`, `"George"`, and `"Ringo"`.
2. Use a `for` loop to iterate over each element in the [`names`] array. In each iteration, the variable [`x`] is assigned the value of the current element.
3. Inside the loop, print the value of [`x`], which is the current name from the [`names`] array.
4. Repeat steps 2-3 for each element in the [`names`] array.

The output of this loop will be:

John
Paul
George
Ringo

Each name in the [`names`] array is printed on a new line in the order they appear in the array.

## How does this loop work with nested loops, please explain me two nested loops with the following code structure?

names = ["Sisovin", "Sovanny", "Viphop"]
actions = ["codes", "eats", "sleeps"]
for name in names:
for action in actions:
print(name +" "+ action +".")
print("")
for action in actions:
for name in names:
print(name +" "+ action +".")

**\*Explanation:**

This Python code snippet demonstrates the use of nested loops to iterate over two lists, [`names`] and [`actions`], and print combinations of their elements. Here's a step-by-step explanation:

1. **First Outer Loop ([`for name in names:`])**: This loop iterates over each element in the [`names`] list. For each iteration of this loop, the variable [`name`] takes on the value of the current element from the [`names`] list.

2. **First Inner Loop ([`for action in actions:`])**: Inside the first outer loop, there's a nested loop that iterates over each element in the [`actions`] list. For each iteration of this inner loop, the variable [`action`] takes on the value of the current element from the [`actions`] list.

   - **Combination Printing ([`print(name +" "+ action +".")`])**: Inside the inner loop, it prints a combination of the current [`name`] from the outer loop and the current [`action`] from the inner loop, separated by a space and ending with a period. This results in printing all actions for each name before moving to the next name.

3. **Empty Print Statement ([`print("")`])**: After completing the first set of nested loops, it prints an empty line for visual separation in the output.

4. **Second Outer Loop ([`for action in actions:`])**: This loop iterates over each element in the [`actions`] list. For each iteration of this loop, the variable [`action`] takes on the value of the current element from the [`actions`] list.

5. **Second Inner Loop ([`for name in names:`])**: Inside the second outer loop, there's another nested loop that iterates over each element in the [`names`] list. For each iteration of this inner loop, the variable [`name`] takes on the value of the current element from the [`names`] list.

   - **Combination Printing ([`print(name +" "+ action +".")`])**: Inside the inner loop, it prints a combination of the current [`name`] from the inner loop and the current [`action`] from the outer loop, separated by a space and ending with a period. This results in printing all names for each action before moving to the next action.

**Summary of the Output**:

- The first set of nested loops prints all actions for each name, one name at a time.
- After a blank line for separation, the second set of nested loops prints all names for each action, one action at a time.

This structure allows for every possible combination of names and actions to be printed, first grouped by names, and then grouped by actions.

## Display a list of names and actions each person is doing at least three rows with two columns.

### Iterate through each name and action

for i, name in enumerate(names, start=1):
print(f"{i}. {name} {actions[1]}.")

Please explain me how this code works?

**Explanation**

This Python code snippet is designed to display a list of names and corresponding actions, formatting the output in a numbered list. Here's a step-by-step explanation:

1. **Comment**: The first line is a comment, explaining the purpose of the code block. It's not executed but provides information about what the code is intended to do.

2. **Loop**: The `for` loop is used to iterate over each element in the [`names`] list. The [`enumerate`] function is used to keep track of the iteration count, starting from 1 (as specified by `start=1`). This is useful for displaying a numbered list.

3. **Variables**:

   - [`i`]: Represents the current iteration number (or index) in the loop, starting from 1.
   - [`name`]: Represents the current name being processed in the loop from the [`names`] list.

4. **Print Statement**: Inside the loop, a formatted string (`f-string`) is used to print the output. It combines the iteration number ([`i`]), the current name ([`name`]), and a specific action. The action is fetched from the [`actions`] list, specifically [`actions[1]`], which means it always prints the second action for every name. This is likely a mistake if the intention is to print corresponding actions for each name.

5. **Issue**: The code has a logical error. It uses [`actions[1]`] inside the loop, which means it will repeatedly print the same action for every name, instead of varying the action per name. If the intention is to match each name with a corresponding action, the code should use [`actions[i-1]`] (assuming [`actions`] list has the same length as [`names`] list and is 0-indexed).

6. **Expected Behavior**: As written, the code will print a list where each line starts with a number (starting from 1), followed by a name from the [`names`] list, and the second action from the [`actions`] list. This action will not change throughout the list, which might not be the intended behavior.

7. **Improvement Suggestion**: To fix the issue and ensure each name is paired with its corresponding action, the code should be modified to use [`actions[i-1]`] instead of [`actions[1]`], and ensure [`names`] and [`actions`] lists are of the same length to avoid `IndexError`.
