"""
Matrix utility library for CS1060 HW9.

Provides basic matrix operations and data structures for linear algebra computations.
"""


class Matrix:
    """
    A simple matrix data structure supporting basic operations.
    
    Attributes:
        rows: Number of rows in the matrix
        cols: Number of columns in the matrix
        data: 2D list containing matrix elements
    """
    
    def __init__(self, data):
        """
        Initialize a matrix from a 2D list.
        
        Args:
            data: List of lists representing matrix rows
            
        Raises:
            ValueError: If rows have inconsistent lengths
        """
        if not data:
            raise ValueError("Matrix cannot be empty")
        
        self.rows = len(data)
        self.cols = len(data[0])
        
        # Validate all rows have same length
        for row in data:
            if len(row) != self.cols:
                raise ValueError("All rows must have the same number of columns")
        
        self.data = [row[:] for row in data]  # Deep copy
    
    def __eq__(self, other):
        """Check matrix equality."""
        if not isinstance(other, Matrix):
            return False
        return (self.rows == other.rows and 
                self.cols == other.cols and 
                self.data == other.data)
    
    def __repr__(self):
        """String representation of the matrix."""
        return f"Matrix({self.rows}x{self.cols})"
    
    def get(self, row, col):
        """Get element at (row, col). Zero-indexed."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        return self.data[row][col]
    
    def set(self, row, col, value):
        """Set element at (row, col). Zero-indexed."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.data[row][col] = value
    
    def transpose(self):
        """
        Return the transpose of this matrix.
        
        Returns:
            New Matrix object that is the transpose
        """
        transposed_data = [[self.data[i][j] for i in range(self.rows)] 
                          for j in range(self.cols)]
        return Matrix(transposed_data)
    
    def add(self, other):
        """
        Add two matrices element-wise.
        
        Args:
            other: Another Matrix object
            
        Returns:
            New Matrix object containing the sum
            
        Raises:
            ValueError: If dimensions don't match
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        
        result = [[self.data[i][j] + other.data[i][j] 
                   for j in range(self.cols)] 
                  for i in range(self.rows)]
        return Matrix(result)
    
    def multiply(self, other):
        """
        Multiply two matrices.
        
        Args:
            other: Another Matrix object
            
        Returns:
            New Matrix object containing the product
            
        Raises:
            ValueError: If dimensions incompatible for multiplication
        """
        if self.cols != other.rows:
            raise ValueError(
                f"Cannot multiply {self.rows}x{self.cols} matrix "
                f"with {other.rows}x{other.cols} matrix"
            )
        
        result = [[sum(self.data[i][k] * other.data[k][j] 
                       for k in range(self.cols))
                   for j in range(other.cols)]
                  for i in range(self.rows)]
        return Matrix(result)
    
    def scalar_multiply(self, scalar):
        """
        Multiply matrix by a scalar.
        
        Args:
            scalar: A number to multiply all elements by
            
        Returns:
            New Matrix object with scaled elements
        """
        result = [[self.data[i][j] * scalar 
                   for j in range(self.cols)] 
                  for i in range(self.rows)]
        return Matrix(result)
    
    def trace(self):
        """
        Calculate the trace (sum of diagonal elements).
        
        Returns:
            Sum of diagonal elements
            
        Raises:
            ValueError: If matrix is not square
        """
        if self.rows != self.cols:
            raise ValueError("Trace is only defined for square matrices")
        
        return sum(self.data[i][i] for i in range(self.rows))
