# Code from the Big O notation section of the course.

def multiplyNumbers(n):
    """
        The time complexity for the following code
        is O(1). No matter what input we give the function,
        there will always be 1 (or a constant) operation 
        that takes place. This is the most efficient big O 
         time complexity.
    """
    return n*n

# print(multiplyNumbers(5))

def linearTimeComplexity(n):
    """
        Time compelxity grows linearly in 
        direct proportion with input data.
    """

    for i in range(n):
        print(i)

# linearTimeComplexity(10)



def dropConstants(n):
    """
        Both loops are linear in their time complexity.
        When you sum up their time complexities, you get
        n + n = 2n. Big O describes the rate of increase, therefore,
        the constants are dropped, regardless of what the constant may be.
        When performing asymtotic analysis, we are concerned only
        with the algorithim being used, and not the architecture of 
        the machine that the code is being run on. Dropping constants allows 
        us to ignore the hardware differences and focus on the algorithm at hand.
    """
     
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)
 
# dropConstants(10)

def quadraticTimeComplexity(n):
    """
        Both loops are O(n) time complexities,
        however since they are nested within eachother 
        their time complexities are multiplied. Which results in 
        n * n = n^2 time complexity, this is known as quadratic 
        time complexity. 
        
        Note: regardless of the power n is raised to i.e. n^3...n^n,
        we still call it quadratic time [ O(n^2) ] complexity in terms of Big O
        notation.
    
    """

    for i in range(n):
        for j in range(n):
            print(i,j)

def nonDominantTerms(n):
    """
        Dominat terms are the terms which are larger in value in their time
        complexities. In this example the nested loop part is O(n^2) time complexity,
        while the bottom loop is just O(n). Were we to sum up their time complexities,
        we'd get O(n^2 + n). Since n^2 is the dominant term, we drop the n, the non dominant term. 
        Therefore the final time complexity would be O(n^2).
    """

    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
        print(k)

