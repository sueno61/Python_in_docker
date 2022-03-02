import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image

import time

st.title('StreamLit 超入門')


# st.write('プログレスバーの表示')
# '<< Start'
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.01)
# 'Done >>'


# st.write('DataFrame')
"""
# １章 DataFrame

```
import pandas
pd.DataFrame
```
"""



df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})
# st.write(df)
#st.dataframe(df.style.highlight_max(axis=0), width=240, height=160)
# st.table(df.style.highlight_max(axis=0))


df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
#st.write(df2.head())
#st.line_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat','lon']
)
#st.write(df3.head())
chk1 = st.checkbox('Show Map')
if chk1:
    st.map(df3)

"""
#  ２章 Images
"""

if st.checkbox('Show Image'):

    img = Image.open('nowar.jpg')
    st.image(img, caption="No War!", use_column_width=True)


st.write('Interactive')

opt = st.sidebar.selectbox(
    '好きな数字は？',
    list(range(1,11))
)
'好きな数字： ', opt

txt = st.sidebar.text_input('あなたの趣味は？')
'趣味： ', txt

cond = st.sidebar.slider('コンディションを表現すると', 0, 100, 50)
'コンディション： ', cond

"""
## カラムわけ
"""
left_col, right_col = st.columns(2)
btn = left_col.button('右に文字を表示')
if btn:
    right_col.write('ここは右カラム')

st.write('Expander')
exp1 = st.expander('問い合わせ内容１')
exp1.write('問い合わせ１の回答')


