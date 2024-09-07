

def solve():
    # print most freq char in a str
    s = 'abiudfjnsafsajnfdxuichvijoneknsafklansdfnapsdfniwenfsdakfn'
    cnt = {}
    for c in s:
        cnt.setdefault(c, 0)
        cnt[c] += 1
    print(cnt)
    maximum_frequent_alpha_char = max({c for c in s if c.isalpha()}, key=s.count)
    print(f'{maximum_frequent_alpha_char = }')

def main():
    solve()


if __name__=='__main__':
    main()
