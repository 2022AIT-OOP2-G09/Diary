from diaries.DiarySample import DiarySample
from diaries.YamadaDiary import YamadaDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    YamadaDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()