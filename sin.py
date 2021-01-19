import argparse
from random import random
from transfer_functions import hardlim,purelin,logsig
def neuron(w,b,p,transfer_function=hardlim):
    """
    Single Input Neuron

    :param int w: scalar weight of neuron
    :param int b: scalar bias of neuron
    :param int p: scalar input of neuron
    :param transfer_function: linear or non-linear transfer function for neuron
    :type transfer_function: callable
    :return: scalar neuron output a
    :rtype: int
    """
    return transfer_function(w*p+b)


def main():
    parser = argparse.ArgumentParser(prog="sin",description = "Neural Network Design: Single-Input Neuron")
    parser.add_argument('--p',type=int, default=1.0-random(), metavar="Input",
                        help="Input for Neuron")
    parser.add_argument('--w',type=int, default=1.0-random(),metavar="Weight",
                        help="Initial Weight for Neuron")
    parser.add_argument('--b',type=int, default=1.0-random(),metavar="Bias",
                        help="Initial Bias for Neuron")
    parser.add_argument('--a',type=str, default="hardlim",metavar="Transfer_Func",
                        help="Transfer function used for Neuron", choices = ["hardlim","purelin"])
    args = parser.parse_args()
    
    transfer_functions = {
        "hardlim":hardlim,
        "purelin":purelin,
        "logsig":logsig
        }
    try:
        if args.a in transfer_functions:
            tf = transfer_functions[args.a]
        else:
            raise ValueError("Incorrect Transfer Function Specified. Please specify from the given list in help by sin --help")
        out = neuron(args.w,args.b,args.p,tf)
        print(out)
        return 0
    except ValueError as ve:
        print(ve)
    except Exception as err:
        print(err)
if __name__=="__main__":
    main()
    
    
    
    
    
