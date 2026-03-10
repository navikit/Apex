"""Streamlit dashboard prototype for AI Life Optimizer.

Run with:

    streamlit run streamlit_app.py

This is a starting point and is intentionally minimal. Expand with graphs,
heatmaps, goal tracking, and personalized recommendations.
"""

import streamlit as st


st.set_page_config(page_title="AI Life Optimizer", layout="wide")

st.title("AI Life Optimizer")

st.markdown(
    """
    This dashboard is a placeholder for visual analytics and recommendations.

    It should connect to the FastAPI backend to fetch user metrics, predictions,
    and suggested daily schedules.
    """
)

st.sidebar.header("Data Sources")
st.sidebar.markdown("- Calendar\n- Fitness trackers\n- Sleep data\n- Financial spending")

with st.expander("Example Recommendations", expanded=True):
    st.write(
        "Here you can display AI-generated suggestions such as ideal work blocks, "
        "best times to exercise, or when to take breaks."
    )

with st.expander("Metric Summary", expanded=True):
    st.metric(label="Productivity trend", value="+0.3%", delta="+0.05%")
    st.metric(label="Average sleep (hrs)", value="7.2", delta="-0.2")

st.write("## Next steps")
st.write(
    "Add API integration, connect to your local FastAPI backend, and plot live metrics."
)
