from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def sortPair(val1,val2):
    if val1 > val2:
        return val2,val1
    else:
        return val1,val2
def copyStructure(x1,y1,z1,x2,y2,z2):
    #
    x1,x2=sortPair(x1,x2)
    y1,y2=sortPair(y1,y2)
    z1,z2=sortPair(z1,z2)

    width=x2-x1
    height=y2-y1
    length=z2-z1

    structure=[]

    print("Please wait..........")

    mc.getBlocks(x1,y1,z1,x2,y2,z2)
