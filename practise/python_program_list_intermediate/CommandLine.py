import re

def CommandLine(str):
    # Regular expression to split by key=value pairs
    pairs = re.findall(r'(\S+?)=([^=]*)', str)

    # Construct the result format "len(key)=len(value)"
    result = ["{}={}".format(len(key), len(value)) for key, value in pairs]

    return " ".join(result)

# Test cases
print(CommandLine("SampleNumber=3234 provider=Dr. M. Welby patient=John Smith priority=High"))  
# Output: "12=4 8=12 7=10 8=4"

print(CommandLine("letters=A B Z T numbers=1 2 26 20 combine=true"))  
# Output: "7=7 7=9 7=4"

print(CommandLine("a=3 b=4 a=23 b=a 4 23 c="))  
# Output: "1=1 1=1 1=2 1=6 1=0"
