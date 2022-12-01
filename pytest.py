
import xloil as xlo
import numpy as np
#import privugger as pv
from xloil.gui.wx import wx_thread
import wx


#app = xlo.app()

@xlo.func
def Greeting(who):
    return "Hello  " + who
	
@xlo.func
def Adder(x, y):
    return x + y
	
def str_cat(p1,p2):
    return f"{p1}:{p2}"

def get_size(range):
    #if(len(p1) == 2):
    #    print(f"Error position 1 incorrect length: {p1}" )
    #if(len(p2) == 2):
    #    print(f"Error position 1 incorrect length: {p2}" )
    #A1:B2
    x1 = ord(range[0].upper())
    x2 = ord(range[3].upper())
    y1 = int(range[1])
    y2 = int(range[4])
    return (x2-x1,y2-y1)

xlo.app().Range("A1", "B2").Value = ((1, 2), (3, 4))
    

@xlo.func(args={'x': "2-dim array to return"})
def pyTestArr2d(x: xlo.Array(float)) -> xlo.Array(float):
	return x

@xlo.func
def getRange(p1, p2):
	#write to range: xlo.Range("A1:B2").value = np.array([[1, 2], [3, 4]])
	#reading range xlo.Range("A1:C1").value
    return sum(xlo.Range(p1 + ":" + p2).value)

@xlo.func
def Gen_data(range):
    #xlo.app().Range("A1", "B2").Value = ((1, 2), (3, 4))
    return 1
    #dim = get_size(range)
    #xlo.Range(range).value = np.random.rand(dim[0],dim[1])

if __name__ == "__main__":
    get_size("A1:A2")

#program = pv.Program('output',dataset=ds, output_type=pv.Float, function=dp_program)
#trace = pv.infer(program, cores=4, chains=2, draws=20000, method='pymc3')


#xlo.Range("A1:B2").value = np.array([[1, 2], [3, 4]])