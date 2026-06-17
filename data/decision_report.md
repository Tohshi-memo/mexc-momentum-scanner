# Decision Report

- generated_at: 2026-06-17T10:58:42.615119+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6925**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6925, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| ASK | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +2.37% | **+1.42%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.69% | **+1.35%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.63% | **+1.18%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$194.84** / 初期 $100.00 (+94.84%)
- 確定: 1798件 (Win 487 / Loss 566 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $194.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.60** / 初期 $100.00 (+0.60%)
- 確定: 198件 (Win 45 / Loss 43 / Flat 110) / skip 138件
- 成長率目線: 平均log +0.000030 / 幾何平均 +0.003% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $100.60

## 5. Latest Market Context

- 更新: 2026-06-17T10:58:35.974101+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=64752.0
- Funnel: target 786 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +55.60% | $7,174,601.23 |
| HIGH/USDT:USDT | +36.13% | $3,080,139.91 |
| SQD/USDT:USDT | +24.23% | $2,973,324.13 |
| ID/USDT:USDT | +22.56% | $1,330,980.13 |
| UNI/USDT:USDT | +17.64% | $59,209,948.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +3.39% | +3.59% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.09% | +2.29% |
| RUNE/USDT:USDT | below_1h_threshold | +1.46% | +1.66% |
| AERO/USDT:USDT | below_1h_threshold | +1.28% | +1.48% |
| XPL/USDT:USDT | below_1h_threshold | +1.12% | +1.32% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
