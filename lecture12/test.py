import matplotlib.pyplot as plt
   
def threepoints(z):
    x1=z[0][0]
    y1=z[0][1]
    x2=z[1][0]
    y2=z[1][1]
    y=z[2][1]
    x=z[2][0]
    if (x2-x1)*y-(y2-y1)*x-y1*x2+y2*x1==0:
       print('They lie on a straight line.')
    else:
        plt.plot([z[0][0],z[1][0]],[z[0][1],z[1][1]],c="black")
        plt.plot([z[1][0],z[2][0]],[z[1][1],z[2][1]],c="black")
        plt.plot([z[0][0],z[2][0]],[z[0][1],z[2][1]],c="black")
        plt.show()

n=[[1,1],[1,2],[1,3]]
m=[[1,1],[2,3],[4,2]]
threepoints(n)
threepoints(m)