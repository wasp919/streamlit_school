import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
# import time

st.title('streamlit 超入門')

st.write('プレぐレスバーの表示')
'Start!!'




latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iternation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

st.write('DataFrame')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味は', text

condition = st.slider('あなたの今の調子は？', 10, 100, 50)
'コンディション：', condition

# option = st.selectbox(
#     'あなたが好きな数字を教えて',
#     list(range(1,10))
# # )
# 'あなたの好きな数字は', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('sample.JPG')
#     st.image(img, caption='Kohei Imanishi', use_column_width=True)

#df = pd.DataFrame({
#    '1列目': [1,2,3,4],
#    '2列目': [10,20,30,40]
#})

#st.table(df.style.highlight_max(axis=0) )

"""
# 小
## 確
### 幸

'''python
import streamlit as st
import numpy as np
import pandas as pd

"""

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50 , 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.write(df)
# st.line_chart(df)
# st.area_chart(df)
# st.map(df)
