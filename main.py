from diaries.DiarySample import DiarySample
from diaries.k19041Diary import k19041Diary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    k19041Diary(),
    
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()