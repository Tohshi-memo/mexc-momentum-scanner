# Decision Report

- generated_at: 2026-09-16T11:41:42.891881+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14676**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14676, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.31% | **-2.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.60% | **+0.72%** |
| LIMIT_9PCT | 5/20 | 25.0% | +2.52% | **+0.63%** |
| LIMIT_7PCT | 8/20 | 40.0% | +1.55% | **+0.62%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +3.18% | **+3.02%** |
| MARKET_LONG | 20/20 | 100.0% | +2.25% | **+2.25%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.65% | **+1.98%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.02% | **+1.81%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.83% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,105.77** / 初期 $100.00 (+1005.77%)
- 確定: 5554件 (Win 1659 / Loss 1794 / Flat 2101) / skip 5683件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,105.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$231.66** / 初期 $100.00 (+131.66%)
- 確定: 3082件 (Win 848 / Loss 726 / Flat 1508) / skip 5005件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0261 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $231.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.97** / 初期 $100.00 (+23.97%)
- 確定: 2954件 (Win 878 / Loss 1163 / Flat 913) / pending 2件 / skip 3195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000139 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.97

## 6. Latest Market Context

- 更新: 2026-09-16T11:41:24.070647+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=76001.2
- Funnel: target 1058 → liquid 152 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.1 >= 65=1, 4h RSI 65.0 >= 65=1, 4h RSI 82.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +126.47% | $18,798,100.52 |
| BR/USDT:USDT | +94.35% | $22,288,572.75 |
| LSK/USDT:USDT | +61.29% | $25,258,051.92 |
| BULLA/USDT:USDT | +45.62% | $1,440,139.69 |
| USELESS/USDT:USDT | +16.21% | $7,649,246.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +3.69% | +3.60% |
| IOST/USDT:USDT | below_1h_threshold | +3.26% | +3.17% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.83% | +2.74% |
| VVV/USDT:USDT | below_1h_threshold | +2.67% | +2.58% |
| SPX/USDT:USDT | below_1h_threshold | +2.30% | +2.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
