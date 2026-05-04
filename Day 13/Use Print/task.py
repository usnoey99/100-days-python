word_per_page = 0  # Initialize variable (currently 0)

pages = int(input("Number of pages: "))  # Get number of pages from user

# BUG: '==' is a comparison operator, not assignment
# This line checks equality but does NOT store the input value
word_per_page == int(input("Number of words per page: "))

# Since word_per_page is still 0, the result will always be 0
total_words = pages * word_per_page

print(total_words)  # Outputs 0 due to the bug


# FIXED VERSION

# Get number of pages
pages = int(input("Number of pages: "))

# Correctly assign the input value using '='
word_per_page = int(input("Number of words per page: "))

# Multiply to get total words
total_words = pages * word_per_page

# Print the correct result
print(total_words)