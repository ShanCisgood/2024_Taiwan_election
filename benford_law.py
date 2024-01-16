# <------------------------------------>
# 此程式基本上就是利用班佛定律
# 驗證2024年中華民國總統大選的資料是否合理
# 取樣是以各「投開票所」做統計
# 最後結果: 
# 1. 每位候選人在各縣市的數據是否符合班佛定律
# 2. 每位候選人在全臺灣的數據是否符合班佛定律
# 3. 各縣市及全國的各候選人得票統計
# <------------------------------------>

import csv
import math

def print_dict(data_p, data_c):
    benford_ls = [math.log10((n + 1) / n) * 100 for n in range(1, 10)]

    print('| digit |  count  |  real  |theorical| error rate |', file = otp)
    print('|-------|---------|--------|---------|------------|', file = otp)
    for key in range(1, 10):
        print('| {0:3d}   |{1:7d}  | {2:5.2f}% |  {3:5.2f}% |  {4:6.2f}%   |'.format(key, data_c[key], data_p[key], benford_ls[key - 1], benford_ls[key - 1] - data_p[key]), file = otp)
    print('', file = otp)

def benfordLaw(ls_data):

    # initial process
    num = len(ls_data)
    first_nums = [int(str(n)[0]) for n in ls_data]
    count = [0 for i in range(0, 10)]
    persent = [0 for i in range(0, 10)]

    # data process
    for val in first_nums:
        count[val] += 1
    for i in range(0, 10):
        persent[i] = round((count[i] / num * 100), 2)

    # print
    print_dict(persent, count)

if __name__ == '__main__':

    filename_arr = ['台北', '新北', '基隆', '桃園', '竹市', 
                    '竹縣', '苗栗', '台中', '彰化', '南投',
                    '雲林', '嘉市', '嘉縣', '台南', '高雄',
                    '屏東', '宜蘭', '花蓮', '台東', '金門',
                    '連江', '澎湖']
    print_arr = ['', '\n一號柯盈得票: ', '\n二號美德得票: ', '\n三號侯康得票: ']

    all_candidates = []
    candidates = [[] for i in range(4)]
    total_vote_people = 0
    each_vote_people = [0 for i in range(0, 4)]

    # write
    otp = open('benford_law_output.txt', 'w')

    for cities in filename_arr:
        
        # init 
        total_gets = [[] for i in range(0, 4)]
        total = 0
        filename = f'city_list\{cities}.csv'

        # read file
        f = open(filename, mode = "r", newline = "")
        reader = csv.reader(f)
        for row in reader:
            if row[2].isnumeric():
                for i in range(1, 4):
                    total_gets[i].append(int(row[2 + i]))
                    candidates[i].append(int(row[2 + i]))
                    each_vote_people[i] += int(row[2 + i])

                cnt = int(row[3]) + int(row[4]) + int(row[5])
                total += cnt
                total_vote_people += cnt   
                all_candidates.append(cnt)

        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', file = otp)
        print(f'\n{cities}總票數: {total}', file = otp)
        for i in range(1, 4):
            print(f'{print_arr[i]}{sum(total_gets[i])}', file = otp)
            benfordLaw(total_gets[i])

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', file = otp)
    print(f'\n全台總票數: {total_vote_people}', file = otp)
    for i in range(1, 4):
        print(f'{print_arr[i]}{each_vote_people[i]}', file = otp)
        benfordLaw(candidates[i])

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n', file = otp)
    print(f'總票數統計: {total_vote_people}', file = otp)
    benfordLaw(all_candidates)

    otp.close()
