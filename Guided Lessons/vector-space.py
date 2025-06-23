class R2Vector:
    def __init__(self, *, x, y):
        """
        Initializes an R2Vector instance with x and y coordinates.

        Parameters:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

    def norm(self):
        """
        Calculates and returns the Euclidean norm of the vector.

        Returns:
            float: The Euclidean norm of the vector.
        """
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        """
        Returns a string representation of the R2Vector instance.

        The string representation includes the x and y coordinates as a tuple.

        Returns:
            str: A string representation of the R2Vector instance.
        """
        return str(tuple(getattr(self, i) for i in vars(self))) # getattr(self, i) return the value of the attribute i

    def __repr__(self):
        """
        Returns a string representation of the R2Vector instance suitable for debugging.

        The string representation shows the class name and the attribute names and values.

        Returns:
            str: A string representation of the R2Vector instance.
        """
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})' # __class__.__name__ return the name of the class

    def __add__(self, other):
        """
        Adds two R2Vector instances and returns a new R2Vector instance with the sum of the coordinates.

        Parameters:
            other (R2Vector): Another R2Vector instance to add.

        Returns:
            R2Vector: A new R2Vector instance with the sum of the coordinates.

        Raises:
            NotImplemented: If the other object is not an instance of R2Vector.
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        """
        Subtracts two R2Vector instances and returns a new R2Vector instance with the difference of the coordinates.

        Parameters:
            other (R2Vector): Another R2Vector instance to subtract.

        Returns:
            R2Vector: A new R2Vector instance with the difference of the coordinates.

        Raises:
            NotImplemented: If the other object is not an instance of R2Vector.
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        """
        Multiplies two R2Vector instances and returns a new R2Vector instance with the product of the coordinates.

        If the other object is an integer or a float, it multiplies all coordinates of the current instance with the other object.

        If the other object is also an instance of R2Vector, it returns the sum of the product of the corresponding coordinates of the current instance and the other object.

        Parameters:
            other (int, float, or R2Vector): The other object to multiply.

        Returns:
            R2Vector or int or float: A new R2Vector instance with the product of the coordinates or the sum of the product of the coordinates.

        Raises:
            NotImplemented: If the other object is not an integer, a float, or an instance of R2Vector.
        """
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other):
        """
        Compares two R2Vector instances for equality.

        Parameters:
            other (R2Vector): Another R2Vector instance to compare.

        Returns:
            bool: True if the coordinates of the two R2Vector instances are equal, False otherwise.

        Raises:
            NotImplemented: If the other object is not an instance of R2Vector.
        """
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other):
        """
        Compares two R2Vector instances for inequality.

        Parameters:
            other (R2Vector): Another R2Vector instance to compare.

        Returns:
            bool: True if the coordinates of the two R2Vector instances are not equal, False otherwise.

        Raises:
            NotImplemented: If the other object is not an instance of R2Vector.
        """
        return not self == other

    def __lt__(self, other):
        """
        Compares two R2Vector instances for less than.

        The comparison is based on the Euclidean norm of the vectors.

        Parameters:
            other (R2Vector): Another R2Vector instance to compare.

        Returns:
            bool: True if the Euclidean norm of the current instance is less than the Euclidean norm of the other instance, False otherwise.

        Raises:
            NotImplemented: If the other object is not an instance of R2Vector.
        """
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        """
        Compares two R2Vector instances for greater than.

        The comparison is based on the Euclidean norm of the vectors.

        Parameters:
            other (R2Vector): Another R2Vector instance to compare.

        Returns:
            bool: True if the Euclidean norm of the current instance is greater than the Euclidean norm of the other instance, False otherwise.

        Raises:
            NotImplemented: If the other object is not an instance of R2Vector.
        """
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        """
        Compares two R2Vector instances for less than or equal.

        The comparison is based on the Euclidean norm of the vectors.

        Parameters:
            other (R2Vector): Another R2Vector instance to compare.

        Returns:
            bool: True if the Euclidean norm of the current instance is less than or equal to the Euclidean norm of the other instance, False otherwise.

        Raises:
            NotImplemented: If the other object is not an instance of R2Vector.
        """
        return not self > other

    def __ge__(self, other):
        """
        Compares two R2Vector instances for greater than or equal.

        The comparison is based on the Euclidean norm of the vectors.

        Parameters:
            other (R2Vector): Another R2Vector instance to compare.

        Returns:
            bool: True if the Euclidean norm of the current instance is greater than or equal to the Euclidean norm of the other instance, False otherwise.

        Raises:
            NotImplemented: If the other object is not an instance of R2Vector.
        """
        return not self < other

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        """
        Initializes a new R3Vector instance with x, y and z coordinates.

        Parameters:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
            z (float): The z-coordinate of the vector.
        """
        super().__init__(x=x, y=y) # call the constructor of the parent class
        self.z = z
        
    def cross(self, other):
        """
        Computes the cross product of the current R3Vector instance with another R3Vector instance.

        The cross product is a vector perpendicular to both input vectors, calculated using the
        determinants of the components.

        Parameters:
            other (R3Vector): Another R3Vector instance to compute the cross product with.

        Returns:
            R3Vector: A new R3Vector instance representing the cross product of the two vectors.

        Raises:
            NotImplemented: If the other object is not an instance of R3Vector.
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        return self.__class__(**kwargs)
    
    
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
v6 = v1.cross(v2)