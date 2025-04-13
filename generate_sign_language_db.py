import sqlite3

# 建立資料庫並初始化表格
def create_database():
    conn = sqlite3.connect('sign_language.db')
    cursor = conn.cursor()

    # 建立 SignGestures 表格
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SignGestures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sign_name TEXT NOT NULL,
            f1_min REAL NOT NULL,
            f1_max REAL NOT NULL,
            f2_min REAL NOT NULL,
            f2_max REAL NOT NULL,
            f3_min REAL NOT NULL,
            f3_max REAL NOT NULL,
            f4_min REAL NOT NULL,
            f4_max REAL NOT NULL,
            f5_min REAL NOT NULL,
            f5_max REAL NOT NULL,
            fo1_min REAL NOT NULL,
            fo1_max REAL NOT NULL,
            fo2_min REAL NOT NULL,
            fo2_max REAL NOT NULL,
            fo3_min REAL NOT NULL,
            fo3_max REAL NOT NULL,
            fo4_min REAL NOT NULL,
            fo4_max REAL NOT NULL,
            fo5_min REAL NOT NULL,
            fo5_max REAL NOT NULL,
            is_double_hand INTEGER NOT NULL
        )
    ''')

    # 檢查是否已有資料，若無則插入初始資料
    cursor.execute("SELECT COUNT(*) FROM SignGestures")
    if cursor.fetchone()[0] == 0:
        signs = [
            # 雙手詞彙
            ('讀書', 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 1),
            ('門', 50, 180, 0, 50, 0, 50, 0, 50, 0, 50, 50, 180, 0, 50, 0, 50, 0, 50, 0, 50, 1),
            ('血', 0, 50, 50, 180, 50, 180, 50, 180, 50, 180, 50, 180, 0, 50, 50, 180, 50, 180, 50, 180, 1),
            ('當', 50, 180, 0, 50, 0, 50, 0, 50, 50, 180, 50, 180, 0, 50, 50, 180, 50, 180, 50, 180, 1),
            ('表演', 50, 180, 0, 50, 50, 180, 50, 180, 50, 180, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 1),
            ('牛', 0, 50, 50, 180, 50, 180, 50, 180, 0, 50, 0, 50, 50, 180, 50, 180, 50, 180, 0, 50, 1),
            ('心', 0, 50, 0, 50, 50, 180, 50, 180, 50, 180, 0, 50, 0, 50, 50, 180, 50, 180, 50, 180, 1),
            ('相信', 50, 180, 0, 50, 0, 50, 50, 180, 50, 180, 50, 180, 0, 50, 0, 50, 50, 180, 50, 180, 1),
            ('坦白', 0, 50, 0, 50, 0, 50, 50, 180, 50, 180, 0, 50, 0, 50, 0, 50, 50, 180, 50, 180, 1),
            ('有名', 0, 50, 50, 180, 50, 180, 50, 180, 50, 180, 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 1),
            ('小', 50, 180, 0, 50, 50, 180, 50, 180, 50, 180, 50, 180, 0, 50, 0, 50, 50, 180, 50, 180, 1),
            ('銀行', 50, 180, 50, 180, 0, 50, 0, 50, 0, 50, 50, 180, 50, 180, 0, 50, 0, 50, 0, 50, 1),
            ('銀行', 0, 50, 50, 180, 0, 50, 0, 50, 0, 50, 0, 50, 50, 180, 0, 50, 0, 50, 0, 50, 1),
            # 單手詞彙
            ('男', 0, 50, 50, 180, 50, 180, 50, 180, 50, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('高', 50, 180, 50, 180, 0, 50, 50, 180, 50, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('等', 0, 50, 0, 50, 50, 180, 50, 180, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('在', 50, 180, 50, 180, 50, 180, 50, 180, 50, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('女', 50, 180, 50, 180, 50, 180, 50, 180, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('我', 50, 180, 0, 50, 50, 180, 50, 180, 50, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('命令', 50, 180, 0, 50, 0, 50, 50, 180, 50, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('ok', 50, 180, 50, 180, 0, 50, 0, 50, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('ok', 0, 50, 50, 180, 0, 50, 0, 50, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('川', 50, 180, 0, 50, 0, 50, 0, 50, 50, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('是', 50, 180, 0, 50, 0, 50, 0, 50, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('有', 0, 50, 0, 50, 0, 50, 0, 50, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('怎麼會', 0, 50, 50, 180, 50, 180, 50, 180, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('刷牙', 0, 50, 0, 50, 50, 180, 50, 180, 50, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('懶惰', 0, 50, 0, 50, 0, 50, 50, 180, 50, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            ('八', 0, 50, 0, 50, 0, 50, 0, 50, 50, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        ]

        cursor.executemany('''
            INSERT INTO SignGestures (sign_name, f1_min, f1_max, f2_min, f2_max, f3_min, f3_max, f4_min, f4_max, f5_min, f5_max, fo1_min, fo1_max, fo2_min, fo2_max, fo3_min, fo3_max, fo4_min, fo4_max, fo5_min, fo5_max, is_double_hand)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', signs)

        conn.commit()
    return conn

