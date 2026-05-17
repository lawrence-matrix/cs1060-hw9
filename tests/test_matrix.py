"""
Comprehensive test suite for matrix utility library.

Tests cover initialization, access, operations, and error handling.
"""

import pytest
from src.matrix import Matrix


class TestMatrixInitialization:
    """Test matrix creation and validation."""
    
    def test_create_simple_matrix(self):
        """Test creating a basic matrix."""
        data = [[1, 2, 3], [4, 5, 6]]
        m = Matrix(data)
        assert m.rows == 2
        assert m.cols == 3
        assert m.data == data
    
    def test_create_1x1_matrix(self):
        """Test creating a 1x1 matrix."""
        m = Matrix([[42]])
        assert m.rows == 1
        assert m.cols == 1
        assert m.get(0, 0) == 42
    
    def test_create_empty_matrix_raises(self):
        """Test that empty matrix raises error."""
        with pytest.raises(ValueError):
            Matrix([])
    
    def test_inconsistent_row_lengths_raises(self):
        """Test that inconsistent row lengths raise error."""
        with pytest.raises(ValueError):
            Matrix([[1, 2], [3, 4, 5]])
    
    def test_matrix_is_copied(self):
        """Test that matrix data is copied, not referenced."""
        data = [[1, 2], [3, 4]]
        m = Matrix(data)
        data[0][0] = 999  # Modify original
        assert m.get(0, 0) == 1  # Matrix should be unchanged


class TestMatrixAccess:
    """Test matrix element access."""
    
    def setup_method(self):
        """Set up test matrices."""
        self.m = Matrix([[1, 2, 3], [4, 5, 6]])
    
    def test_get_valid_element(self):
        """Test getting elements within bounds."""
        assert self.m.get(0, 0) == 1
        assert self.m.get(0, 2) == 3
        assert self.m.get(1, 1) == 5
    
    def test_get_out_of_bounds_raises(self):
        """Test that out of bounds access raises IndexError."""
        with pytest.raises(IndexError):
            self.m.get(2, 0)
        with pytest.raises(IndexError):
            self.m.get(0, 3)
        with pytest.raises(IndexError):
            self.m.get(-1, 0)
    
    def test_set_valid_element(self):
        """Test setting elements within bounds."""
        self.m.set(0, 0, 99)
        assert self.m.get(0, 0) == 99
        self.m.set(1, 2, -5)
        assert self.m.get(1, 2) == -5
    
    def test_set_out_of_bounds_raises(self):
        """Test that out of bounds set raises IndexError."""
        with pytest.raises(IndexError):
            self.m.set(2, 0, 0)
        with pytest.raises(IndexError):
            self.m.set(0, 3, 0)


class TestMatrixEquality:
    """Test matrix equality comparison."""
    
    def test_equal_matrices(self):
        """Test that identical matrices are equal."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2], [3, 4]])
        assert m1 == m2
    
    def test_different_data_not_equal(self):
        """Test that matrices with different data are not equal."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2], [3, 5]])
        assert m1 != m2
    
    def test_different_dimensions_not_equal(self):
        """Test that matrices with different dimensions are not equal."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2, 3], [4, 5, 6]])
        assert m1 != m2
    
    def test_not_equal_to_non_matrix(self):
        """Test that matrix is not equal to non-matrix objects."""
        m = Matrix([[1, 2], [3, 4]])
        assert m != "not a matrix"
        assert m != 42
        assert m != None


class TestMatrixTranspose:
    """Test matrix transpose operation."""
    
    def test_transpose_2x3_matrix(self):
        """Test transposing a 2x3 matrix."""
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        t = m.transpose()
        assert t.rows == 3
        assert t.cols == 2
        assert t.data == [[1, 4], [2, 5], [3, 6]]
    
    def test_transpose_square_matrix(self):
        """Test transposing a square matrix."""
        m = Matrix([[1, 2], [3, 4]])
        t = m.transpose()
        assert t.data == [[1, 3], [2, 4]]
    
    def test_transpose_1x1_matrix(self):
        """Test transposing a 1x1 matrix."""
        m = Matrix([[42]])
        t = m.transpose()
        assert t.rows == 1
        assert t.cols == 1
        assert t.get(0, 0) == 42
    
    def test_double_transpose_equals_original(self):
        """Test that transposing twice gives original matrix."""
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        assert m == m.transpose().transpose()


class TestMatrixAddition:
    """Test matrix addition operation."""
    
    def test_add_same_dimensions(self):
        """Test adding matrices with same dimensions."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1.add(m2)
        assert result.data == [[6, 8], [10, 12]]
    
    def test_add_with_negative_values(self):
        """Test addition with negative values."""
        m1 = Matrix([[1, -2], [3, 4]])
        m2 = Matrix([[-1, 2], [-3, -4]])
        result = m1.add(m2)
        assert result.data == [[0, 0], [0, 0]]
    
    def test_add_incompatible_dimensions_raises(self):
        """Test that adding matrices with different dimensions raises error."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2, 3]])
        with pytest.raises(ValueError):
            m1.add(m2)
    
    def test_add_single_element_matrices(self):
        """Test adding 1x1 matrices."""
        m1 = Matrix([[5]])
        m2 = Matrix([[3]])
        result = m1.add(m2)
        assert result.get(0, 0) == 8


class TestMatrixMultiplication:
    """Test matrix multiplication operation."""
    
    def test_multiply_2x2_matrices(self):
        """Test multiplying two 2x2 matrices."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1.multiply(m2)
        # [1*5 + 2*7, 1*6 + 2*8] = [19, 22]
        # [3*5 + 4*7, 3*6 + 4*8] = [43, 50]
        assert result.data == [[19, 22], [43, 50]]
    
    def test_multiply_2x3_by_3x2(self):
        """Test multiplying 2x3 by 3x2 matrix."""
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[7, 8], [9, 10], [11, 12]])
        result = m1.multiply(m2)
        # [1*7 + 2*9 + 3*11, 1*8 + 2*10 + 3*12] = [58, 64]
        # [4*7 + 5*9 + 6*11, 4*8 + 5*10 + 6*12] = [139, 154]
        assert result.data == [[58, 64], [139, 154]]
    
    def test_multiply_with_identity(self):
        """Test multiplying by identity matrix."""
        m = Matrix([[1, 2], [3, 4]])
        identity = Matrix([[1, 0], [0, 1]])
        result = m.multiply(identity)
        assert result == m
    
    def test_multiply_incompatible_dimensions_raises(self):
        """Test that incompatible dimensions raise error."""
        m1 = Matrix([[1, 2], [3, 4]])  # 2x2
        m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 3x3
        with pytest.raises(ValueError):
            m1.multiply(m2)


