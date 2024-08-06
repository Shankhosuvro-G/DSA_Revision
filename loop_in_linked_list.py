def detect_loop(head):
    itr=head
    mp=set()
    while itr:
        if itr in mp:
            return True
        mp.add(itr)
        itr=itr.next
    return False