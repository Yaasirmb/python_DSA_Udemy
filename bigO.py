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



# Space Complexity
def sum(n):
    
    """
        This function will take O(n) space complexity as since the function is recursive,
        each iteration will call itself and is reliant on the previous call. Thus the function 
        calls will be in the stack simultaniously.
    """
    if n<=0:
        return 0
    return n + sum(n-1)

# sum(3)

def pariSumSequence(n):
 
    total = 0 
    for i in range(n):
        total = total + pairSum(i, i+1)
    return total

def pairSum(a,b):
    """
        This function will take O(1) space complexity. Althought there are O(n) calls of the 
        function, it will only take O(1) space complexity.This is because the function calls 
        will not exist simultaniously in the stack.
    """
    return a+b

# print(pariSumSequence(4))

# Add vs Multiply Time complexities

def print_items(a,b):
    """
        This will take a time complexity of O(a+b). This is because while at first glance you may
        be tempted to say it's O(n) + O(n) = O(2n) time complexity, this is wrong. While it may be possible for such a case,
        that is a specific case. So what happens when a != b? Then both a & b can not = n. Thus we look at the variable indeipendently 
        and add their time complexities. So we get O(a+b) time complexity. Note it can not be simplified further than that.
    
        If your algorithm is in the form of "do this, when complete then do that" you add the time complexities.
    
    """
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

# You could add a decorator here if you want to run both functions or just rename them
def print_items(a,b):
    """
        Now this function will take O(a*b) time complexity. This is because for each iteration of the first loop, we run the nested loop.
        In this case we multiply the 2 time complexities.

        If your algorithm is in the form of "do this for each time you do that", then you multiply their time complexities.

    """
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)