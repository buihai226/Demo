if __name__ == '__main__':
    test = int(input())
    date = {}
    for _ in range(test):
        s = input().split()
        if s[3] == 'OUT':
            continue
        else:
            if s[2] == '5':
                if s[1] == 'Xe_con':
                    if s[4] in date:
                        date[s[4]] += 10000
                    else:
                        date[s[4]] = 0
                        date[s[4]] += 10000
            if s[2] == '7':
                if s[1] == 'Xe_con':
                    if s[4] in date:
                        date[s[4]] += 15000
                    else:
                        date[s[4]] = 0
                        date[s[4]] += 15000
            if s[2] == '2':
                if s[1] == 'Xe_tai':
                    if s[4] in date:
                        date[s[4]] += 20000
                    else:
                        date[s[4]] = 0
                        date[s[4]] += 20000
            if s[2] == '29':
                if s[1] == 'Xe_khach':
                    if s[4] in date:
                        date[s[4]] += 50000
                    else:
                        date[s[4]] = 0
                        date[s[4]] += 50000
            if s[2] == '45':
                if s[1] == 'Xe_khach':
                    if s[4] in date:
                        date[s[4]] += 70000
                    else:
                        date[s[4]] = 0
                        date[s[4]] += 70000
    for key,val in date.items():
        print(key , ': ',val,sep='')
        
        