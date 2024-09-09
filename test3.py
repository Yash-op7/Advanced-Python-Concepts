s = 'abc!, vbd, sdaoj, ,ijf ds   fad'
gen_obj = (clip for clip in s.split(sep=' ') if clip)

def check(clip):
    # Membership checks
    for ch in clip:
        if ch.isdigit():
            return False
        elif ch.isalpha():
            if ch.lower() != ch:
                return False
        else:
            if (ch != '-') or ()
    # dash check
    # special symbol check

cnt = 0
for clip in gen_obj:
    if check(clip):
        cnt += 1

print(cnt)