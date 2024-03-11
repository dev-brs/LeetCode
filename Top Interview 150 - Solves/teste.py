def permutations(nums:list[int]) -> list[int]:
    answer = []
    
    if(len(nums) == 1):
        return [nums[:]]
    
    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permutations(nums)
        
        for perm in perms:
            perm.append(n)
            
        answer.extend(perms)
        nums.append(n)
        
    return answer


def main():
    my_set = [1,2,3]
    perm = permutations(my_set)    
    
    print(perm)

if __name__ == "__main__":
    main()