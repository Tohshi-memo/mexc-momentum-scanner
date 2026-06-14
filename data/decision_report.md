# Decision Report

- generated_at: 2026-06-14T18:00:38.402931+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6691**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=6691, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.43% | **+1.22%** |
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.00% | **-0.00%** |
| ASK_LONG | 20/20 | 100.0% | -0.19% | **-0.19%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.64% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.03** / 初期 $100.00 (+72.03%)
- 確定: 1564件 (Win 417 / Loss 497 / Flat 650) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $172.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.77** / 初期 $100.00 (-1.23%)
- 確定: 70件 (Win 19 / Loss 14 / Flat 37) / skip 32件
- 成長率目線: 平均log -0.000177 / 幾何平均 -0.018% per trade / maxDD +2.00%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0068 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $98.77

## 5. Latest Market Context

- 更新: 2026-06-14T18:00:31.802895+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63715.7
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +11.31% | $3,535,999.10 |
| CLO/USDT:USDT | +5.90% | $1,429,087.75 |
| BANANAS31/USDT:USDT | +5.52% | $2,103,049.66 |
| STG/USDT:USDT | +5.08% | $6,195,815.91 |
| BTW/USDT:USDT | +4.57% | $3,394,563.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_1h_threshold | +0.20% | +0.19% |
| MITO/USDT:USDT | below_1h_threshold | +0.19% | +0.18% |
| EDGE/USDT:USDT | below_1h_threshold | +0.18% | +0.17% |
| RAVE/USDT:USDT | below_1h_threshold | +0.17% | +0.15% |
| ATOM/USDT:USDT | below_1h_threshold | +0.15% | +0.14% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
