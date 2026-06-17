# Decision Report

- generated_at: 2026-06-17T08:57:29.716953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6917**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6917, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.03% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.64% | **+1.32%** |
| ASK_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.82** / 初期 $100.00 (+97.82%)
- 確定: 1790件 (Win 485 / Loss 560 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $197.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.56** / 初期 $100.00 (+0.56%)
- 確定: 190件 (Win 42 / Loss 38 / Flat 110) / skip 138件
- 成長率目線: 平均log +0.000029 / 幾何平均 +0.003% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0831 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $100.56

## 5. Latest Market Context

- 更新: 2026-06-17T08:57:25.271033+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.83% price=64960.7
- Funnel: target 784 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +39.19% | $5,668,917.22 |
| ID/USDT:USDT | +26.39% | $1,075,720.61 |
| SQD/USDT:USDT | +22.25% | $2,560,390.04 |
| UNI/USDT:USDT | +15.98% | $55,124,803.76 |
| SPX/USDT:USDT | +15.05% | $9,214,075.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +2.76% | +3.59% |
| PLAY/USDT:USDT | below_1h_threshold | +2.47% | +3.30% |
| STG/USDT:USDT | below_1h_threshold | +1.35% | +2.18% |
| GUA/USDT:USDT | below_1h_threshold | +1.26% | +2.09% |
| LIT/USDT:USDT | below_1h_threshold | +1.22% | +2.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