class TestScalarMultiplication:
    """Test scalar multiplication operation."""
    
    def test_scalar_multiply_by_integer(self):
        """Test multiplying matrix by an integer."""
        m = Matrix([[1, 2], [3, 4]])
        result = m.scalar_multiply(3)
        assert result.data == [[3, 6], [9, 12]]
    
    def test_scalar_multiply_by_zero(self):
        """Test multiplying matrix by zero."""
        m = Matrix([[1, 2], [3, 4]])
        result = m.scalar_multiply(0)
        assert result.data == [[0, 0], [0, 0]]
    
    def test_scalar_multiply_by_negative(self):
        """Test multiplying matrix by negative scalar."""
        m = Matrix([[1, -2], [3, 4]])
        result = m.scalar_multiply(-2)
        assert result.data == [[-2, 4], [-6, -8]]
    
    def test_scalar_multiply_by_float(self):
        """Test multiplying matrix by float."""
        m = Matrix([[2, 4], [6, 8]])
        result = m.scalar_multiply(0.5)
        assert result.data == [[1.0, 2.0], [3.0, 4.0]]


class TestMatrixTrace:
    """Test trace operation (sum of diagonal elements)."""
    
    def test_trace_2x2_matrix(self):
        """Test trace of a 2x2 matrix."""
        m = Matrix([[1, 2], [3, 4]])
        assert m.trace() == 5
    
    def test_trace_3x3_matrix(self):
        """Test trace of a 3x3 matrix."""
        m = Matrix([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
        assert m.trace() == 6
    
    def test_trace_1x1_matrix(self):
        """Test trace of a 1x1 matrix."""
        m = Matrix([[42]])
        assert m.trace() == 42
    
    def test_trace_with_negative_values(self):
        """Test trace with negative diagonal values."""
        m = Matrix([[1, 2], [3, -4]])
        assert m.trace() == -3
    
    def test_trace_non_square_matrix_raises(self):
        """Test that trace of non-square matrix raises error."""
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        with pytest.raises(ValueError):
            m.trace()


class TestMatrixIntegration:
    """Integration tests for multiple operations."""
    
    def test_complex_matrix_expression(self):
        """Test combining multiple operations."""
        m1 = Matrix([[1, 0], [0, 1]])  # Identity
        m2 = Matrix([[2, 3], [4, 5]])
        
        # (m2 * 2) + (m2.transpose())
        scaled = m2.scalar_multiply(2)
        transposed = m2.transpose()
        result = scaled.add(transposed)
        
        # [[2, 3], [4, 5]] * 2 = [[4, 6], [8, 10]]
        # [[2, 3], [4, 5]] transposed = [[2, 4], [3, 5]]
        # [[4, 6], [8, 10]] + [[2, 4], [3, 5]] = [[6, 10], [11, 15]]
        assert result.data == [[6, 10], [11, 15]]
