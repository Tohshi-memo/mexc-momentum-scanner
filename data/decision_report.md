# Decision Report

- generated_at: 2026-07-03T05:11:48.564621+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8132**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8132, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.46% | **+1.31%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.86% | **+0.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +6.84% | **+0.68%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.78% | **+0.62%** |
| ASK_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.08% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$289.03** / 初期 $100.00 (+189.03%)
- 確定: 2454件 (Win 757 / Loss 818 / Flat 879) / skip 2239件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $289.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.44** / 初期 $100.00 (+5.44%)
- 確定: 586件 (Win 141 / Loss 139 / Flat 306) / skip 957件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0356 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.35% 残高後 $105.44

## 5. Latest Market Context

- 更新: 2026-07-03T05:11:42.687259+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=61509.9
- Funnel: target 834 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +37.76% | $6,016,536.75 |
| MAGMA/USDT:USDT | +31.39% | $5,941,178.28 |
| ZKP/USDT:USDT | +29.72% | $2,423,769.83 |
| GUA/USDT:USDT | +22.40% | $10,073,061.84 |
| THE/USDT:USDT | +18.11% | $2,193,209.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +2.83% | +2.68% |
| CAP/USDT:USDT | below_1h_threshold | +2.32% | +2.17% |
| RPL/USDT:USDT | below_1h_threshold | +2.18% | +2.03% |
| US/USDT:USDT | below_1h_threshold | +1.80% | +1.65% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.39% | +1.24% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
