# Fill in the two functions and the two classes below (look for the TODO comments).
#
# Parts 1 and 2 must use RECURSION - a function that calls itself on a smaller version
# of the problem. Do NOT use a loop for those two.
#
# Do not rename anything, because the automated tests use these names.


def count_occurrences(target, values):

    count = 0;
    if(len(values) == 0):
        return 0
    
    if(values[0] == target):
        count = count + 1
    
    return count + count_occurrences(target,values[1:])
    

def is_sorted(values):

    if(len(values) <= 1):
        return True
    
    if(values[0] > values[1]):
        return False
        
    return is_sorted(values[1:])


class Rectangle:
    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height

    def perimeter(self):

        return 2 * (self.width + self.height)

    def __str__(self):

        return (f"{self.width}x{self.height}")


class Square(Rectangle):   # Part 4 - stretch (optional)
    def __init__(self, side):

        super().__init__(side, side)


def main():
    # Optional scratch space - try your work here, then run: python lab07.py
    #print(count_occurrences('a', ['a',1, 2, 2, 3, 2]))   # 3
    #print(is_sorted([1, 1, 3]))                    # True
    #print(Rectangle(3, 4).area())                  # 12
    #print(Square(5))                               # 5x5
    pass


if __name__ == "__main__":
    main()
