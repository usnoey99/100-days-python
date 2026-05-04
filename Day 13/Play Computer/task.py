year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")

# The issue:
# 1994 does not satisfy either condition because:
# - The first condition uses "< 1994" → excludes 1994
# - The second condition uses "> 1994" → also excludes 1994
# So when year == 1994, no condition is true, and nothing is printed.

if year > 1980 and year <= 1994:
    # Now 1994 is included here (<= 1994)
    print("You are a millennial.")
elif year > 1994:
    # This handles years after 1994
    print("You are a Gen Z.")