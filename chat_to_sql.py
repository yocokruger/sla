import vanna as vn 
import streamlit as st

vn.set_api_key(st.secrets["5a8e0a9558d640398a8a73cec4a5809c"])
vn.set_model('yoco')
vn.connect_to_sqlite('/Users/wernerkruger/Documents/stockdata-main/stockdata.db')

my_question = st.text_input("Ask me a question that I can turn into SQL", key="my_question")

sql = vn.generate_sql(my_question)
st.code(sql, language='sql')

df = vn.run_sql(sql)    
st.dataframe(df, use_container_width=True)

fig = vn.get_plotly_figure(plotly_code=vn.generate_plotly_code(question=my_question, sql=sql, df=df), df=df)
st.plotly_chart(fig, use_container_width=True)
