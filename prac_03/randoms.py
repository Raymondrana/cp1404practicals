# What did you see on line 1?
# Answer: A random integer between 5 and 20 inclusive (e.g., 18).
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number was 5, and the largest number was 20.

# What did you see on line 2?
# Answer: A random odd integer from the sequence 3, 5, 7, 9 (e.g., 7).
# What was the smallest number you could have seen, what was the largest? (for line 2)
# Answer: The smallest number was 3, and the largest number was 9. (10 is excluded, and it increments by 2).

# What did you see on line 3?
# Answer: A random floating-point (decimal) number between 2.5 and 5.5 (e.g., 4.89509).
# What was the smallest number you could have seen, what was the largest? (for line 3)
# Answer: The smallest number was 2.5, and the largest number was 5.5.

import random

print(random.randint(1, 100))