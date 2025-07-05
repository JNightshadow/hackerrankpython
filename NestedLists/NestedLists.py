if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    minscore = float('inf')
    secondlowest = float('inf')
    
    for row in records:
        if minscore>row[1]:
            secondlowest = minscore
            minscore = row[1]
        elif row[1]>minscore and row[1]<secondlowest:
            secondlowest = row[1]
    studentlist = [record[0] for record in records if record[1]==secondlowest]
    studentlist.sort()
    print(*studentlist,sep="\n")
