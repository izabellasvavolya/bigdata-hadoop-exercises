import sys
cw=None
cc=0
for line in sys.stdin:
    p=line.strip().split("\t",1)
    if len(p)!=2: continue
    w,c=p[0],p[1]
    try: c=int(c)
    except: continue
    if cw==w:
        cc+=c
    else:
        if cw is not None: print(f"{cw}\t{cc}")
        cw=w
        cc=c
if cw is not None: print(f"{cw}\t{cc}")
