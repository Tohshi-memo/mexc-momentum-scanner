# Decision Report

- generated_at: 2026-09-13T11:06:15.174835+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14419**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=14419, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.54% | **+0.51%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.92% | **+1.31%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.67% | **+0.83%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.99% | **+0.79%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.05% | **+0.74%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.37% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5549件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$225.59** / 初期 $100.00 (+125.59%)
- 確定: 2937件 (Win 817 / Loss 699 / Flat 1421) / skip 4893件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0956 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $225.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.83** / 初期 $100.00 (+26.83%)
- 確定: 2853件 (Win 849 / Loss 1103 / Flat 901) / pending 3件 / skip 3039件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000299 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.83

## 6. Latest Market Context

- 更新: 2026-09-13T11:06:07.007499+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=76663.1
- Funnel: target 1068 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +284.26% | $95,575,610.96 |
| STEEM/USDT:USDT | +62.37% | $1,849,538.03 |
| ARK/USDT:USDT | +43.16% | $1,468,443.98 |
| VTHO/USDT:USDT | +39.25% | $3,221,592.32 |
| POWR/USDT:USDT | +29.69% | $2,709,627.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +1.30% | +1.28% |
| SOXS/USDT:USDT | below_1h_threshold | +1.00% | +0.98% |
| ZCAT/USDT:USDT | below_1h_threshold | +0.92% | +0.89% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.69% | +0.66% |
| BTW/USDT:USDT | below_1h_threshold | +0.68% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
