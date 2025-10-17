import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 生成假数据：70只小鼠的免疫实验结果

np.random.seed(42)
days = np.arange(0, 15)
mice = [f"Mouse_{i}" for i in range(1, 71)]
data = []

for mouse in mice:
    baseline = np.random.uniform(0.5, 1.0)
    antibody_levels = baseline + np.random.normal(0, 0.05, size=len(days))
    antibody_levels += np.linspace(0, np.random.uniform(0.1, 0.5), len(days))
    data.extend(zip([mouse]*len(days), days, antibody_levels))

df = pd.DataFrame(data, columns=["mouse_id", "day", "antibody_level"])

# 2. Streamlit 页面布局

st.title(" Immunology Experiment Dashboard")
st.markdown("Visualize antibody levels across different mice and days.")

# 选择小鼠
selected_mouse = st.selectbox("Select Mouse", sorted(df["mouse_id"].unique()))

# 筛选数据
subset = df[df["mouse_id"] == selected_mouse]

# 3. Matplotlib 图表

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(subset["day"], subset["antibody_level"], marker='o')
ax.set_xlabel("Day")
ax.set_ylabel("Antibody Level")
ax.set_title(f"Antibody Levels Over Time - {selected_mouse}")
st.pyplot(fig)

# 4. 汇总分析
st.markdown("### Group Summary")
group_stats = (
    df.groupby("day")["antibody_level"]
    .agg(["mean", "std"])
    .reset_index()
)
st.line_chart(group_stats.set_index("day")[["mean", "std"]])
