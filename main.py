from diaries.DiarySample import DiarySample
from diaries.K21095Diary import K21095Diary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    K21095Diary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()