
import re
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        creditCard = input()
        pattern = r"[456]\d{3}(-?\d{4}){3}$"
        if(not re.match(pattern,creditCard)):
            print("Invalid")
            continue
        repeatCheckPattern = r"(\d)\1{3,}"
        removedsymbols = creditCard.replace("-","")
        if( re.search(repeatCheckPattern,removedsymbols)):
            print("Invalid")
            continue
        else:
            print("Valid")
            
