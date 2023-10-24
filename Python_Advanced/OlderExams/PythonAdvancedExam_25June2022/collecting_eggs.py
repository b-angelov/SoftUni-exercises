eggs = list(map(int,input().split(", ")))
paper_pieces = list(map(int,input().split(", ")))
filled_boxes = 0

while eggs and paper_pieces:
    egg = eggs.pop(0)
    if egg <= 0 or egg == 13:
        if egg == 13:
            paper_pieces[0],paper_pieces[-1] = paper_pieces[-1],paper_pieces[0]
        continue
    paper = paper_pieces.pop()
    wrapped = egg + paper
    if wrapped > 50:
        continue
    filled_boxes += 1

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str,eggs))}")
if paper_pieces:
    print(f"Pieces of paper left: {', '.join(map(str,paper_pieces))}")

