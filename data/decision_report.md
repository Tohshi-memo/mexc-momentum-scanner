# Decision Report

- generated_at: 2026-05-26T17:09:14.008850+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4906**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.58% / filled 20/20。**
- 全期間 MARKET基準: n=4906, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| ASK | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.09% | **+0.76%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.41% | **+0.39%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.52% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.22** / 初期 $100.00 (+29.22%)
- 確定: 677件 (Win 171 / Loss 215 / Flat 291) / skip 790件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $129.22

## 4. Latest Market Context

- 更新: 2026-05-26T17:09:11.870169+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=76497.6
- Funnel: target 769 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +13.30% | $6,307,927.97 |
| ESPORTS/USDT:USDT | +10.83% | $6,743,746.72 |
| BILL/USDT:USDT | +4.75% | $13,871,352.08 |
| DYDX/USDT:USDT | +3.14% | $1,701,932.00 |
| MYX/USDT:USDT | +2.77% | $1,014,057.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +4.86% | +4.91% |
| IO/USDT:USDT | below_1h_threshold | +1.50% | +1.55% |
| USELESS/USDT:USDT | below_1h_threshold | +1.12% | +1.17% |
| DYDX/USDT:USDT | below_1h_threshold | +1.11% | +1.15% |
| LIT/USDT:USDT | below_1h_threshold | +1.03% | +1.08% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
