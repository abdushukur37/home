# def majority_element(nums:list)->int:
#     if len(nums)==0:
#         return-1
#     eng_kop=nums[0]
#     soni=0
#     for i in nums:
#         if nums.count(i)>soni:
#             soni=nums.count(i)
#             eng_kop=i
#     return eng_kop
# nums=[2,2,1,1,1,2,2]
# print(majority_element(nums))
# 2--------------
def search_by_genre(cinema:list,genre:str)->list:
    natija=[]
    for film in cinema:
        if film["genre"]==genre:
            natija.append(film)
    return natija
cinema=[
    {"title":"Avatar","genre":"Fantastika","price":40000},
    {"title":"Sherlock","genre":"Detektiv","price":30000},
    {"title":"Oq yo‘l","genre":"Drama","price":25000},
    {"title":"Dune","genre":"Fantastika","price":35000}
]
print(search_by_genre(cinema,"Fantastika"))
print(search_by_genre(cinema,"Drama"))
print(search_by_genre(cinema,"Komediya"))
print(search_by_genre([],"Boevik"))
print(search_by_genre(cinema,"Detektiv"))