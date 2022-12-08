from diaries.DiarySample import DiarySample
from diaries.k21026Diary import k21026iDiary
from diaries.K21010Diary import K21010Diary
from diaries.k19041Diary import k19041Diary
from diaries.K21016Diary import K21016Diary
from diaries.K21095Diary import K21095Diary
from diaries.YamadaDiary import YamadaDiary
from diaries.k21132_yatch import k21132_yatch

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    K21010Diary(),
    k19041Diary(),
    K21016Diary(),
    K21095Diary(),
    YamadaDiary(),
    k21026iDiary(),
    k21132_yatch()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()