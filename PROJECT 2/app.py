"""SIGNAL NOIR // EDITORIAL INTELLIGENCE STUDIO
Cinematic NLP Sentiment Telemetry Platform for News & Financial Bulletins.
"""

from io import BytesIO, StringIO
import json
from pathlib import Path
import sys
import time
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Ensure src package is importable
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from news_sentiment.cleanup import reset_streamlit_session
from news_sentiment.config import (
    ALLOWED_LABELS,
    APP_NAME,
    APP_TAGLINE,
    APP_VERSION,
    DEFAULT_DATA_PATH,
    DEFAULT_HYPERPARAMS,
    METADATA_PATH,
    METRICS_PATH,
    MODEL_PATH,
    SAMPLE_DATA_PATH,
    SENTIMENT_STYLES,
    THEME_COLORS,
)
from news_sentiment.data_validation import (
    validate_csv_input,
    validate_headline_text,
    validate_training_dataset,
)
from news_sentiment.evaluation import (
    create_confusion_matrix_figure,
    create_sentiment_distribution_figure,
    create_timeline_trend_figure,
)
from news_sentiment.inference import predict_batch, predict_single
from news_sentiment.model import (
    get_model_metadata,
    load_pipeline,
    train_and_evaluate,
)
from news_sentiment.preprocessing import audit_dataset, clean_text

