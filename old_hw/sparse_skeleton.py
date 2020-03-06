import numpy as np

### A library of functions for sparse vectors 

# Print out a sparse vector a 
def sprint(a):
    # TODO: implement the code
    return

# Scale sparse vector a by scalar s 
def sscale(a, s):
    # TODO: implement the code
    return a

# Compute dot product between sparse vector a and vector b
def ssdot(a, b):
    dot_prod=-1
    # TODO: implement the code
    return dot_prod

# Compute hadamard product between sparse vector a and vector b 
def sshadamard(a, b):
    had_prod=[]
    # TODO: implement the code
    return had_prod

# Compute sum of entries of sparse vector a 
def ssum(a):
    sum_a=-1
    # TODO: implement the code
    return sum_a

# Compute s.a + b, where s is a scalar and a and b are sparse vectors. 
def ssaxpy(s, a, b):
    axpy=[]
    # TODO: implement the code
    return axpy

# Compute max and argmax over elements of sparse vector a 
def smax(a):
    smax=-1
    sargmax=-1
    # TODO: implement the code
    return smax,sargmax

# Compute min and argmin over elements of sparse vector a 
def smin(a):
    smin=-1
    sargmin=-1
    # TODO: implement the code
    return smin,sargmin

# Compute max and argmax over absolute values of elements of sparse vector a 
def sabs_max(a):
    sabs_max=-1
    sabs_argmax=-1
    # TODO: implement the code
    return sabs_max,sabs_argmax

# Clip elements of sparse vector a such that all elements lie between lower bound lb and upper bound ub 
def sclip(a, lb, ub):
    # TODO: implement the code
    return a

# Return the total number of non-zero elements in a sparse vector a
def nnz(a):
    nnz_a=-1
    # TODO: implement the code
    return nnz_a

# Return the maximum index in a
def smax_idx(a):
    max_idx_a=-1
    # TODO: implement the code
    return max_idx_a
 
### A library of functions for sparse matrices

# Print out a sparse matrix A
def smatprint(A):
    # TODO: implement the code
    return

# Multiply a sparse matrix A with a sparse vector b
def smatmult(A, b):
    Ab=[]
    # TODO: implement the code
    return Ab

# Multiply a sparse matrix A with a numpy vector b
def matmult(A, b):
    Ab=[]
    # TODO: implement the code
    return Ab

# Return the total number of non-zero elements in a sparse matrix A
def smatnnz(A):
    nnz_A=-1
    # TODO: implement the code
    return nnz_A

# Return the maximum index of a row in A
def smat_max_row_idx(A):
    max_row_idx_A=-1
    # TODO: implement the code
    return max_row_idx_A

# Return the size (that is, number of rows and columns) of the matrix A
def smatsize(A):
    rows_A=-1
    cols_A=-1
    # TODO: implement the code
    return rows_A, cols_A

# Read in a sparse matrix from a libsvm file
def smatread(fname):
    A=[]
    # TODO: implement the code
    return A

# Extract and return the idx row of A
def smat_get_row(idx):
    a=[]
    # TODO: implement the code
    return a

def main():

    # Create two sparse vectors:
    # a = [1, 0, 1, 0, 2, 0, 0, 1, 3, 0]
    # b = [3, -1, 0, 0, 2, 1, 0, 0, 1, 4]
    
    # TODO: implement the code for creating the vectors 
    
    
    sprint(a)
    sprint(b)
    
    a=sscale(a, 1.2)
    print "after scaling a by 1.2"
    sprint(a)
  
    print "dot product between a and b:", ssdot(a, b)
  
    c=sshadamard(a, b);
    print "Hadamard product between a and b:"
    sprint(c)
    
    print "sum of entries in c:", ssum(c)

    print "sum of elements of a:", ssum(a)
  
    c=ssaxpy(-1.0, b, a)
    print "a - b:"
    sprint(c)
  
    print "max and argmax of a:", smax(a)

    print "min and argmin of a:", smin(a)

    a=sscale(a, -1.0)
    print "a after scaling with -1.0:"
    sprint(a);

    print "max and argmax of a after scaling:", smax(a)
    print "abs max and abs argmax of a:", sabs_max(a) 
  
    sclip(a, 0.0, 1.0)
    print "a after clipping:"
    sprint(a);

    print "number of non-zeros in a:", nnz(a)
    print "number of non-zeros in c:", nnz(c)

    print "max_idx in a:", smax_idx(a)
    print "max_idx in c:", smax_idx(c)

    # Now let us test our matrix functions
    
    # TODO: set fname to point to the file a9a
    fname=""
    A=smatread(fname)
    
    smatprint(A)

    print "size of A:", smatsize(A)
    print "maximum row idx in A:", smat_max_row_idx(A)
    print "number of non-zeros in A:", smatnnz(A)
    
    cols=smat_max_row_idx(A)
    x=np.ones(cols+1)
    Ax=matmult(A, x)
    print "A multiplied with vector of all ones:"
    sprint(Ax)
    

    y=smat_get_row(10)
    Ay=smatmult(A,y)
    print "A multiplied with its eleventh row:"
    sprint(Ay)
    return

    
if __name__ == "__main__":
    main()

