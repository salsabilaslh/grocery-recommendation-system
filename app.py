import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

df = pd.read_csv("association rules.csv")
df = df.iloc[2:].copy()
numeric_cols = ["Support","Confidence","Coverage","Strength","Lift","Leverage"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

st.set_page_config(page_title="식료품 추천 시스템",layout="centered")
st.markdown("""<style>
.main {padding-top: 2rem;}
h1 {color: #2E7D32;}
.stButton>button {background-color: #2E7D32;color: white;border-radius: 10px;border: none;}
.stButton>button:hover {background-color: #1B5E20;}
</style>""", unsafe_allow_html=True)

st.title("식료품 추천 시스템")
st.caption("상품을 선택하면 함께 구매되는 추천 상품을 확인할 수 있습니다.")
with st.expander("시스템 설명 보기"):
    st.write("""이 시스템은 구매 패턴 데이터를 분석하여함께 구매될 가능성이 높은 상품을 추천합니다.""")

all_products = set()
for item in df['Antecedent'].dropna():
    cleaned = item.replace("=1", "")
    parts = cleaned.split(",")

    for p in parts:
        all_products.add(p.strip())

products = sorted(list(all_products))
col1, col2, col3, col4 = st.columns(4)
with col1:st.metric("상품 수", len(products))
with col2:st.metric("연관 규칙", len(df))
with col3:st.metric("추천 시스템", "활성")
with col4:st.metric("평균 Lift", round(df["Lift"].mean(), 2))

selected_products = st.multiselect("상품 선택", products)
st.info("최대 3개의 상품을 선택하여 추천 결과를 확인할 수 있습니다.")
if len(selected_products) > 3:
    st.warning("최대 3개 상품만 선택할 수 있습니다.")
    st.stop()

top_n = st.number_input("추천 개수",min_value=1,max_value=10,value=5,step=1)

unique_items = []
chart_data = []
if st.button("추천 상품 확인"):
    if not selected_products:
        st.warning("상품을 먼저 선택해주세요.")
        st.stop()

    recommendations = df.copy()

    for product in selected_products:
        recommendations = recommendations[
            recommendations["Antecedent"].str.contains(
                product,
                na=False
            )
        ]
    recommendations = recommendations.sort_values(by="Confidence",ascending=False)
    unique_items = []
    for _, row in recommendations.iterrows():
        item = row["Consequent"]
        cleaned = item.replace("=1", "")
        parts = cleaned.split(",")

        for p in parts:
            p = p.strip()
            if (p not in [item["상품"]
                    for item in unique_items
                ]
                and p not in selected_products
            ):
                unique_items.append({"상품": p,"Lift": row["Lift"]})
                chart_data.append({"상품": p,"Lift": row["Lift"]})

with st.container():
    st.subheader("추천 상품")
    if unique_items:
        for item in unique_items[:top_n]:
            st.markdown(
                f"""<div style="
                    padding:12px;
                    margin:10px 0;
                    border-radius:10px;
                    background-color:#E8F5E9;
                    border-left: 5px solid #2E7D32;">
                    <h4>{item['상품']}</h4>
                    <p>Lift: {item['Lift']:.2f}</p></div>""",
                unsafe_allow_html=True)

        st.progress(100)
        if chart_data:
            chart_df = pd.DataFrame(chart_data[:top_n])
            chart_df = chart_df.sort_values(by="Lift",ascending=False)

            st.subheader("추천 상품 연관도 (Lift)")
            st.bar_chart(chart_df.set_index("상품"))

        selected_text = ", ".join(selected_products)
        st.success(f"추천 상품 {len(unique_items[:top_n])}개를 찾았습니다.")
        st.info(f"선택한 상품: {selected_text}")
        result_df = pd.DataFrame(unique_items[:top_n])

        st.download_button("결과 다운로드", result_df.to_csv(index=False),
            file_name="recommendation.csv", mime="text/csv")

    else:
        st.error("추천 가능한 상품이 없습니다.")

st.divider()
st.header("구매 패턴 분석")
st.markdown("""본 분석은 고객 구매 데이터를 기반으로 가장 많이 구매된 상품과 연관 규칙을 시각화한 결과입니다.""")
products = ["우유","기타 채소","열대과일","감귤류","롤빵","뿌리채소","돼지고기","소고기","요거트","닭고기"]
counts = [1129,790,690,598,565,529,465,397,378,367]

chart_option = st.radio("그래프 종류 선택",["막대 그래프", "원형 그래프"])
if chart_option == "막대 그래프":
    fig, ax = plt.subplots(figsize=(8,5))
    ax.bar(products, counts)

else:
    fig, ax = plt.subplots(figsize=(8,5))
    ax.pie(counts, labels=products, autopct='%1.1f%%')

st.pyplot(fig)
st.subheader("연관 규칙 분석 결과")

simple_rules = df[(df['Antecedent'].str.count(',') == 0) &
    (df['Consequent'].str.count(',') == 0)]

top_rules = simple_rules.sort_values(by="Lift", ascending=False)[
    ['Antecedent', 'Consequent', 'Lift']].head(10)
top_rules = top_rules.rename(columns={"Antecedent": "상품","Consequent": "추천 상품","Lift": "연관도(Lift)"})
top_rules["상품"] = top_rules["상품"].str.replace("=1", "")
top_rules["추천 상품"] = top_rules["추천 상품"].str.replace("=1", "")

st.dataframe(top_rules)
