# Decision Report

- generated_at: 2026-09-12T16:26:21.092601+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14315**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.85% / filled 20/20。**
- 全期間 MARKET基準: n=14315, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.75% | **+1.31%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.02% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.10% | **+0.82%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.73% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.42% | **+1.28%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.29% | **+1.03%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.38% | **+0.36%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.07% | **+0.01%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.08% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5428件 (Win 1635 / Loss 1760 / Flat 2033) / skip 5448件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2834件 (Win 780 / Loss 656 / Flat 1398) / skip 4892件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0259 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.33** / 初期 $100.00 (+23.33%)
- 確定: 2767件 (Win 818 / Loss 1064 / Flat 885) / pending 0件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000346 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.33

## 6. Latest Market Context

- 更新: 2026-09-12T16:26:10.777479+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77349.5
- Funnel: target 1068 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +3.69% | $2,971,356.21 |
| BEAT/USDT:USDT | +2.33% | $18,748,415.31 |
| RIVER/USDT:USDT | +2.04% | $9,863,439.71 |
| BTW/USDT:USDT | +1.48% | $2,362,728.30 |
| UAI/USDT:USDT | +1.42% | $16,596,197.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.91% | +3.91% |
| BEAT/USDT:USDT | below_1h_threshold | +2.11% | +2.11% |
| RIVER/USDT:USDT | below_1h_threshold | +1.97% | +1.96% |
| BTW/USDT:USDT | below_1h_threshold | +1.48% | +1.47% |
| UAI/USDT:USDT | below_1h_threshold | +1.35% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
