"""
Author: Vikas Tyagi
Date: June 5th, 2024
"""

def attendance_probability(N):
    """
    Calculates the number of ways to attend classes over N days and the probability
    of missing the graduation ceremony given the constraint that I am not allowed
    to miss classes for four or more consecutive days.
    
    Parameters:
    N (int): The number of days in the academic year.
    
    Returns:
    tuple: A tuple containing:
        - total_ways (int): The total number of valid ways to attend classes over N days.
        - probability (str): The probability of missing the graduation ceremony in the form "numerator/denominator".
    """
    
    # Checking for zero given as an input
    if N == 0:
        return 0, "0/0"

    # Checking for the edge case where N is 1
    if N == 1:
        # For N = 1, there are 2 ways to attend classes (attend or miss the class),
        # and the probability of missing graduation is 1/2.
        return 2, "1/2"
    
    # Initializing the dp table where each element is a list of 4 integers [dp[i][0], dp[i][1], dp[i][2], dp[i][3]]
    dp = [[0, 0, 0, 0] for _ in range(N+1)]
    
    # Base cases for day 1: I can either attend or miss the class on day 1 
    dp[1][0] = 1  # Attended on day 1
    dp[1][1] = 1  # Missed on day 1
    dp[1][2] = 0  # Not possible to miss for 2 days on day 1, hence 0
    dp[1][3] = 0  # Not possible to miss for 3 days on day 1, hence 0
    
    # Filling the dp table for days from 2 to N
    for i in range(2, N+1):
        # If attending class on day i, then I need to sum the following scenarios
        # dp[i-1][0] : attended class on day i-1 as well
        # dp[i-1][1] : missed class on day i-1 for 1 day
        # dp[i-1][2] : missed class on day i-1 for 2 consecutive days
        # dp[i-1][3] : missed class on day i-1 for 3 consecutive days
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
        
        # If missing class on day i for 1 day, then I attended class on day i-1
        dp[i][1] = dp[i-1][0]
        # If missing class on day i for 2 consecutive days, then I missed class on day i-1 for 1 consecutive days
        dp[i][2] = dp[i-1][1]
        # If missing class on day i for 3 consecutive days, then I missed class on day i-1 for 2 consecutive days
        dp[i][3] = dp[i-1][2]
    
    # Total number of ways to attend classes over N days will be sum of dp[N][0], dp[N][1], dp[N][2], dp[N][3]
    total_ways = dp[N][0] + dp[N][1] + dp[N][2] + dp[N][3]
    # The number of ways to miss the graduation ceremony (i.e., miss the class on the Nth day)
    ways_to_miss_graduation = total_ways - dp[N][0] # dp[N][0] represents total number of ways I attended the graduation ceremony which is on Nth day
    
    # Return the total ways and the probability as a string in the form "numerator/denominator"
    return total_ways, f"{ways_to_miss_graduation}/{total_ways}"


if __name__ == "__main__":
    # Reading input
    N = int(input("Enter the day: "))

    # Get the results
    total_ways, probability = attendance_probability(N)

    # Print the final result
    print(f"{probability} / {total_ways}")
