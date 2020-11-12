def attach_head(element, input_list):
    return [element] + input_list
res=attach_head(5,attach_head(6,attach_head(7,attach_head('8', []))))
print(res)