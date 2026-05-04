import streamlit as st
import pandas as pd
from datetime import datetime
import time
import webbrowser

# ══════════════════════════════════════════════════════════════════════════
#  AILYN PRO V144 — 6K RESOLUTION 3D GLASSMISM (FINAL COMBINED V)
# ══════════════════════════════════════════════════════════════════════════

st.set_page_config(page_title="AILYN PRO V144 ULTRA", layout="wide")

class AilynUltraCombined:
    def __init__(self):
        self.name = "AILYN CONSTRUCTION PRO"
        self.project_label = "HOUSE PROJECT"
        self.recipients = "garryboypepito2004@gmail.com,ailyn_peps0678@yahoo.com"
        self.neon = "#00ff88"
        self.gold = "#ffcc00"
        self.bg_image = "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2070"
        
        # System State
        if 'ledger' not in st.session_state: st.session_state.ledger = []
        if 'budget' not in st.session_state: st.session_state.budget = 0.0
        if 'view' not in st.session_state: st.session_state.view = "HOME"
        if 'intro_done' not in st.session_state: st.session_state.intro_done = False

    def inject_ultra_ui(self):
        """Hardware-Accelerated 144Hz Visuals & 3D Glass Physics"""
        st.markdown(f"""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
            
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url("{self.bg_image}");
                background-size: cover;
                background-attachment: fixed;
                font-family: 'Inter', sans-serif;
            }}

            /* 144Hz FLOATING ANIMATION */
            @keyframes floatTile {{
                0% {{ transform: translateY(0px) rotateX(0deg); }}
                50% {{ transform: translateY(-12px) rotateX(2deg); }}
                100% {{ transform: translateY(0px) rotateX(0deg); }}
            }}

            /* REALISTIC 3D GLASS PANEL */
            .glass-panel {{
                background: rgba(255, 255, 255, 0.06);
                backdrop-filter: blur(40px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 45px;
                padding: 60px;
                box-shadow: 0 50px 100px rgba(0,0,0,0.7), inset 0 0 30px rgba(255,255,255,0.05);
                text-align: center;
                margin: 25px auto;
                width: 92%;
            }}

            .label-sub {{ color: {self.neon}; font-weight: 900; letter-spacing: 5px; font-size: 15px; margin-bottom: 10px; }}
            .amount-val {{ color: white; font-size: 65px; font-weight: 900; text-shadow: 0 15px 30px rgba(0,0,0,0.5); }}

            /* 144Hz TILE BUTTONS WITH SPRING-BACK EFFECT */
            .stButton>button {{
                background: rgba(255, 255, 255, 0.04) !important;
                backdrop-filter: blur(20px) !important;
                border: 1px solid rgba(0, 255, 136, 0.4) !important;
                color: {self.neon} !important;
                border-radius: 22px !important;
                height: 115px !important;
                font-weight: 900 !important;
                letter-spacing: 3px !important;
                animation: floatTile 5s ease-in-out infinite;
                transition: all 0.15s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            }}

            .stButton>button:active {{
                transform: scale(0.88) translateY(8px) !important;
                background: {self.neon} !important;
                color: black !important;
                box-shadow: 0 0 60px {self.neon} !important;
            }}

            .stButton>button:hover {{
                border-color: white !important;
                box-shadow: 0 0 45px rgba(0, 255, 136, 0.5) !important;
            }}

            header, footer {{ visibility: hidden; }}
            </style>
        """, unsafe_allow_html=True)

    def trigger_dispatch(self):
        """Unified House Project Dual-Email Reporting"""
        spent = sum(x['Total'] for x in st.session_state.ledger)
        leftover = st.session_state.budget - spent
        
        subject = f"HOUSE PROJECT: Official Inventory Receipt - {datetime.now().strftime('%Y-%m-%d')}"
        greeting = "GOOD TAYLIN,"
        intro_letter = "Here is the greeting letter regarding the material list for our house project update."
        details = f"\n\nBUDGET MONEY: P{st.session_state.budget:,.2f}\nTOTAL SPENT: P{spent:,.2f}\nLEFT OVER MONEY: P{leftover:,.2f}\n\nThank you for your time to see this email Taylin love heart ❤️"
        
        full_body = f"{greeting}\n\n{intro_letter}{details}"
        url = f"https://mail.google.com/mail/?view=cm&fs=1&to={self.recipients}&su={subject}&body={full_body}"
        webbrowser.open_new_tab(url)

    def run(self):
        self.inject_ultra_ui()

        # --- INTRO TRANSITION ---
        if not st.session_state.intro_done:
            intro_placeholder = st.empty()
            intro_placeholder.markdown(f"""
                <div style="height:90vh; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                    <h1 style="color:white; font-size:75px; font-weight:900; letter-spacing:30px; animation: floatTile 2s infinite;">{self.project_label}</h1>
                    <p style="color:{self.neon}; letter-spacing:10px; font-size:14px; opacity:0.8;">V144 ULTRA INITIALIZED</p>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(2.5)
            st.session_state.intro_done = True
            st.rerun()

        if st.session_state.view == "HOME":
            st.markdown(f'<h1 style="text-align:center; color:white; font-weight:900; letter-spacing:12px; margin-bottom:0;">{self.name}</h1>', unsafe_allow_html=True)
            
            # --- 3D BUDGET & LEFT OVER DASHBOARD ---
            spent = sum(x['Total'] for x in st.session_state.ledger)
            leftover = st.session_state.budget - spent
            
            st.markdown(f"""
                <div class="glass-panel">
                    <div style="display:flex; justify-content:space-around; align-items:center;">
                        <div style="flex:1;">
                            <div class="label-sub">BUDGET MONEY</div>
                            <div class="amount-val">₱ {st.session_state.budget:,.2f}</div>
                        </div>
                        <div style="width:2px; height:90px; background:rgba(255,255,255,0.15);"></div>
                        <div style="flex:1;">
                            <div class="label-sub">LEFT OVER MONEY</div>
                            <div class="amount-val" style="color:{self.neon}">₱ {leftover:,.2f}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # --- 6-TILE FLOATING COMMAND GRID ---
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("➕ LOG MATERIAL"): st.session_state.view = "ADD"; st.rerun()
                if st.button("💰 BUDGET SETUP"): st.session_state.view = "CONFIG"; st.rerun()
            with c2:
                if st.button("📧 DUAL DISPATCH"): self.trigger_dispatch()
                if st.button("🔄 REFRESH 144Hz"): st.rerun()
            with c3:
                # Placeholder for dynamic HTML report generation
                st.download_button("📥 HTML REPORT", "Material Summary", "Report.html", "text/html")
                if st.button("⚠️ MASTER RESET"): st.session_state.ledger = []; st.rerun()

            # --- MATERIAL LEDGER LIST ---
            if st.session_state.ledger:
                st.markdown('<h3 style="color:white; text-align:center; letter-spacing:5px; margin-top:40px;">MATERIAL LEDGER</h3>', unsafe_allow_html=True)
                df = pd.DataFrame(st.session_state.ledger)
                st.dataframe(df, use_container_width=True, hide_index=True)

        elif st.session_state.view == "ADD":
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.title("Material Logger")
            item = st.text_input("ITEM DESCRIPTION / TYPE").upper()
            qty = st.number_input("QUANTITY", min_value=1)
            prc = st.number_input("UNIT PRICE (₱)", min_value=0.0)
            if st.button("COMMIT TO LEDGER"):
                st.session_state.ledger.insert(0, {
                    "DATE": datetime.now().strftime("%Y-%m-%d"),
                    "ITEM": item, "QTY": qty, "Total": qty*prc
                })
                st.session_state.view = "HOME"; st.rerun()
            if st.button("EXIT"): st.session_state.view = "HOME"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.view == "CONFIG":
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.title("Financial Control")
            st.session_state.budget = st.number_input("SET BUDGET MONEY AMOUNT", value=st.session_state.budget)
            if st.button("UPDATE BUDGET"): st.session_state.view = "HOME"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    AilynUltraCombined().run()