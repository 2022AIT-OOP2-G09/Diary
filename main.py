from diaries.DiarySample import DiarySample
from diaries.K21016Diary import K21016Diary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    K21016Diary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()