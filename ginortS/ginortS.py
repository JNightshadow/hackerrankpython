if __name__=="__main__":
    string = input()
    result = sorted(string, key=lambda x: (
        x.isdigit(),  
        x.isupper(),           
        int(x) % 2 == 0 if x.isdigit() else False,  
        x                      
    ))
    print(''.join(result))
