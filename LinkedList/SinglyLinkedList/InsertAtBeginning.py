def insertAtFirst(val,head):
    new_node = {"value":val,"next":head}
    curr = new_node
    while curr:
        print(curr["value"],end=" -> ")
        curr = curr["next"]
    

node1 = {"value":10,"next":None}
node2 = {"value":20,"next":None}
node3 = {"value":30,"next":None}

node1["next"] = node2
node2["next"] = node3
val = 5
head = node1
print(insertAtFirst(val,head))