# 從資料庫讀取詞彙和角度條件
def load_signs_from_db(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SignGestures")
    signs = []
    for row in cursor.fetchall():
        sign = {
            'id': row[0],
            'sign_name': row[1],
            'f1_min': row[2], 'f1_max': row[3],
            'f2_min': row[4], 'f2_max': row[5],
            'f3_min': row[6], 'f3_max': row[7],
            'f4_min': row[8], 'f4_max': row[9],
            'f5_min': row[10], 'f5_max': row[11],
            'fo1_min': row[12], 'fo1_max': row[13],
            'fo2_min': row[14], 'fo2_max': row[15],
            'fo3_min': row[16], 'fo3_max': row[17],
            'fo4_min': row[18], 'fo4_max': row[19],
            'fo5_min': row[20], 'fo5_max': row[21],
            'is_double_hand': row[22]
        }
        signs.append(sign)
    return signs

# 編輯詞彙和角度的命令行工具
def edit_signs(conn):
    while True:
        print("\n詞彙編輯工具")
        print("1. 查看所有詞彙")
        print("2. 新增詞彙")
        print("3. 修改詞彙")
        print("4. 刪除詞彙")
        print("5. 退出編輯")
        choice = input("請選擇操作 (1-5): ")

        cursor = conn.cursor()

        if choice == '1':
            signs = load_signs_from_db(conn)
            for sign in signs:
                print(f"ID: {sign['id']}, 詞彙: {sign['sign_name']}, "
                      f"f1: [{sign['f1_min']}-{sign['f1_max']}], "
                      f"f2: [{sign['f2_min']}-{sign['f2_max']}], "
                      f"f3: [{sign['f3_min']}-{sign['f3_max']}], "
                      f"f4: [{sign['f4_min']}-{sign['f4_max']}], "
                      f"f5: [{sign['f5_min']}-{sign['f5_max']}], "
                      f"雙手: {sign['is_double_hand']}")
                if sign['is_double_hand']:
                    print(f"  另一隻手 - fo1: [{sign['fo1_min']}-{sign['fo1_max']}], "
                          f"fo2: [{sign['fo2_min']}-{sign['fo2_max']}], "
                          f"fo3: [{sign['fo3_min']}-{sign['fo3_max']}], "
                          f"fo4: [{sign['fo4_min']}-{sign['fo4_max']}], "
                          f"fo5: [{sign['fo5_min']}-{sign['fo5_max']}]")

        elif choice == '2':
            sign_name = input("輸入詞彙名稱: ")
            f1_min = float(input("輸入 f1 最小值: "))
            f1_max = float(input("輸入 f1 最大值: "))
            f2_min = float(input("輸入 f2 最小值: "))
            f2_max = float(input("輸入 f2 最大值: "))
            f3_min = float(input("輸入 f3 最小值: "))
            f3_max = float(input("輸入 f3 最大值: "))
            f4_min = float(input("輸入 f4 最小值: "))
            f4_max = float(input("輸入 f4 最大值: "))
            f5_min = float(input("輸入 f5 最小值: "))
            f5_max = float(input("輸入 f5 最大值: "))
            is_double_hand = int(input("是否需要雙手 (1=是, 0=否): "))
            fo1_min = fo1_max = fo2_min = fo2_max = fo3_min = fo3_max = fo4_min = fo4_max = fo5_min = fo5_max = 0
            if is_double_hand:
                fo1_min = float(input("輸入 fo1 最小值: "))
                fo1_max = float(input("輸入 fo1 最大值: "))
                fo2_min = float(input("輸入 fo2 最小值: "))
                fo2_max = float(input("輸入 fo2 最大值: "))
                fo3_min = float(input("輸入 fo3 最小值: "))
                fo3_max = float(input("輸入 fo3 最大值: "))
                fo4_min = float(input("輸入 fo4 最小值: "))
                fo4_max = float(input("輸入 fo4 最大值: "))
                fo5_min = float(input("輸入 fo5 最小值: "))
                fo5_max = float(input("輸入 fo5 最大值: "))

            cursor.execute('''
                INSERT INTO SignGestures (sign_name, f1_min, f1_max, f2_min, f2_max, f3_min, f3_max, f4_min, f4_max, f5_min, f5_max, fo1_min, fo1_max, fo2_min, fo2_max, fo3_min, fo3_max, fo4_min, fo4_max, fo5_min, fo5_max, is_double_hand)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (sign_name, f1_min, f1_max, f2_min, f2_max, f3_min, f3_max, f4_min, f4_max, f5_min, f5_max, fo1_min, fo1_max, fo2_min, fo2_max, fo3_min, fo3_max, fo4_min, fo4_max, fo5_min, fo5_max, is_double_hand))
            conn.commit()
            print(f"已新增詞彙: {sign_name}")

        elif choice == '3':
            sign_id = int(input("輸入要修改的詞彙 ID: "))
            cursor.execute("SELECT * FROM SignGestures WHERE id = ?", (sign_id,))
            sign = cursor.fetchone()
            if not sign:
                print("找不到該詞彙！")
                continue

            print(f"當前詞彙: {sign[1]}")
            sign_name = input(f"輸入新詞彙名稱 (留空保持 {sign[1]}): ") or sign[1]
            f1_min = float(input(f"輸入 f1 最小值 (留空保持 {sign[2]}): ") or sign[2])
            f1_max = float(input(f"輸入 f1 最大值 (留空保持 {sign[3]}): ") or sign[3])
            f2_min = float(input(f"輸入 f2 最小值 (留空保持 {sign[4]}): ") or sign[4])
            f2_max = float(input(f"輸入 f2 最大值 (留空保持 {sign[5]}): ") or sign[5])
            f3_min = float(input(f"輸入 f3 最小值 (留空保持 {sign[6]}): ") or sign[6])
            f3_max = float(input(f"輸入 f3 最大值 (留空保持 {sign[7]}): ") or sign[7])
            f4_min = float(input(f"輸入 f4 最小值 (留空保持 {sign[8]}): ") or sign[8])
            f4_max = float(input(f"輸入 f4 最大值 (留空保持 {sign[9]}): ") or sign[9])
            f5_min = float(input(f"輸入 f5 最小值 (留空保持 {sign[10]}): ") or sign[10])
            f5_max = float(input(f"輸入 f5 最大值 (留空保持 {sign[11]}): ") or sign[11])
            is_double_hand = int(input(f"是否需要雙手 (1=是, 0=否, 留空保持 {sign[22]}): ") or sign[22])
            fo1_min = fo1_max = fo2_min = fo2_max = fo3_min = fo3_max = fo4_min = fo4_max = fo5_min = fo5_max = 0
            if is_double_hand:
                fo1_min = float(input(f"輸入 fo1 最小值 (留空保持 {sign[12]}): ") or sign[12])
                fo1_max = float(input(f"輸入 fo1 最大值 (留空保持 {sign[13]}): ") or sign[13])
                fo2_min = float(input(f"輸入 fo2 最小值 (留空保持 {sign[14]}): ") or sign[14])
                fo2_max = float(input(f"輸入 fo2 最大值 (留空保持 {sign[15]}): ") or sign[15])
                fo3_min = float(input(f"輸入 fo3 最小值 (留空保持 {sign[16]}): ") or sign[16])
                fo3_max = float(input(f"輸入 fo3 最大值 (留空保持 {sign[17]}): ") or sign[17])
                fo4_min = float(input(f"輸入 fo4 最小值 (留空保持 {sign[18]}): ") or sign[18])
                fo4_max = float(input(f"輸入 fo4 最大值 (留空保持 {sign[19]}): ") or sign[19])
                fo5_min = float(input(f"輸入 fo5 最小值 (留空保持 {sign[20]}): ") or sign[20])
                fo5_max = float(input(f"輸入 fo5 最大值 (留空保持 {sign[21]}): ") or sign[21])

            cursor.execute('''
                UPDATE SignGestures
                SET sign_name = ?, f1_min = ?, f1_max = ?, f2_min = ?, f2_max = ?, f3_min = ?, f3_max = ?, f4_min = ?, f4_max = ?, f5_min = ?, f5_max = ?,
                    fo1_min = ?, fo1_max = ?, fo2_min = ?, fo2_max = ?, fo3_min = ?, fo3_max = ?, fo4_min = ?, fo4_max = ?, fo5_min = ?, fo5_max = ?, is_double_hand = ?
                WHERE id = ?
            ''', (sign_name, f1_min, f1_max, f2_min, f2_max, f3_min, f3_max, f4_min, f4_max, f5_min, f5_max, fo1_min, fo1_max, fo2_min, fo2_max, fo3_min, fo3_max, fo4_min, fo4_max, fo5_min, fo5_max, is_double_hand, sign_id))
            conn.commit()
            print(f"已更新詞彙 ID {sign_id}")

        elif choice == '4':
            sign_id = int(input("輸入要刪除的詞彙 ID: "))
            cursor.execute("DELETE FROM SignGestures WHERE id = ?", (sign_id,))
            conn.commit()
            print(f"已刪除詞彙 ID {sign_id}")

        elif choice == '5':
            break

        else:
            print("無效選擇，請重試！")

# 主程式
def main():
    conn = create_database()
    print("資料庫 sign_language.db 已生成或已存在！")
    print("是否需要編輯詞彙？")
    edit_choice = input("輸入 y 進入編輯模式，輸入 n 退出 (y/n): ")
    if edit_choice.lower() == 'y':
        edit_signs(conn)
    conn.close()
    print("程式結束。")

if __name__ == "__main__":
    main()