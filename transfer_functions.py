from math import exp
def hardlim(n):
    """
    Hard Limit Transfer Function

    :param int n:Net Input of Neuron
    :return: Compute Heaviside step function 
    :rtype: int
    """
    if n<0:
        return 0
    else:
        return 1
def hardlims(n):
    """
    Symmetrical Hard Limit Transfer Function

    :param int n:Net Input of Neuron
    :return: Compute Heaviside step function 
    :rtype: int
    """
    if n<0:
        return -1
    else:
        return 1  
def purelin(n):
    """
    Linear Transfer Function

    :param int n:Net Input of Neuron
    :return: Compute purelin(n)=n
    :rtype: int
    """
    return n
def logsig(n):
    """
    Logistic Sigmoid Function (Numerically Stabilized)
    
    :param int n:Net Input of Neuron
    :return: Compute logsig(p) = log(p/(1-p)) in range (-1,1)
    :rtype: float
    """
    if n>=0:
        return 1/(1+exp(-n))
    else:
        x = exp(n)
        return x/1+x
