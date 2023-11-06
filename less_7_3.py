def gen_step(chislo):
    i=0
    while True:
        result = chislo **i
        yield result
        if result>100**20:
            return 
        i+=1

rez = gen_step(12345)
print(rez)
for t  in rez:
    print(t)
