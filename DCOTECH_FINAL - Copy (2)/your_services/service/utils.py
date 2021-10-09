def avarage_rating(list_rating):
    
    if len(list_rating)==0:
        return 0
    else:
        return(round(sum(list_rating)/len(list_rating)))

def page_devider(l):
    num_pages=[]
    pages=l//4+1
    for i in range(0,pages):
        num_pages.append(i)
    return num_pages
    