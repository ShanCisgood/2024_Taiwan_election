# 檢驗此次總統大選結果是否符合班佛定律

>2024 中華民國正副總統大選結果出爐
>我利用中選會的資料轉為 csv 檔，之後再使用 Python 做分析
>目的是為了觀察結果是否符合班佛定律
>
>在benford_law.py是使用全臺灣各投開票所做統計
>並以benford_law_output.txt作為輸出
>
>在by_districts.py是使用全臺灣各鄉鎮市區做統計
>並以output_by_districts.txt作為輸出
>
>result_plot是把資料畫成圖的結果
>
>由於只有以鄉鎮市區作為劃分的資料比較準
>因此result_plot資料夾當中都是以鄉鎮市區作為劃分統計的繪圖
>
>各縣市投票資料來源: 中央選舉委員會
>https://vote2024.cec.gov.tw/zh-TW/indexP.html
