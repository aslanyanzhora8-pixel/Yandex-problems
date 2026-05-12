n = int(input())
mijnatver = list()
modaner = list()
yndhanur = list()
sharqer = list()
for i in range(n):
    sharq = input()
    sharq = sharq.split(" ")
    sharqer.append(sharq)
for k in sharqer:
    mijnatver.append(k[len(k) // 2])
    yndhanur = yndhanur + k
    print(k[len(k) // 2], end="")  # mijnativ
print()
for v in sharqer:
    mod = list()
    for elem in v:
        mod.append(v.count(elem))
    modaner.append(v[mod.index(max(mod))])
    print(v[mod.index(max(mod))], end="")  # mod
print()
print(mijnatver[len(mijnatver) // 2])  # mijnatveri mijnativ
mod = list()
for j in modaner:
    mod.append(modaner.count(j))
print(modaner[mod.index(max(mod))])  # modaneri modan
print(yndhanur[len(yndhanur) // 2])  # yndhanuri mijnativy
mod = list()
for item in yndhanur:
    mod.append(yndhanur[yndhanur.count(item)])
print(yndhanur[mod.index(max(mod))])
