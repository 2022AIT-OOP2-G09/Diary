from diaries.AbstractDiary import AbstractDiary

class YamadaDiary(AbstractDiary):
    def get_date(self):
        return "2022-12-09"
    
    def get_summary(self):
        return "今日も一日中眠たい"
    
    def get_author(self):
        return "山田"
