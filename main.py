from diaries.DiarySample import DiarySample
from diaries.k19041Diary import k19041Diary
from diaries.K21016Diary import K21016Diary
from diaries.K21095Diary import K21095Diary
from diaries.YamadaDiary import YamadaDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    k19041Diary(),
    K21016Diary(),
    K21095Diary(),
    YamadaDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()