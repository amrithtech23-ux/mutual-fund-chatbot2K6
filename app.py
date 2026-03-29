import streamlit as st
import requests
import os
import random

# ================= CONFIGURATION =================
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENROUTER_API_KEY")
MODEL = "qwen/qwen-2.5-72b-instruct"

# ================= KNOWLEDGE BASE =================
KB = """
MUTUAL FUND COMPREHENSIVE KNOWLEDGE BASE

FOR COMMERCE STUDENTS:
1. What Are Mutual Funds and How Do They Work?
   - Pooled investments, NAV calculation, fund structures
   - How money is pooled from multiple investors
   - Professional fund management benefits
   - Diversification across securities

2. Types of Mutual Funds:
   - Equity funds (large-cap, mid-cap, small-cap)
   - Debt funds (gilt, corporate bond, liquid)
   - Hybrid funds (balanced, aggressive, conservative)
   - Index funds and ETFs
   - Sectoral and thematic funds

3. Understanding NAV, AUM, and Expense Ratios:
   - Net Asset Value calculation and importance
   - Assets Under Management significance
   - Expense ratio impact on returns
   - Direct vs. Regular plan expense differences

4. SIP vs. Lump Sum Investing:
   - Systematic Investment Plan benefits
   - Rupee cost averaging concept
   - When to use lump sum investments
   - Market timing considerations

5. Risk-Return Profiles:
   - Different fund category risk levels
   - Matching funds to investor risk tolerance
   - Volatility and return expectations
   - Investment horizon considerations

6. Tax Implications:
   - Capital gains (short-term vs. long-term)
   - Dividend distribution tax
   - Tax-saving funds (ELSS)
   - Indexation benefits for debt funds

7. How to Read a Mutual Fund Factsheet:
   - Portfolio holdings interpretation
   - Performance metrics understanding
   - Risk metrics (beta, standard deviation)
   - Fund manager information

8. Direct vs. Regular Plans:
   - Distributor commission impact
   - Expense ratio differences
   - Long-term return impact
   - How to switch between plans

9. Exit Loads and Lock-in Periods:
   - Exit load structure and purpose
   - ELSS lock-in period (3 years)
   - Impact on redemption decisions
   - Planning investment tenure

10. Fund Performance Benchmarking:
    - Choosing appropriate benchmarks
    - Relative vs. absolute returns
    - Rolling returns analysis
    - Consistency of performance

11. Role of Fund Managers and AMCs:
    - Investment decision-making process
    - Research and analysis framework
    - AMC track record importance
    - Fund manager tenure impact

12. Building a Diversified Portfolio:
    - Asset allocation principles
    - Correlation between fund categories
    - Rebalancing strategies
    - Goal-based investing approach

FOR MBA FINANCE STUDENTS:
13. Modern Portfolio Theory and Fund Construction:
    - Diversification and correlation principles
    - Efficient frontier concept
    - Risk-return optimization
    - Capital market line

14. Advanced Performance Metrics:
    - Sharpe Ratio calculation and interpretation
    - Alpha and Beta analysis
    - Standard deviation and volatility
    - Information Ratio and Treynor Ratio

15. Active vs. Passive Fund Management:
    - Cost-benefit analysis
    - Outperformance potential
    - Index tracking efficiency
    - Market efficiency considerations

16. Factor Investing and Smart Beta:
    - Value, momentum, quality factors
    - Low-volatility strategies
    - Factor rotation strategies
    - Smart beta fund construction

17. Style Drift and Manager Consistency:
    - Investment mandate adherence
    - Style box analysis
    - Manager track record evaluation
    - Consistency metrics

18. Sector Rotation and Tactical Allocation:
    - Market cycle analysis
    - Sector performance patterns
    - Tactical vs. strategic allocation
    - Economic indicator analysis

19. Currency-Hedged International Funds:
    - FX risk management
    - Hedging cost-benefit analysis
    - Global diversification benefits
    - Currency impact on returns

20. ESG Integration in Fund Selection:
    - Sustainability criteria evaluation
    - ESG scoring methodologies
    - Impact on financial returns
    - Regulatory requirements

21. Fund of Funds (FoF) Structures:
    - Layered investment analysis
    - Double expense ratio impact
    - Diversification benefits
    - When FoFs make sense

22. Liquidity Management in Open-End Funds:
    - Redemption pressure handling
    - Cash flow mismatch management
    - Liquid asset maintenance
    - Stress scenario planning

23. Performance Attribution Analysis:
    - Asset allocation effect
    - Security selection effect
    - Timing effect decomposition
    - Benchmark-relative analysis

24. Behavioral Finance and Fund Flows:
    - Investor sentiment impact
    - Herding behavior analysis
    - Flow-performance relationship
    - Market impact of flows

25. Regulatory Frameworks:
    - SEBI regulations (India)
    - SEC regulations (USA)
    - UCITS requirements (Europe)
    - Cross-border compliance

FOR INVESTMENT BANKING ASPIRANTS:
26. Mutual Fund Value Chain:
    - AMC roles and responsibilities
    - Distributor network structure
    - Custodian and registrar functions
    - Depositary oversight

27. Fund Distribution Channels:
    - Direct channel economics
    - Advisor/IFA model
    - Platform/distributor model
    - Institutional sales

28. New Fund Offerings (NFOs):
    - Launch process and timeline
    - Marketing and positioning
    - Evaluation criteria
    - Common pitfalls

29. Fund Mergers and Scheme Rationalization:
    - Consolidation rationale
    - Investor communication
    - Tax implications
    - Portfolio integration

30. Fund Documentation:
    - Scheme Information Document (SID)
    - Key Information Memorandum (KIM)
    - Annual reports
    - Fact sheets and updates

31. Research and Analyst Roles:
    - Equity analyst responsibilities
    - Debt analyst functions
    - Quantitative analyst roles
    - Career preparation

32. Sales and Distribution Careers:
    - Relationship management skills
    - Channel development
    - Client acquisition strategies
    - Performance metrics

33. Compliance and Operations Roles:
    - Regulatory reporting
    - Risk controls
    - Back-office functions
    - Audit requirements

34. Interview Preparation:
    - Technical questions
    - Behavioral questions
    - Case study preparation
    - Industry knowledge

35. Certifications:
    - NISM certifications
    - CFA program
    - CAIA designation
    - Other relevant credentials

36. Building Research Portfolio:
    - Fund analysis documentation
    - Model portfolio creation
    - Market commentary
    - Track record building

37. Networking Strategies:
    - Industry events
    - Professional associations
    - LinkedIn optimization
    - Mentor relationships

FOR INVESTMENT BANKING PROFESSIONALS:
38. Designing Thematic and Sectoral Funds:
    - Emerging trend identification
    - Fund structuring
    - Risk management
    - Marketing positioning

39. Institutional Share Classes:
    - Fee negotiation strategies
    - Custom terms for institutions
    - Pension fund requirements
    - Sovereign wealth fund needs

40. Cross-Border Distribution:
    - Regulatory approvals
    - Tax treaty considerations
    - Localization requirements
    - Marketing adaptations

41. Liquidity Tools:
    - Swing pricing mechanisms
    - Redemption gates
    - Side pockets
    - Stress scenario management

42. Derivatives Usage:
    - Futures and options strategies
    - Risk management applications
    - Regulatory limits
    - Return enhancement

43. Private Credit and Alternative Funds:
    - Liquid alternative structures
    - Retail investor access
    - Risk-return profiles
    - Regulatory considerations

44. Fund Incubation:
    - Track record building
    - Seed capital strategies
    - Performance marketing
    - Graduation criteria

45. M&A in Asset Management:
    - Valuation drivers
    - Integration challenges
    - Synergy realization
    - Cultural alignment

46. ETF vs. Mutual Fund Strategy:
    - Product selection criteria
    - Cost considerations
    - Trading vs. investing
    - Target investor profiles

47. Fee Compression and Innovation:
    - Pricing adaptation
    - Scale benefits
    - Service differentiation
    - Technology leverage

48. Technology and Analytics:
    - AI in investment processes
    - Alternative data usage
    - Quantitative models
    - Digital transformation

49. Regulatory Arbitrage:
    - Jurisdiction selection
    - Domicile considerations
    - Distribution optimization
    - Compliance efficiency

50. Future of Mutual Funds:
    - Personalization trends
    - Direct indexing
    - Tokenization potential
    - Evolution of structures
"""

