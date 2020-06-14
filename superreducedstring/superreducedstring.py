def super_reduced_string(s):
    """Reduce the string
    This function reduces the string by carrying out a series of operations.
    In each operation, the adjacent letters that match are deleted.

    :param str s: input string entered by user

    :return (str) reduced string
    """

    #If string contains as single character or if string is empty, return the input string itself

    stack = []

    for char in s:
        #compare if the char and its adjacent char are same
        if (stack and stack[-1] == char):
            stack.pop()

        else:
            stack.append(char)

    # If string contains as single character, return 'Empty String'
    return ('Empty String' if len(stack)==0 else ''.join(stack))


if __name__ == '__main__':
    print('Enter the string')
    s = input()
    reducedString = super_reduced_string(s)
    print("Reduced String is", reducedString)