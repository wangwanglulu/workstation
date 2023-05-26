def moveTower(height, fromPole, toPole, withPole):
    if height>=1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
def moveDisk(fp,tp):
    print(f"moving disk from {fp} to {tp}\n")


moveTower(5,"x","y","z")