# Decision Report

- generated_at: 2026-06-12T09:50:43.562242+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6495**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=6495, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.88% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.73% | **+0.37%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.65% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$163.93** / 初期 $100.00 (+63.93%)
- 確定: 1369件 (Win 372 / Loss 441 / Flat 556) / skip 1687件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $163.93

## 4. Latest Market Context

- 更新: 2026-06-12T09:50:37.214529+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.59% price=63812.5
- Funnel: target 769 → liquid 158 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.7 >= 65=1, 4h RSI 81.8 >= 65=1, 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +107.16% | $151,667,249.98 |
| ESPORTS/USDT:USDT | +79.98% | $40,163,880.73 |
| NAORIS/USDT:USDT | +51.34% | $3,448,245.27 |
| XPL/USDT:USDT | +36.88% | $10,858,420.27 |
| SKYAI/USDT:USDT | +30.14% | $16,248,678.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.29% | +3.70% |
| VELVET/USDT:USDT | below_1h_threshold | +3.85% | +3.26% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.67% | +3.08% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +3.44% | +2.86% |
| SOXL/USDT:USDT | below_1h_threshold | +3.35% | +2.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
