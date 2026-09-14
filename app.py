import streamlit as st
import pandas as pd
import plotly.express as px


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Luxury Fashion Intelligence",
    page_icon="✦",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    /* GLOBAL */

    .stApp {
        background-color: #F5F3EF;
        color: #161616;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 4rem;
        max-width: 1380px;
    }

    [data-testid="stAppViewContainer"] > .main {
        background-color: #F5F3EF;
    }


    /* HERO */

    .hero {
        padding: 1rem 0 1.8rem 0;
        border-bottom: 1px solid #DCD6CC;
        margin-bottom: 2rem;
    }

    .eyebrow {
        font-size: 0.72rem;
        letter-spacing: 0.24rem;
        text-transform: uppercase;
        color: #92794F;
        margin-bottom: 1rem;
        font-weight: 600;
    }

    .hero h1 {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(3rem, 5vw, 4.8rem);
        line-height: 1.02;
        font-weight: 400;
        letter-spacing: -0.13rem;
        margin: 0;
        color: #151515;
        max-width: 950px;
    }

    .hero p {
        max-width: 720px;
        font-size: 1rem;
        color: #777069;
        margin-top: 1.2rem;
        line-height: 1.65;
    }


    /* SECTION TITLES */

    .section-label {
        font-size: 0.69rem;
        letter-spacing: 0.22rem;
        text-transform: uppercase;
        color: #92794F;
        margin-top: 0.7rem;
        margin-bottom: 0.45rem;
        font-weight: 600;
    }

    h2 {
        font-family: Georgia, "Times New Roman", serif;
        font-weight: 400 !important;
        font-size: 2.2rem !important;
        letter-spacing: -0.04rem;
        color: #171717;
        margin-bottom: 0.2rem !important;
    }

    h3 {
        font-family: Georgia, "Times New Roman", serif;
        font-weight: 400 !important;
    }


    /* KPI CARDS */

    [data-testid="stMetric"] {
        background-color: #FAF9F6;
        padding: 1.2rem 1.3rem 1.35rem 1.3rem;
        border: 1px solid #DED8CE;
        border-radius: 0px;
        box-shadow: none;
        min-height: 135px;
    }

    [data-testid="stMetric"]:hover {
        border-color: #A99066;
        transition: 0.25s ease;
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.72rem;
        letter-spacing: 0.09rem;
        text-transform: uppercase;
        color: #777069;
    }

    [data-testid="stMetricValue"] {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 2.35rem;
        font-weight: 400;
        color: #202027;
        margin-top: 0.35rem;
    }


    /* BRAND PORTFOLIO */

    .brand-card {
        background-color: #FAF9F6;
        border: 1px solid #DDD7CD;
        padding: 1.8rem;
        min-height: 295px;
    }

    .brand-company {
        color: #92794F;
        font-size: 0.68rem;
        letter-spacing: 0.20rem;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 0.65rem;
    }

    .brand-card h3 {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 2rem;
        color: #171717;
        margin: 0 0 0.7rem 0;
    }

    .brand-description {
        color: #777069;
        font-size: 0.90rem;
        line-height: 1.6;
        margin-bottom: 1.3rem;
    }

    .brand-list {
        border-top: 1px solid #E2DDD4;
        padding-top: 1.1rem;
        color: #252525;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 1.05rem;
        line-height: 2;
    }

    .brand-count {
        margin-top: 1rem;
        color: #999188;
        font-size: 0.72rem;
        letter-spacing: 0.08rem;
        text-transform: uppercase;
    }


    /* INSIGHT CARDS */

    .insight-card {
        background-color: #FAF9F6;
        border-top: 2px solid #A99066;
        border-left: 1px solid #E0DAD0;
        border-right: 1px solid #E0DAD0;
        border-bottom: 1px solid #E0DAD0;
        padding: 1.5rem;
        min-height: 190px;
    }

    .insight-card h4 {
        font-family: Georgia, "Times New Roman", serif;
        font-weight: 400;
        font-size: 1.25rem;
        color: #171717;
        margin: 0 0 0.75rem 0;
    }

    .insight-card p {
        color: #706A63;
        font-size: 0.92rem;
        line-height: 1.7;
    }


    /* SOURCES */

    [data-testid="stCaptionContainer"] {
        color: #817B74;
    }

    .source-note {
        border-top: 1px solid #DCD6CC;
        padding-top: 1.3rem;
        margin-top: 3rem;
        font-size: 0.78rem;
        color: #837C73;
        line-height: 1.8;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HERO
# ==================================================

st.markdown(
    """<div class="hero">
<div class="eyebrow">✦ LUXURY INTELLIGENCE / 2026</div>
<h1>The Business<br>Behind Luxury.</h1>
<p>Financial performance and competitive intelligence across the world's leading luxury groups.</p>
</div>""",
    unsafe_allow_html=True
)


# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv("Data/luxury_financials.csv")

lvmh_df = (
    df[df["Company"] == "LVMH"]
    .sort_values("Year")
    .copy()
)

richemont_df = (
    df[df["Company"] == "Richemont"]
    .sort_values("Year")
    .copy()
)


# ==================================================
# KPI CALCULATIONS
# ==================================================

latest_revenue = lvmh_df.loc[
    lvmh_df["Year"] == 2025,
    "Revenue"
].iloc[0]

previous_revenue = lvmh_df.loc[
    lvmh_df["Year"] == 2024,
    "Revenue"
].iloc[0]

first_revenue = lvmh_df.loc[
    lvmh_df["Year"] == 2023,
    "Revenue"
].iloc[0]

richemont_latest = richemont_df.loc[
    richemont_df["Year"] == 2026,
    "Revenue"
].iloc[0]

yoy_change = (
    (latest_revenue - previous_revenue)
    / previous_revenue
) * 100

three_year_change = (
    (latest_revenue - first_revenue)
    / first_revenue
) * 100


# ==================================================
# AT A GLANCE
# ==================================================

st.markdown(
    '<div class="section-label">At a Glance</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="LVMH 2025 Revenue",
        value=f"€{latest_revenue:.1f}B"
    )

with col2:
    st.metric(
        label="LVMH YoY Change",
        value=f"{yoy_change:.1f}%"
    )

with col3:
    st.metric(
        label="LVMH vs. 2023",
        value=f"{three_year_change:.1f}%"
    )

with col4:
    st.metric(
        label="Richemont FY26 Sales",
        value=f"€{richemont_latest:.1f}B"
    )

st.write("")


# ==================================================
# 01 — COMPETITIVE LANDSCAPE
# ==================================================

st.markdown(
    '<div class="section-label">01 / Competitive Landscape</div>',
    unsafe_allow_html=True
)

st.markdown("## Revenue Scale")

st.caption(
    "Absolute reported revenue comparison between LVMH and Richemont."
)

fig = px.line(
    df,
    x="Year",
    y="Revenue",
    color="Company",
    markers=True,
    color_discrete_map={
        "LVMH": "#171717",
        "Richemont": "#B49A6A"
    }
)

fig.update_traces(
    line=dict(width=3),
    marker=dict(size=9)
)

fig.update_layout(
    paper_bgcolor="#FAF9F6",
    plot_bgcolor="#FAF9F6",
    font=dict(
        family="Arial",
        color="#5F5A54"
    ),
    showlegend=False,
    hovermode="x unified",
    margin=dict(
        l=30,
        r=90,
        t=35,
        b=35
    ),
    height=500
)

fig.update_xaxes(
    title="",
    dtick=1,
    showgrid=False,
    tickfont=dict(
        size=13,
        color="#77716A"
    ),
    linecolor="#D8D2C8"
)

fig.update_yaxes(
    title="Revenue (€B)",
    gridcolor="#E9E4DC",
    zeroline=False,
    tickfont=dict(
        size=12,
        color="#77716A"
    )
)

lvmh_last = lvmh_df.iloc[-1]

fig.add_annotation(
    x=lvmh_last["Year"],
    y=lvmh_last["Revenue"],
    text="LVMH",
    showarrow=False,
    xshift=42,
    font=dict(
        size=13,
        color="#171717"
    )
)

richemont_last = richemont_df.iloc[-1]

fig.add_annotation(
    x=richemont_last["Year"],
    y=richemont_last["Revenue"],
    text="Richemont",
    showarrow=False,
    xshift=55,
    font=dict(
        size=13,
        color="#92794F"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.caption(
    "Reporting periods differ: LVMH reports by calendar year, "
    "while Richemont reports fiscal years ending March 31."
)


# ==================================================
# 02 — GROWTH DYNAMICS
# ==================================================

st.write("")

st.markdown(
    '<div class="section-label">02 / Growth Dynamics</div>',
    unsafe_allow_html=True
)

st.markdown("## Growth Momentum")

st.caption(
    "Revenue indexed to 100 at each company's first available year."
)

growth_df = (
    df.sort_values(["Company", "Year"])
    .copy()
)

growth_df["Base Revenue"] = (
    growth_df
    .groupby("Company")["Revenue"]
    .transform("first")
)

growth_df["Growth Index"] = (
    growth_df["Revenue"]
    / growth_df["Base Revenue"]
) * 100

growth_fig = px.line(
    growth_df,
    x="Year",
    y="Growth Index",
    color="Company",
    markers=True,
    color_discrete_map={
        "LVMH": "#171717",
        "Richemont": "#B49A6A"
    }
)

growth_fig.update_traces(
    line=dict(width=3),
    marker=dict(size=9)
)

growth_fig.add_hline(
    y=100,
    line_dash="dot",
    line_color="#BDB6AC"
)

growth_fig.update_layout(
    paper_bgcolor="#FAF9F6",
    plot_bgcolor="#FAF9F6",
    font=dict(
        family="Arial",
        color="#5F5A54"
    ),
    showlegend=False,
    hovermode="x unified",
    margin=dict(
        l=30,
        r=90,
        t=35,
        b=35
    ),
    height=500
)

growth_fig.update_xaxes(
    title="",
    dtick=1,
    showgrid=False,
    tickfont=dict(
        size=13,
        color="#77716A"
    ),
    linecolor="#D8D2C8"
)

growth_fig.update_yaxes(
    title="Growth Index",
    gridcolor="#E9E4DC",
    zeroline=False,
    tickfont=dict(
        size=12,
        color="#77716A"
    )
)

lvmh_growth_last = (
    growth_df[
        growth_df["Company"] == "LVMH"
    ]
    .iloc[-1]
)

growth_fig.add_annotation(
    x=lvmh_growth_last["Year"],
    y=lvmh_growth_last["Growth Index"],
    text="LVMH",
    showarrow=False,
    xshift=42,
    font=dict(
        size=13,
        color="#171717"
    )
)

richemont_growth_last = (
    growth_df[
        growth_df["Company"] == "Richemont"
    ]
    .iloc[-1]
)

growth_fig.add_annotation(
    x=richemont_growth_last["Year"],
    y=richemont_growth_last["Growth Index"],
    text="Richemont",
    showarrow=False,
    xshift=55,
    font=dict(
        size=13,
        color="#92794F"
    )
)

st.plotly_chart(
    growth_fig,
    use_container_width=True
)


# ==================================================
# 03 — BRAND PORTFOLIO
# ==================================================

st.write("")

st.markdown(
    '<div class="section-label">03 / Brand Portfolio</div>',
    unsafe_allow_html=True
)

st.markdown("## The Houses Behind the Numbers")

st.caption(
    "A selection of flagship Maisons within each luxury group."
)

brand1, brand2 = st.columns(2)

with brand1:
    st.markdown(
        """<div class="brand-card">
<div class="brand-company">LVMH</div>
<h3>Fashion-Led Luxury Ecosystem</h3>
<div class="brand-description">A diversified portfolio spanning fashion, leather goods, jewellery, beauty, hospitality and retail.</div>
<div class="brand-list">
Louis Vuitton<br>
Christian Dior<br>
Fendi<br>
Loewe<br>
Celine
</div>
<div class="brand-count">Selected flagship Maisons</div>
</div>""",
        unsafe_allow_html=True
    )

with brand2:
    st.markdown(
        """<div class="brand-card">
<div class="brand-company">RICHEMONT</div>
<h3>Jewellery & Maison Leadership</h3>
<div class="brand-description">A portfolio strongly positioned across jewellery, watchmaking, fashion and high-end craftsmanship.</div>
<div class="brand-list">
Cartier<br>
Van Cleef & Arpels<br>
Alaïa<br>
Chloé<br>
Montblanc
</div>
<div class="brand-count">Selected flagship Maisons</div>
</div>""",
        unsafe_allow_html=True
    )


# ==================================================
# 04 — STRATEGIC TAKEAWAYS
# ==================================================

st.write("")

st.markdown(
    '<div class="section-label">04 / Strategic Takeaways</div>',
    unsafe_allow_html=True
)

st.markdown("## What the Data Suggests")

insight1, insight2, insight3 = st.columns(3)

with insight1:
    st.markdown(
        """<div class="insight-card">
<h4>✦ Scale Leadership</h4>
<p>LVMH remains substantially larger than Richemont based on reported revenue, reflecting its broader portfolio and diversified luxury ecosystem.</p>
</div>""",
        unsafe_allow_html=True
    )

with insight2:
    st.markdown(
        """<div class="insight-card">
<h4>✦ Momentum Shift</h4>
<p>Richemont shows positive sales momentum across its latest reported fiscal years while LVMH has experienced softer top-line performance.</p>
</div>""",
        unsafe_allow_html=True
    )

with insight3:
    st.markdown(
        """<div class="insight-card">
<h4>✦ Performance Pressure</h4>
<p>LVMH's 2025 revenue remains below both 2024 and 2023 levels, highlighting pressure on recent revenue growth.</p>
</div>""",
        unsafe_allow_html=True
    )


# ==================================================
# SOURCES
# ==================================================

st.markdown(
    """<div class="source-note">
<strong>Sources</strong><br><br>
LVMH Investor Relations · Richemont Investor Relations<br>
Financial values are presented in billions of euros. Reporting periods differ between companies.<br>
Brand portfolio represents selected flagship Maisons rather than each group's complete portfolio.<br><br>
Built with Python · Pandas · Plotly · Streamlit
</div>""",
    unsafe_allow_html=True
)