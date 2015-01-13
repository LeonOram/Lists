##def get_rows_col(list_in):
##    rows = len(list_in)
##    cols = len(list_in[0])
##    print(rows,cols)

##def get_max(lists):
##    max_len=[]
##    
##    for list_count,list_ in enumerate(lists):
##        max_=0
##        max_len.append(0)
##        for index,item in enumerate(list_):
##            if len(str(item))> max_:
##                max_=len(str(item))
##        max_len.append(max_)
##    print(max_len)


def get_max_col(lists,col):
    max_len=0
    for list_ in lists:
        len_ = len(str(list_[col]))
        if len_ > max_len:
            max_len=len_
    return max_len

def loop_col_len(lists):
    col_len=[]
    for count,row in enumerate(lists[0]):
        col_len.append(get_max_col(lists,count))
    draw_table(lists,col_len)

def draw_table(lists,col_len):
    for list_ in lists:
        row = "|"
        for index,item in enumerate(list_):
            insert ="{0:<{1}}".format(str(item),col_len[index])
            row = row + insert
            row = row + "|"
        print("-"*len(row))
        print(row)
    print("-"*len(row))
    
players =[
    ["k1llmAchine",51,49,3],
    ["bob2247",555,999,54],
    ["hAxOr12",72,30,345]
    ]

loop_col_len(players)