# ================= SUGGESTION PROMPTS =================
SUGGESTIONS = [
    "What are mutual funds and how do they work?",
    "SIP vs. Lump Sum - which is better?",
    "How to read a mutual fund factsheet?",
    "Tax implications of mutual fund investments?",
    "Direct vs. Regular plans - difference?",
    "How to build a diversified portfolio?",
    "What is NAV and how is it calculated?",
    "Active vs. Passive fund management?",
    "How to evaluate fund performance?",
    "ELSS funds for tax saving?"
]

# ================= CUSTOM CSS STYLING =================
st.markdown("""
<style>
.stTextArea label {
    font-weight: bold !important;
    font-size: 1.2rem !important;
    color: #00008B !important;
}
.stTextArea textarea {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    border: 3px solid #00008B !important;
    border-radius: 8px !important;
}
.result-box {
    background-color: #003366 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 1.1rem !important;
    border: 3px solid #00008B !important;
    border-radius: 8px !important;
    padding: 20px !important;
    margin-top: 15px !important;
    white-space: pre-wrap !important;
}
.stButton > button {
    color: #00008B !important;
    font-weight: bold !important;
    font-size: 1.05rem !important;
    border: 2px solid #00008B !important;
    background-color: white !important;
    padding: 12px 18px !important;
    border-radius: 8px !important;
}
.stButton > button:hover {
    background-color: #00008B !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Mutual Fund Chatbot", page_icon="📈", layout="wide")

# ================= INITIALIZE SESSION STATE =================
if 'last_answer' not in st.session_state:
    st.session_state.last_answer = ""
if 'reset_counter' not in st.session_state:
    st.session_state.reset_counter = 0

# ================= TITLE =================
st.markdown('<h1 style="font-size: 2.5rem; font-weight: bold; color: #003366; text-align: center;">📈 Mutual Fund Chatbot</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.1rem; color: #666; text-align: center;">50+ Topics | Powered by Qwen 2.5 72B</p>', unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("### 🎯 Controls")
    if st.button("🔄 Reset Chat", use_container_width=True, key="reset_btn"):
        st.session_state.last_answer = ""
        st.session_state.reset_counter += 1
        st.rerun()
    st.info("🤖 Model: qwen-2.5-72b-instruct")
    st.success("📚 KB: 4 Categories, 50 Topics")
    st.markdown("---")
    st.markdown("### 🎓 Target Audience:")
    st.markdown("- 📊 Commerce Students")
    st.markdown("- 📈 MBA Finance Students")
    st.markdown("- 💼 Investment Banking Aspirants")
    st.markdown("- 👔 Investment Banking Professionals")
    st.markdown("---")
    st.caption("📄 License: MIT | 🐙 GitHub + Streamlit Cloud")

# ================= SUGGESTION PROMPTS =================
st.markdown("### 💡 Suggestion Prompts (Select text → Right-click → Copy):")

cols_row1 = st.columns(5)
cols_row2 = st.columns(5)
display_prompts = random.sample(SUGGESTIONS, 10)

for i, prompt in enumerate(display_prompts[:5]):
    with cols_row1[i]:
        st.markdown(f"""
        <div style="background-color: white; border: 2px solid #00008B; border-radius: 8px; padding: 20px; margin: 5px; text-align: center;">
            <p style="color: #00008B; font-weight: bold; font-size: 1.05rem; margin: 0;">{prompt}</p>
        </div>
        """, unsafe_allow_html=True)

for i, prompt in enumerate(display_prompts[5:10]):
    with cols_row2[i]:
        st.markdown(f"""
        <div style="background-color: white; border: 2px solid #00008B; border-radius: 8px; padding: 20px; margin: 5px; text-align: center;">
            <p style="color: #00008B; font-weight: bold; font-size: 1.05rem; margin: 0;">{prompt}</p>
        </div>
        """, unsafe_allow_html=True)

st.info("💡 **How to use:** Select any suggestion text above → Right-click → Copy → Paste in query box below → Click Submit")

st.markdown("---")

# ================= QUERY INPUT =================
st.markdown("### 📝 Enter Your Mutual Fund Query:")

user_query = st.text_area(
    label="Query Input",
    value="",
    height=150,
    placeholder="📋 Copy a suggestion above (right-click) and paste here, or type your own question...",
    key=f"query_input_{st.session_state.reset_counter}"
)

# ================= SUBMIT BUTTON =================
st.markdown('<div style="margin-top: 20px;">', unsafe_allow_html=True)
submit_btn = st.button("🚀 Submit Query", type="primary", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ================= PROCESS QUERY =================
if submit_btn:
    if not user_query.strip():
        st.warning("⚠️ Please copy a suggestion or type a question first.")
    elif not API_KEY:
        st.error("🔑 API Key 'OPENROUTER_API_KEY' not configured in Streamlit Cloud secrets!")
        st.info("Go to Settings → Secrets → Add OPENROUTER_API_KEY")
    else:
        with st.spinner("🔍 Consulting Mutual Fund Knowledge Base..."):
            try:
                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                }
                
                system_prompt = f"""You are an expert Mutual Fund consultant and educator.
Target: Commerce students, MBA Finance students, Investment Banking aspirants and professionals.

Use this knowledge base:
{KB}

Guidelines:
- Provide comprehensive, detailed answers
- Use bullet points and examples
- Reference specific topics from KB
- Explain concepts clearly for different audience levels"""

                payload = {
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_query}
                    ],
                    "max_tokens": 1500,
                    "temperature": 0.3
                }
                
                response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
                response.raise_for_status()
                
                answer = response.json()['choices'][0]['message']['content']
                st.session_state.last_answer = answer
                
            except requests.exceptions.Timeout:
                st.error("⏱️ Timeout: API request took too long. Please try again.")
            except requests.exceptions.HTTPError as e:
                if response.status_code == 401:
                    st.error("🔑 Authentication failed. Check your OpenRouter API key.")
                elif response.status_code == 429:
                    st.error("⚠️ Rate limit exceeded. Please wait and try again.")
                else:
                    st.error(f"❌ HTTP Error {response.status_code}: {str(e)}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ================= DISPLAY RESULT =================
if st.session_state.last_answer:
    st.markdown("### 📄 Result:")
    st.markdown(f'<div class="result-box">{st.session_state.last_answer}</div>', unsafe_allow_html=True)
    st.caption("💡 **Tip:** Select and copy the answer above for your notes.")

st.markdown("---")
st.caption("🎯 Target: Commerce | MBA Finance | Investment Banking Aspirants | Professionals | MIT License")