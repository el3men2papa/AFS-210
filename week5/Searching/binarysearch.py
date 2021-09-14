# binary search on a sorted list
def binary_search(list, fst_elm_idx, lst_elm_idx, term):
        
        if (lst_elm_idx < fst_elm_idx):
                return False
        else:
                mid = fst_elm_idx + ((lst_elm_idx - fst_elm_idx) // 2)
                
                if (list[mid] > term):
                        return binary_search(list, fst_elm_idx, mid - 1, term)
                elif (list[mid] < term):
                        return binary_search(list, mid + 1, lst_elm_idx, term)
                else:
                        return True
    
list1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(binary_search(list1, 0, len(list1)-1, 31))
print(binary_search(list1, 0, len(list1)-1, 77))
print(binary_search(list2, 0, len(list2)-1, "Delta"))