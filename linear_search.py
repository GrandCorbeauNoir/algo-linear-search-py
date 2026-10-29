def linear_search(value_to_find, array_to_search_through):
    
    for idx in range(len(array_to_search_through)):
        if value_to_find == array_to_search_through[idx]:
           return idx
       
    return None
       
    
    
   

def linear_search_global(value_to_find, array_to_search_through):
            
    all_ids = []
    for idx in range(len(array_to_search_through)):
        if value_to_find == array_to_search_through[idx]:
                 all_ids.append(idx)
                 
    if len(all_ids):
       return all_ids
    else:
       return None
    
            
               
            
        
