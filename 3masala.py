# 3-----------
def merge_unique_ids(active_users: list, new_users: list) -> list:
    natija=[]
    for i in active_users + new_users:
        if i not in natija:
            natija.append(i)
    return natija
active_users=['U1001', 'U1002', 'U1003','U1004','U1001']
new_users=['U1003','U1005','U1006','U1002','U1007']
print(merge_unique_ids(active_users, new_users))