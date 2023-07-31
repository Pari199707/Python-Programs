def filterFunc(x):
    if x%2==0:
        return False
    return True

def main():
    nums=[1,2,3,4,5]
    odds = list(filter(filterFunc, nums))
    print(odds)

if __name__ == "__main__":
    main()

