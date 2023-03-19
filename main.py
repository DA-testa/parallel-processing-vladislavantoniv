import heapq
# python3

def parallel_processing(n, m, data):
    output = []
    aw=[None]*m
    st=[None]*m
    nft=[0]*n
    for i in range(n):
        heapq.heappush(output,(nft[i],i))
    for i in range(len(data)):
        new=0
        (k,new)=heapq.heappop(output)
        aw[i]=new
        st[i]=nft[new]
        nft[new]=nft[new]+data[i]
        heapq.heappush(output,(nft[new],new))
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(len(data)):
        print(aw[i],st[i])

def main():
    # TODO: create input from keyboard
    arr=input()
    sp=arr.split(' ')
    n=int(sp[0])
    m=int(sp[1])
    data=list(map(int,input().split()))
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count


    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line


if __name__ == "__main__":
    main()