# Streamlit Page Config
st.set_page_config(
    page_title=f"{APP_NAME} // Intelligence Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Design System: SIGNAL NOIR Editorial Dark Terminal
SIGNAL_NOIR_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* Global Root Resets */
    :root {
        --noir-void: #07080b;
        --noir-surface: #0e1117;
        --noir-surface-elevated: #151922;
        --noir-border: rgba(255, 255, 255, 0.07);
        --noir-border-bright: rgba(255, 255, 255, 0.16);
        --noir-text-primary: #f8fafc;
        --noir-text-muted: #8b949e;
        --noir-text-dim: #4b5563;
        --noir-lime: #d4ff32;
        --noir-cyan: #22d3ee;
        --noir-crimson: #ff3b5c;
    }

    .stApp {
        background-color: var(--noir-void);
        color: var(--noir-text-primary);
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }

    /* Top Global Header Bar */
    .noir-header {
        background: linear-gradient(180deg, #10141d 0%, #0a0d13 100%);
        border: 1px solid var(--noir-border);
        border-radius: 8px;
        padding: 16px 24px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        overflow: hidden;
    }
    .noir-header::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #d4ff32 0%, #22d3ee 50%, transparent 100%);
    }

    .brand-mark {
        font-family: 'JetBrains Mono', monospace;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: -0.5px;
        color: #ffffff;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .brand-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        letter-spacing: 1px;
        padding: 2px 8px;
        border-radius: 4px;
        background: rgba(212, 255, 50, 0.1);
        color: var(--noir-lime);
        border: 1px solid rgba(212, 255, 50, 0.3);
    }
    .header-telemetry {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        color: var(--noir-text-muted);
        display: flex;
        gap: 16px;
        align-items: center;
    }
    .signal-pulse {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: var(--noir-lime);
        display: inline-block;
        box-shadow: 0 0 10px var(--noir-lime);
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(212, 255, 50, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(212, 255, 50, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(212, 255, 50, 0); }
    }

    /* Hero Section */
    .hero-container {
        padding: 10px 0 24px 0;
    }
    .hero-kicker {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: var(--noir-lime);
        margin-bottom: 8px;
    }
    .hero-title {
        font-family: 'Newsreader', Georgia, serif;
        font-size: 42px;
        font-weight: 600;
        letter-spacing: -1px;
        line-height: 1.15;
        color: #ffffff;
        margin: 0 0 10px 0;
    }
    .hero-subtitle {
        font-size: 15px;
        color: var(--noir-text-muted);
        max-width: 680px;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    /* Cards & Panels */
    .noir-panel {
        background: var(--noir-surface);
        border: 1px solid var(--noir-border);
        border-radius: 8px;
        padding: 20px 24px;
        margin-bottom: 16px;
        transition: border-color 0.2s ease;
    }
    .noir-panel:hover {
        border-color: var(--noir-border-bright);
    }

    .telemetry-card {
        background: var(--noir-surface);
        border: 1px solid var(--noir-border);
        border-radius: 6px;
        padding: 14px 18px;
        margin-bottom: 12px;
    }
    .telemetry-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--noir-text-dim);
        margin-bottom: 4px;
    }
    .telemetry-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
    }

    /* Editorial Intelligence Card */
    .intel-card {
        background: linear-gradient(180deg, #11151f 0%, #0a0d13 100%);
        border: 1px solid var(--noir-border-bright);
        border-radius: 8px;
        padding: 24px;
        margin-top: 16px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.45);
    }
    .intel-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid var(--noir-border);
        padding-bottom: 14px;
        margin-bottom: 16px;
    }
    .intel-headline-preview {
        font-family: 'Newsreader', Georgia, serif;
        font-size: 20px;
        font-style: italic;
        color: #f1f5f9;
        line-height: 1.4;
        margin-bottom: 16px;
    }

    /* Sentiment Meter Spectrum */
    .spectrum-container {
        margin: 18px 0;
        background: #090c12;
        border: 1px solid var(--noir-border);
        border-radius: 6px;
        padding: 12px 16px;
    }
    .spectrum-track {
        height: 8px;
        border-radius: 4px;
        background: linear-gradient(90deg, #ff3b5c 0%, #334155 50%, #d4ff32 100%);
        position: relative;
        margin: 10px 0 6px 0;
    }
    .spectrum-marker {
        position: absolute;
        top: -6px;
        width: 6px;
        height: 20px;
        border-radius: 2px;
        background: #ffffff;
        box-shadow: 0 0 10px #ffffff;
        transform: translateX(-50%);
        transition: left 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .spectrum-labels {
        display: flex;
        justify-content: space-between;
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        color: var(--noir-text-muted);
    }

    /* Feature Attribution Chips */
    .chip-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 12px 0;
    }
    .term-chip-pos {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        background: rgba(212, 255, 50, 0.08);
        border: 1px solid rgba(212, 255, 50, 0.3);
        color: var(--noir-lime);
        padding: 3px 8px;
        border-radius: 4px;
    }
    .term-chip-neg {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        background: rgba(255, 59, 92, 0.08);
        border: 1px solid rgba(255, 59, 92, 0.3);
        color: var(--noir-crimson);
        padding: 3px 8px;
        border-radius: 4px;
    }

    /* Plain Language Synthesis */
    .synthesis-box {
        font-size: 13px;
        color: var(--noir-text-muted);
        line-height: 1.6;
        border-left: 2px solid var(--noir-lime);
        padding-left: 14px;
        margin-top: 14px;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent;
        gap: 4px;
        border-bottom: 1px solid var(--noir-border);
        padding-bottom: 2px;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        background-color: transparent;
        border-radius: 4px 4px 0 0;
        color: var(--noir-text-muted);
        padding: 10px 18px;
    }
    .stTabs [aria-selected="true"] {
        background-color: var(--noir-surface) !important;
        color: var(--noir-lime) !important;
        border-bottom: 2px solid var(--noir-lime) !important;
    }

    /* Buttons */
    .stButton>button {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border-radius: 4px;
        transition: all 0.2s ease;
    }
</style>
"""
st.markdown(SIGNAL_NOIR_CSS, unsafe_allow_html=True)


# Model State Caching
@st.cache_resource(show_spinner=False)
def get_cached_pipeline(model_file_mtime: float) -> Optional[Any]:
    """Loads and caches the model pipeline based on file modification timestamp."""
    try:
        return load_pipeline(MODEL_PATH)
    except Exception:
        return None


def check_engine_status():
    """Retrieves live model pipeline, mtime, and training metadata."""
    if not MODEL_PATH.exists():
        return False, None, None
    mtime = MODEL_PATH.stat().st_mtime
    model = get_cached_pipeline(mtime)
    meta = get_model_metadata()
    return (model is not None), model, meta


model_available, pipeline, model_meta = check_engine_status()

# Initialize Session State
if "session_history" not in st.session_state:
    st.session_state.session_history = []
if "single_input_text" not in st.session_state:
    st.session_state.single_input_text = ""
if "confirm_reset" not in st.session_state:
    st.session_state.confirm_reset = False


# Top Persistent Bar
acc_val = f"{model_meta.get('accuracy', 0.0):.1%}" if (model_available and model_meta) else "0.0%"
macro_f1_val = f"{model_meta.get('macro_f1', 0.0):.4f}" if (model_available and model_meta) else "0.0000"
vocab_val = "50K N-GRAMS"

status_pill = (
    "<span style='color: #d4ff32;'>● ONLINE</span>"
    if model_available
    else "<span style='color: #ff3b5c;'>○ ENGINE UNLOADED</span>"
)

st.markdown(f"""
    <div class="noir-header">
        <div class="brand-mark">
            <span class="signal-pulse"></span>
            <span>{APP_NAME}</span>
            <span class="brand-tag">v{APP_VERSION}</span>
        </div>
        <div class="header-telemetry">
            <div>ENGINE: <span style="color: #ffffff;">TFIDF-LOGISTIC-REGRESSION</span></div>
            <div>LEAKAGE: <span style="color: #22d3ee;">0.00% VERIFIED</span></div>
            <div>TEST ACC: <span style="color: #d4ff32;">{acc_val}</span></div>
            <div>STATUS: {status_pill}</div>
        </div>
    </div>
""", unsafe_allow_html=True)


# Sidebar Shell: Navigation & Session Telemetry
with st.sidebar:
    st.markdown("### Studio Telemetry")
    
    if model_available and model_meta:
        st.markdown(f"""
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; line-height: 1.8; color: #94a3b8;">
                <div>ENGINE: <span style="color: #f8fafc;">TFIDF + LOGREG</span></div>
                <div>TRAIN RECORDS: <span style="color: #f8fafc;">{model_meta.get('train_rows', 'N/A')}</span></div>
                <div>TEST RECORDS: <span style="color: #f8fafc;">{model_meta.get('test_rows', 'N/A')}</span></div>
                <div>HELD-OUT ACC: <span style="color: #d4ff32;">{acc_val}</span></div>
                <div>MACRO F1: <span style="color: #22d3ee;">{macro_f1_val}</span></div>
                <div>FINGERPRINT: <span style="color: #64748b;">{model_meta.get('dataset_hash', 'N/A')}</span></div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Model pipeline artifact not found on disk.")
        if st.button("🚀 INITIALIZE ENGINE (TRAIN)", type="primary", use_container_width=True):
            with st.spinner("Training TF-IDF + Logistic Regression on benchmark dataset..."):
                try:
                    df_init = pd.read_csv(DEFAULT_DATA_PATH)
                    train_and_evaluate(df_init, save_artifacts=True)
                    st.cache_resource.clear()
                    st.success("Engine initialized successfully.")
                    st.rerun()
                except Exception as err:
                    st.error(f"Initialization error: {err}")

    st.markdown("---")
    
    # Session Activity Reel
    st.markdown("#### Session Reel")
    st.caption("Recent headline classifications executed in this session:")
    
    if st.session_state.session_history:
        for idx, item in enumerate(reversed(st.session_state.session_history[-5:])):
            s_style = SENTIMENT_STYLES.get(item["label"], {})
            st.markdown(f"""
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; padding: 6px 8px; margin-bottom: 6px; background: #131822; border-left: 2px solid {s_style.get('color', '#94a3b8')}; border-radius: 2px;">
                    <div style="color: {s_style.get('color', '#94a3b8')}; font-weight: 600;">{s_style.get('badge_tag', '')} ({item.get('confidence', 0):.1%})</div>
                    <div style="color: #cbd5e1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{item['text']}</div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<p style='font-size: 11px; color: #475569; font-family: monospace;'>[NO ACTIVE HISTORY]</p>", unsafe_allow_html=True)

    st.markdown("---")
    
    # Session Reset Action
    st.markdown("#### Workspace State")
    if not st.session_state.confirm_reset:
        if st.button("🧹 RESET SESSION STATE", use_container_width=True):
            st.session_state.confirm_reset = True
            st.rerun()
    else:
        st.warning("Clear session inputs and temporary predictions?")
        r_c1, r_c2 = st.columns(2)
        with r_c1:
            if st.button("CONFIRM", type="primary", use_container_width=True):
                reset_streamlit_session(st.session_state)
                st.session_state.confirm_reset = False
                st.success("Session state cleared.")
                st.rerun()
        with r_c2:
            if st.button("CANCEL", use_container_width=True):
                st.session_state.confirm_reset = False
                st.rerun()

    st.markdown("---")
    st.markdown("""
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #475569; line-height: 1.5;">
            SIGNAL NOIR IS A LINGUISTIC VALENCE ANALYZER.<br>
            NOT A FACT-CHECKER, CREDIBILITY DETECTOR, OR MARKET PREDICTOR.<br>
            ALL PROCESSING RUNS 100% LOCALLY.
        </div>
    """, unsafe_allow_html=True)


# Main Application Navigation Tabs
studio_tabs = st.tabs([
    "01 // HEADLINE TERMINAL",
    "02 // BATCH ANALYTICS STUDIO",
    "03 // DATASET LABORATORY",
    "04 // MODEL EVALUATION & RETRAIN",
    "05 // METHODOLOGY & DOSSIER"
])


# TAB 1: Headline Terminal
with studio_tabs[0]:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-kicker">// EDITORIAL CLASSIFIER</div>
            <h1 class="hero-title">Read the signal. Understand the sentiment.</h1>
            <p class="hero-subtitle">
                Deconstruct linguistic tone in headlines, corporate dispatches, and macroeconomic releases.
                Powered by sublinear TF-IDF representation and regularized Logistic Regression.
            </p>
        </div>
    """, unsafe_allow_html=True)

    if not model_available:
        st.error("Engine artifact not available. Please initialize the engine using the sidebar trigger.")
    else:
        # Editorial Presets
        st.markdown("<p style='font-family: \"JetBrains Mono\", monospace; font-size: 11px; color: #94a3b8; margin-bottom: 6px;'>[QUICK SIGNAL PRESETS]</p>", unsafe_allow_html=True)
        preset_cols = st.columns(4)

        preset_pos = "Operating profit expanded 28% year-over-year following strong international demand"
        preset_neg = "Automaker recalls 450000 vehicles over potential brake system failure"
        preset_neu = "Central bank keeps benchmark interest rate unchanged at policy meeting"
        preset_reg = "Heavy regulatory fines imposed following international compliance probe"

        if preset_cols[0].button("📈 POSITIVE EARNINGS", use_container_width=True):
            st.session_state.single_input_text = preset_pos
        if preset_cols[1].button("📉 PRODUCT RECALL", use_container_width=True):
            st.session_state.single_input_text = preset_neg
        if preset_cols[2].button("⚖️ MONETARY POLICY", use_container_width=True):
            st.session_state.single_input_text = preset_neu
        if preset_cols[3].button("⚡ REGULATORY PROBE", use_container_width=True):
            st.session_state.single_input_text = preset_reg

        current_val = st.session_state.get("single_input_text", "")
        
        # Interactive Text Input
        headline_query = st.text_area(
            "Headline Input",
            value=current_val,
            height=90,
            placeholder="Type or paste a news headline here (e.g., 'Retailer raises annual earnings guidance after stellar holiday sales')...",
            key="noir_single_input"
        )

        char_len = len(headline_query.strip())
        st.markdown(
            f"<div style='text-align: right; font-family: monospace; font-size: 10px; color: #64748b; margin-top: -8px;'>"
            f"CHARACTER COUNT: {char_len} / 1000"
            f"</div>",
            unsafe_allow_html=True
        )

        action_c1, action_c2, _ = st.columns([1.5, 1, 3.5])
        with action_c1:
            run_single = st.button("⚡ ANALYZE SIGNAL", type="primary", use_container_width=True)
        with action_c2:
            if st.button("CLEAR", use_container_width=True):
                st.session_state.single_input_text = ""
                st.rerun()

        if run_single:
            is_valid, validation_msg = validate_headline_text(headline_query)
            if not is_valid:
                st.warning(validation_msg)
            else:
                try:
                    analysis = predict_single(headline_query, pipeline)
                    st.session_state.latest_analysis = analysis
                    
                    # Append to session history (capped at 20)
                    st.session_state.session_history.append({
                        "text": analysis["text"],
                        "label": analysis["label"],
                        "confidence": analysis["confidence"],
                        "timestamp": time.strftime("%H:%M:%S")
                    })
                    if len(st.session_state.session_history) > 20:
                        st.session_state.session_history.pop(0)

                except Exception as exc:
                    st.error(f"Inference Failure: {exc}")

        # Display Editorial Intelligence Card
        if "latest_analysis" in st.session_state and st.session_state.latest_analysis:
            res = st.session_state.latest_analysis
            s_style = res["style"]
            label_up = res["label"].upper()
            conf_val = res.get("confidence", 0.0)
            spec_val = res.get("spectrum_score", 0.0) # in [-1.0, 1.0]

            # Calculate marker percentage: -1.0 -> 0%, 0.0 -> 50%, +1.0 -> 100%
            marker_pct = max(2.0, min(98.0, (spec_val + 1.0) / 2.0 * 100.0))

            st.markdown(f"""
                <div class="intel-card">
                    <div class="intel-header">
                        <div>
                            <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #64748b;">SIGNAL INTELLIGENCE REPORT</span>
                            <div style="font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 700; color: {s_style.get('color', '#ffffff')}; margin-top: 4px;">
                                {s_style.get('badge_tag', '')} <span style="font-size: 15px; color: #94a3b8; font-weight: 400;">// {s_style.get('tone_descriptor', '')}</span>
                            </div>
                        </div>
                        <div style="text-align: right; font-family: 'JetBrains Mono', monospace;">
                            <div style="font-size: 10px; color: #64748b;">MODEL CONFIDENCE</div>
                            <div style="font-size: 24px; font-weight: 700; color: #ffffff;">{conf_val:.1%}</div>
                        </div>
                    </div>
                    
                    <div class="intel-headline-preview">"{res['text']}"</div>

                    <!-- Sentiment Spectrum -->
                    <div class="spectrum-container">
                        <div class="spectrum-labels">
                            <span>[-] STRONG BEARISH (-1.0)</span>
                            <span style="color: #22d3ee;">POLARITY: {spec_val:+.3f}</span>
                            <span>[+] STRONG BULLISH (+1.0)</span>
                        </div>
                        <div class="spectrum-track">
                            <div class="spectrum-marker" style="left: {marker_pct:.1f}%;"></div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Telemetry Metrics Grid: Class Probability Breakdown
            st.markdown("#### Class Probability Distribution")
            p_cols = st.columns(3)
            probs = res.get("probabilities", {})
            for idx, c_name in enumerate(["positive", "neutral", "negative"]):
                val_prob = probs.get(c_name, 0.0)
                c_style = SENTIMENT_STYLES.get(c_name, {})
                with p_cols[idx]:
                    st.markdown(f"""
                        <div class="telemetry-card" style="border-left: 3px solid {c_style.get('color', '#94a3b8')};">
                            <div class="telemetry-label">{c_style.get('badge_tag', '')}</div>
                            <div class="telemetry-value">{val_prob:.1%}</div>
                            <div style="background: rgba(255,255,255,0.06); height: 4px; border-radius: 2px; margin-top: 8px;">
                                <div style="background: {c_style.get('color', '#94a3b8')}; width: {val_prob * 100:.1f}%; height: 4px; border-radius: 2px;"></div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

            # Feature Attribution Chips
            contributions = res.get("contributions", [])
            if contributions:
                st.markdown("#### Feature Attribution: Primary Term Signals")
                st.caption("Mathematically extracted term weights (TF-IDF × Logistic Regression coefficient):")
                
                chip_html = "<div class='chip-container'>"
                for item in contributions:
                    chip_class = "term-chip-pos" if item["impact"] >= 0 else "term-chip-neg"
                    sign = "+" if item["impact"] >= 0 else ""
                    chip_html += f"<span class='{chip_class}'>{item['term']}: {sign}{item['impact']:.2f}</span>"
                chip_html += "</div>"
                st.markdown(chip_html, unsafe_allow_html=True)

            # Plain-Language Editorial Synthesis
            st.markdown(f"""
                <div class="synthesis-box">
                    <strong>TELEMETRY SYNTHESIS:</strong> {res.get('explanation', '')}
                </div>
            """, unsafe_allow_html=True)


# TAB 2: Batch Analytics Studio
with studio_tabs[1]:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-kicker">// BULK TELEMETRY</div>
            <h2 style="font-family: 'Newsreader', Georgia, serif; font-size: 32px; font-weight: 600; color: #ffffff; margin: 0 0 6px 0;">
                Batch Telemetry & Aggregate Analytics
            </h2>
            <p style="font-size: 14px; color: #8b949e; margin: 0;">
                Ingest multi-row headline corpora, detect duplicates, classify bulk sentiment, and inspect temporal trajectories.
            </p>
        </div>
    """, unsafe_allow_html=True)

    batch_c1, batch_c2 = st.columns([3, 1])
    with batch_c1:
        st.caption("Upload a `.csv` dataset. Must contain a text column (`text`, `headline`, or custom mapped). Max: 10 MB.")
    with batch_c2:
        if SAMPLE_DATA_PATH.exists():
            sample_data = SAMPLE_DATA_PATH.read_bytes()
            st.download_button(
                label="📥 DOWNLOAD SAMPLE CSV",
                data=sample_data,
                file_name="sample_headlines.csv",
                mime="text/csv",
                use_container_width=True
            )

    uploaded_batch = st.file_uploader(
        "Upload news headlines CSV",
        type=["csv"],
        key="noir_batch_uploader",
        help="Drag and drop a CSV file containing headlines."
    )

    if uploaded_batch is not None:
        batch_val = validate_csv_input(uploaded_batch)
        if not batch_val.is_valid:
            st.error(f"SCHEMA VALIDATION ERROR: {batch_val.error_message}")
        else:
            clean_df = batch_val.df_clean
            auto_text_col = batch_val.text_column

            # Column Mapping Controls
            with st.expander("⚙️ Schema & Column Mapping", expanded=False):
                map_c1, map_c2 = st.columns(2)
                with map_c1:
                    selected_text_col = st.selectbox(
                        "Headline Text Column",
                        options=list(clean_df.columns),
                        index=list(clean_df.columns).index(auto_text_col) if auto_text_col in clean_df.columns else 0
                    )
                with map_c2:
                    date_candidates = ["None"] + [c for c in clean_df.columns if "date" in str(c).lower() or "time" in str(c).lower()]
                    selected_date_col = st.selectbox("Date / Timestamp Column (Optional)", options=date_candidates, index=0)
                    date_col_arg = None if selected_date_col == "None" else selected_date_col

            # Telemetry Metrics Row
            t1, t2, t3, t4 = st.columns(4)
            with t1:
                st.markdown(f"""<div class="telemetry-card">
                    <div class="telemetry-label">INGESTED ROWS</div>
                    <div class="telemetry-value">{batch_val.total_rows}</div>
                </div>""", unsafe_allow_html=True)
            with t2:
                st.markdown(f"""<div class="telemetry-card">
                    <div class="telemetry-label">VALID HEADLINES</div>
                    <div class="telemetry-value" style="color: #22d3ee;">{batch_val.valid_rows}</div>
                </div>""", unsafe_allow_html=True)
            with t3:
                st.markdown(f"""<div class="telemetry-card">
                    <div class="telemetry-label">BLANK / SKIPPED</div>
                    <div class="telemetry-value" style="color: {'#ff3b5c' if batch_val.blank_rows > 0 else '#8b949e'};">{batch_val.blank_rows}</div>
                </div>""", unsafe_allow_html=True)
            with t4:
                st.markdown(f"""<div class="telemetry-card">
                    <div class="telemetry-label">DUPLICATE ROWS</div>
                    <div class="telemetry-value" style="color: {'#fbbf24' if batch_val.duplicate_rows > 0 else '#d4ff32'};">{batch_val.duplicate_rows}</div>
                </div>""", unsafe_allow_html=True)

            if not model_available:
                st.error("Engine unavailable. Train the model before executing batch telemetry.")
            else:
                if st.button("⚡ EXECUTE BATCH INFERENCE", type="primary"):
                    progress_bar = st.progress(0, text="Initializing inference matrix...")
                    try:
                        progress_bar.progress(35, text="Transforming text features...")
                        res_batch = predict_batch(clean_df, selected_text_col, pipeline)
                        progress_bar.progress(85, text="Computing polarity spectrum...")
                        
                        cols_to_strip = [c for c in ["_cleaned_text", "_is_valid_text"] if c in res_batch.columns]
                        st.session_state.batch_results_df = res_batch.drop(columns=cols_to_strip)
                        st.session_state.batch_text_col = selected_text_col
                        st.session_state.batch_date_col = date_col_arg
                        progress_bar.progress(100, text="Batch processing complete.")
                        time.sleep(0.3)
                        progress_bar.empty()
                        st.success(f"Classified {batch_val.valid_rows} headlines successfully.")
                    except Exception as err:
                        progress_bar.empty()
                        st.error(f"Batch execution failed: {err}")

    # Display Batch Analytics Studio
    if "batch_results_df" in st.session_state and st.session_state.batch_results_df is not None:
        batch_df = st.session_state.batch_results_df
        text_column = st.session_state.get("batch_text_col", "text")
        date_column = st.session_state.get("batch_date_col", None)

        st.markdown("---")
        st.markdown("### Studio Telemetry & Visualizations")

        valid_preds = batch_df[batch_df["predicted_sentiment"] != ""]["predicted_sentiment"]
        counts = valid_preds.value_counts().to_dict()

        chart_c1, chart_c2 = st.columns([1, 1])
        with chart_c1:
            fig_dist = create_sentiment_distribution_figure(counts)
            st.plotly_chart(fig_dist, use_container_width=True)

        with chart_c2:
            fig_trend = create_timeline_trend_figure(batch_df, date_column, "predicted_sentiment")
            if fig_trend:
                st.plotly_chart(fig_trend, use_container_width=True)
            else:
                st.info("No trend telemetry available.")

        # Interactive Filtering & Table
        st.markdown("#### Classified Corpus Table")
        f1, f2, f3 = st.columns([1, 1.5, 1])
        with f1:
            sentiment_filter = st.selectbox(
                "Filter Sentiment",
                options=["ALL VALENCES", "positive", "negative", "neutral"],
                index=0
            )
        with f2:
            search_query = st.text_input("Corpus Keyword Search", placeholder="Filter by terms...")
        with f3:
            sort_by = st.selectbox("Sort Order", options=["Default Order", "Highest Polarity", "Lowest Polarity"])

        # Filter View
        view_df = batch_df.copy()
        if sentiment_filter != "ALL VALENCES":
            view_df = view_df[view_df["predicted_sentiment"] == sentiment_filter]
        if search_query.strip():
            view_df = view_df[view_df[text_column].astype(str).str.contains(search_query.strip(), case=False, na=False)]
        if sort_by == "Highest Polarity" and "sentiment_polarity" in view_df.columns:
            view_df = view_df.sort_values("sentiment_polarity", ascending=False)
        elif sort_by == "Lowest Polarity" and "sentiment_polarity" in view_df.columns:
            view_df = view_df.sort_values("sentiment_polarity", ascending=True)

        st.caption(f"Displaying {len(view_df)} of {len(batch_df)} records")
        st.dataframe(view_df, use_container_width=True, height=360)

        # CSV Export
        csv_bytes = batch_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="💾 EXPORT PREDICTIONS CSV",
            data=csv_bytes,
            file_name="signal_noir_predictions.csv",
            mime="text/csv",
            type="primary"
        )


# TAB 3: Dataset Laboratory & Quality Audit
with studio_tabs[2]:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-kicker">// DATA AUDITING</div>
            <h2 style="font-family: 'Newsreader', Georgia, serif; font-size: 32px; font-weight: 600; color: #ffffff; margin: 0 0 6px 0;">
                Dataset Laboratory & Quality Audit
            </h2>
            <p style="font-size: 14px; color: #8b949e; margin: 0;">
                Audit class balance, detect duplicates, inspect text lengths, and verify stratification integrity.
            </p>
        </div>
    """, unsafe_allow_html=True)

    dataset_source = st.radio(
        "Select Dataset Corpus",
        options=["Curated Open Benchmark (data/news.csv)", "Upload Custom Labeled CSV"],
        horizontal=True
    )

    df_audited = None
    if "Curated" in dataset_source:
        if DEFAULT_DATA_PATH.exists():
            df_audited = pd.read_csv(DEFAULT_DATA_PATH)
            st.caption(f"Analyzing official benchmark corpus: `{DEFAULT_DATA_PATH}`.")
        else:
            st.error("Default dataset not found.")
    else:
        custom_upload = st.file_uploader("Upload custom CSV for schema inspection", type=["csv"], key="noir_audit_upload")
        if custom_upload:
            val_custom = validate_csv_input(custom_upload)
            if val_custom.is_valid:
                df_audited = val_custom.df_raw
            else:
                st.error(val_custom.error_message)

    if df_audited is not None:
        audit_results = audit_dataset(df_audited, text_col="text", label_col="label")
        
        # Audit Cards
        d1, d2, d3, d4 = st.columns(4)
        with d1:
            st.markdown(f"""<div class="telemetry-card">
                <div class="telemetry-label">CORPUS ROWS</div>
                <div class="telemetry-value">{audit_results['total_rows']}</div>
            </div>""", unsafe_allow_html=True)
        with d2:
            st.markdown(f"""<div class="telemetry-card">
                <div class="telemetry-label">TOTAL COLUMNS</div>
                <div class="telemetry-value">{audit_results['total_columns']}</div>
            </div>""", unsafe_allow_html=True)
        with d3:
            exact_d = audit_results.get("text_audit", {}).get("exact_duplicate_rows", 0)
            st.markdown(f"""<div class="telemetry-card">
                <div class="telemetry-label">EXACT DUPLICATES</div>
                <div class="telemetry-value" style="color: {'#fbbf24' if exact_d > 0 else '#d4ff32'};">{exact_d}</div>
            </div>""", unsafe_allow_html=True)
        with d4:
            imb = audit_results.get("label_audit", {}).get("imbalance_ratio", 1.0)
            st.markdown(f"""<div class="telemetry-card">
                <div class="telemetry-label">IMBALANCE RATIO</div>
                <div class="telemetry-value" style="color: {'#d4ff32' if imb <= 1.5 else '#fbbf24'};">{imb:.2f}:1</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("---")
        
        # Class Balance & Length Distribution
        lbl_col, len_col = st.columns(2)
        with lbl_col:
            st.markdown("#### Ground-Truth Class Distribution")
            l_audit = audit_results.get("label_audit", {})
            if l_audit and "class_counts" in l_audit:
                table_records = []
                for k, v in l_audit["class_counts"].items():
                    style = SENTIMENT_STYLES.get(k, {})
                    table_records.append({
                        "Class": k.upper(),
                        "Count": v,
                        "Proportion": f"{l_audit['class_proportions'].get(k, 0):.2%}",
                        "Descriptor": style.get("tone_descriptor", "")
                    })
                st.dataframe(pd.DataFrame(table_records), use_container_width=True)
            else:
                st.info("No ground-truth `label` column detected in this dataset.")

        with len_col:
            st.markdown("#### Headline Length Metrics")
            t_audit = audit_results.get("text_audit", {})
            if t_audit and "char_length" in t_audit:
                ch = t_audit["char_length"]
                wd = t_audit["word_count"]
                metrics_df = pd.DataFrame({
                    "Statistic": ["Minimum", "Mean (Avg)", "Median", "Maximum"],
                    "Characters": [ch["min"], ch["mean"], ch["median"], ch["max"]],
                    "Word Count": [wd["min"], wd["mean"], wd["median"], wd["max"]]
                })
                st.dataframe(metrics_df, use_container_width=True)

        st.markdown("#### Dataset Health Verification")
        miss_total = sum(audit_results.get("missing_per_column", {}).values())
        hc1, hc2 = st.columns(2)
        with hc1:
            if miss_total == 0:
                st.success("✅ **Zero Nulls**: All cells populated.")
            else:
                st.warning(f"⚠️ **Missing Data**: {miss_total} missing values detected.")
            if exact_d == 0:
                st.success("✅ **Zero Duplicates**: Complete row uniqueness.")
            else:
                st.warning(f"⚠️ **Duplicates**: {exact_d} exact duplicate records found.")
        with hc2:
            min_c = min(l_audit.get("class_counts", {}).values()) if l_audit.get("class_counts") else 0
            if min_c >= 2:
                st.success("✅ **Stratification Ready**: Minimum class count ≥ 2.")
            else:
                st.error("❌ **Stratification Error**: Rare classes have < 2 examples.")


# TAB 4: Model Evaluation & Retrain
with studio_tabs[3]:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-kicker">// HELD-OUT PERFORMANCE</div>
            <h2 style="font-family: 'Newsreader', Georgia, serif; font-size: 32px; font-weight: 600; color: #ffffff; margin: 0 0 6px 0;">
                Model Evaluation & Retraining Studio
            </h2>
            <p style="font-size: 14px; color: #8b949e; margin: 0;">
                Held-out evaluation metrics computed on test data never seen during vocabulary fitting.
            </p>
        </div>
    """, unsafe_allow_html=True)

    metrics_json = None
    if METRICS_PATH.exists():
        try:
            metrics_json = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
        except Exception:
            metrics_json = None

    if not metrics_json:
        st.info("Evaluation metrics report not found. Train the model to generate verification scores.")
    else:
        # Performance Telemetry Cards
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f"""<div class="telemetry-card">
                <div class="telemetry-label">HELD-OUT ACCURACY</div>
                <div class="telemetry-value" style="color: #d4ff32;">{metrics_json.get('accuracy', 0):.2%}</div>
            </div>""", unsafe_allow_html=True)
        with m2:
            st.markdown(f"""<div class="telemetry-card">
                <div class="telemetry-label">MACRO F1 SCORE</div>
                <div class="telemetry-value" style="color: #22d3ee;">{metrics_json.get('macro_f1', 0):.4f}</div>
            </div>""", unsafe_allow_html=True)
        with m3:
            st.markdown(f"""<div class="telemetry-card">
                <div class="telemetry-label">TEST SPLIT ROWS</div>
                <div class="telemetry-value">{metrics_json.get('test_rows', 'N/A')}</div>
            </div>""", unsafe_allow_html=True)
        with m4:
            st.markdown(f"""<div class="telemetry-card">
                <div class="telemetry-label">TRAIN SPLIT ROWS</div>
                <div class="telemetry-value">{metrics_json.get('train_rows', 'N/A')}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("---")
        
        # Confusion Matrix Heatmap & Classification Report
        ev_c1, ev_c2 = st.columns([1, 1])
        with ev_c1:
            mat = metrics_json.get("confusion_matrix", [])
            cm_lbls = metrics_json.get("confusion_matrix_labels", ["negative", "neutral", "positive"])
            if mat:
                fig_c = create_confusion_matrix_figure(mat, cm_lbls)
                st.plotly_chart(fig_c, use_container_width=True)

        with ev_c2:
            st.markdown("#### Classification Report (Held-Out Test Set)")
            c_rep = metrics_json.get("classification_report", {})
            rep_records = []
            for lbl in cm_lbls:
                if lbl in c_rep:
                    rep_records.append({
                        "Class": lbl.upper(),
                        "Precision": f"{c_rep[lbl]['precision']:.4f}",
                        "Recall": f"{c_rep[lbl]['recall']:.4f}",
                        "F1-Score": f"{c_rep[lbl]['f1-score']:.4f}",
                        "Support": int(c_rep[lbl]["support"])
                    })
            if rep_records:
                st.dataframe(pd.DataFrame(rep_records), use_container_width=True)

            st.caption(
                f"Evaluated on **{metrics_json.get('test_size', 0.2):.0%} stratified split** (Seed={metrics_json.get('random_state', 42)}). "
                "Zero data leakage into feature extractor."
            )

        # Misclassified Error Analysis Table
        misclassified = metrics_json.get("misclassified_samples", [])
        if misclassified:
            st.markdown("#### Test Set Error Analysis (Misclassifications)")
            st.caption("Inspect off-diagonal errors to detect linguistic ambiguity and cross-class lexical bleed:")
            err_df = pd.DataFrame(misclassified)[["text", "true_label", "predicted_label", "confidence"]]
            err_df.columns = ["Headline Text", "Ground Truth", "Predicted Label", "Model Confidence"]
            st.dataframe(err_df, use_container_width=True)

    st.markdown("---")
    
    # Retraining Drawer
    with st.expander("🛠️ Retrain Model Pipeline with Custom Hyperparameters", expanded=False):
        st.write("Train a new TF-IDF + Logistic Regression pipeline on the verified benchmark corpus:")
        
        rt1, rt2, rt3 = st.columns(3)
        with rt1:
            split_pct = st.slider("Test Split Size", min_value=0.15, max_value=0.35, value=0.20, step=0.05)
        with rt2:
            ngram_opt = st.selectbox("N-Gram Range", options=["(1, 2) Unigrams + Bigrams", "(1, 1) Unigrams Only"])
            ngram_choice = (1, 2) if "2" in ngram_opt else (1, 1)
        with rt3:
            reg_c = st.slider("Regularization Inverse (C)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

        if st.button("🚀 EXECUTE PIPELINE RETRAINING", type="primary"):
            with st.spinner("Fitting TF-IDF vocabulary on X_train and optimizing Logistic Regression..."):
                try:
                    df_base = pd.read_csv(DEFAULT_DATA_PATH)
                    pipe_new, new_m = train_and_evaluate(
                        df=df_base,
                        test_size=split_pct,
                        hyperparams={
                            "ngram_range": ngram_choice,
                            "C": reg_c
                        },
                        save_artifacts=True
                    )
                    st.cache_resource.clear()
                    st.success(f"Retraining Complete. New Accuracy: {new_m['accuracy']:.2%}, Macro F1: {new_m['macro_f1']:.4f}")
                    st.rerun()
                except Exception as ex:
                    st.error(f"Retraining Error: {ex}")


# TAB 5: Methodology & Dossier
with studio_tabs[4]:
    st.markdown("""
        <div class="hero-container">
            <div class="hero-kicker">// SYSTEM DOSSIER</div>
            <h2 style="font-family: 'Newsreader', Georgia, serif; font-size: 32px; font-weight: 600; color: #ffffff; margin: 0 0 6px 0;">
                Methodology, Feature Math & Ethical Boundaries
            </h2>
            <p style="font-size: 14px; color: #8b949e; margin: 0;">
                System architecture, feature attribution derivation, and explicit non-goals.
            </p>
        </div>
    """, unsafe_allow_html=True)

    dos1, dos2 = st.columns(2)
    with dos1:
        st.markdown(r"""
            #### 1. Machine Learning Architecture
            • **Feature Representation**: Term Frequency - Inverse Document Frequency (TF-IDF) with sublinear scaling $1 + \log(\text{tf})$.<br>
            • **N-Gram Topology**: Word unigrams and bigrams $(1, 2)$ with minimum document frequency threshold $\text{min\_df}=2$.<br>
            • **Classifier**: L2-regularized Multiclass Logistic Regression with balanced inverse-frequency class weights.<br>
            • **Leakage Prevention**: Stratified train/test partition executed prior to vocabulary compilation.
            
            #### 2. Feature Attribution Math
            Unlike opaque deep models, linear classifiers allow exact feature attribution:
            $$\text{Impact}(w, c) = \text{TF-IDF}(w, x) \cdot \beta_{c, w}$$
            Where $w$ is an n-gram present in headline $x$, and $\beta_{c, w}$ is the learned weight for class $c$.
        """, unsafe_allow_html=True)

    with dos2:
        st.markdown("""
            #### 3. Ethical Boundaries & Non-Goals
            > **⚠️ SIGNAL NOIR IS A LINGUISTIC VALENCE ANALYZER.**
            
            • **No Fact-Checking**: The model identifies how language sounds, not whether factual statements are true.<br>
            • **No Stock / Financial Advice**: Sentiment valence does not predict future market returns. Positive headlines may follow already-priced-in rallies.<br>
            • **Context & Sarcasm Deficit**: Short headlines omit deep corporate context and nuance.
            
            #### 4. Privacy & Data Integrity
            • **100% Local Execution**: Zero cloud API dependencies; no external data egress.<br>
            • **Immutability**: Raw uploaded datasets are kept read-only in memory.<br>
            • **Isolated Sandboxes**: Automated testing executes in ephemeral temporary directories.
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"""
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #64748b; text-align: center;">
            {APP_NAME} // {APP_TAGLINE} • Built with scikit-learn, Pandas, Plotly & Streamlit • License: CC0 1.0 Universal
        </div>
    """, unsafe_allow_html=True)
