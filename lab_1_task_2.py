class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
        self.total_h = 0
        self.bricks_in_current_row = 0

        self.bricks_rows = [i for i in range(self.max_h, 0, -1)]
        self.all_bricks = sum(self.bricks_rows)
        print(self.all_bricks)

    def add_bricks(self, num):
        self.bricks_count += num
        while self.total_h < self.max_h:
            bricks_in_rows = self.bricks_rows[self.total_h]
            if self.bricks_in_current_row + num >= bricks_in_rows:
                num -= (bricks_in_rows - self.bricks_in_current_row)
                self.bricks_in_current_row = 0
                self.total_h += 1
            else:
                self.bricks_in_current_row += num
                break
                
        if num > 0 and self.total_h < self.max_h:
            self.bricks_in_current_row += num
            
        if self.total_h >= self.max_h:
            print('Пирамида достигла максимальной высоты!')
        
            

    def get_height(self):
          # Выводим текущую высоту пирамиды

        print(f"Высота пирамиды: {self.total_h}.")


    def is_done(self):
        res_bricks = self.bricks_count / self.all_bricks * 100
        return res_bricks


class Builder:
    def __init__(self, bricks):
        self.bricks = bricks
        self.day = 1
        self.my_pyramid = Pyramid(15)

    def buy_bricks(self):
        self.bricks += 5
        print(f"Куплено 5 кирпичей. Теперь у строителя {self.bricks} кирпичей.")

    def build_pyramid(self, n):
        if self.bricks >= n:
            self.bricks -= n
            return n
        else:
            print("Недостаточно кирпичей!")
            return 0

    def work_day(self):
        needed_bricks = min(5, self.bricks + 5)  
        added_bricks = self.build_pyramid(needed_bricks)
        

        if added_bricks > 0:
            self.my_pyramid.add_bricks(added_bricks)
        
        print(f"День {self.day}.")
        print(f"Строили пирамиду: добавлено {added_bricks} кирпичей.")
        print(f"Остаток кирпичей у строителя: {self.bricks}.")
        self.my_pyramid.get_height()  # Выводим текущую высоту пирамиды
        

        readiness = self.my_pyramid.is_done()
        print(f"Готовность пирамиды: {readiness:.2f}%.")  
        

        if readiness >= 100:  
            print("Пирамида завершена!")
            exit(0)

        
        if added_bricks == 0:
            self.buy_bricks()
        
        self.day += 1

if __name__ == '__main__':
    b = Builder(13)

    while True:
        b.work_day()
    