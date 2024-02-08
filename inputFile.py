#this is a test to see if all types of comments are removed

def test1() :

    '''
    This is a multi line comment with single quotes
    giberish is inserted here
    '''

    print("Hello")  #This is also a comment

    """ this is a string literal that is treated like a comment"""
    var1 = "This should not be deleted."        """ This should be concatenated"""
    print(var1)    #This is also a comment

    """
    # Even though it looks like a comment, it is considered a string
    # This should also be deleted though as this string is not added to a variable """

    var2 = "This is a variable\
    which should not be deleted"
    print(var2)

    return

def test2() :

    '''There is not much more to test'''    #But this whole line should be deleted
    # If that last line wasn't deleted, Houston We Have a Problem
    
    """
    
    Ok, I think we are done
    
    """
    return