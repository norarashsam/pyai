def tower(h,fp,tp,wp):
    if h>=1:
        tower(h-1,fp,wp,tp)
        disk(fp,tp)
        tower(h-1,wp,tp,fp)

def disk(fp1,tp1):
    print("moving disk from ",fp1," to ",tp1)

tower(3,"A","B","C")
