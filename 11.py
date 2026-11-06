def majority_element(nums:list)->int:
    if len(nums)==0:
        return-1
    eng_kop=nums[0]
    soni=0
    for i in nums:
        if nums.count(i)>soni:
            soni=nums.count(i)
            eng_kop=i
    return eng_kop
nums=[2,2,1,1,1,2,2]
print(majority_element(nums))