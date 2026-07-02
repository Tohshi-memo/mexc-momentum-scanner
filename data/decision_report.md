# Decision Report

- generated_at: 2026-07-02T22:41:41.494332+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8114**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=8114, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.88% | **+0.88%** |
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.77% | **+0.44%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.13% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.93% | **+0.46%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.65% | **+0.42%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.19% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2231件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.02** / 初期 $100.00 (+6.02%)
- 確定: 572件 (Win 139 / Loss 134 / Flat 299) / skip 953件
- 成長率目線: 平均log +0.000102 / 幾何平均 +0.010% per trade / maxDD +3.55%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0725 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: THE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.02

## 5. Latest Market Context

- 更新: 2026-07-02T22:41:35.319370+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=61509.6
- Funnel: target 834 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +39.57% | $1,502,105.69 |
| PIPPIN/USDT:USDT | +16.16% | $4,842,326.91 |
| MAGMA/USDT:USDT | +15.99% | $4,842,885.81 |
| LAB/USDT:USDT | +14.14% | $13,095,936.17 |
| GUA/USDT:USDT | +10.36% | $8,923,274.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZRO/USDT:USDT | below_1h_threshold | +2.32% | +2.41% |
| SYN/USDT:USDT | below_1h_threshold | +2.02% | +2.12% |
| ZBT/USDT:USDT | below_1h_threshold | +1.55% | +1.65% |
| O/USDT:USDT | below_1h_threshold | +1.39% | +1.49% |
| AERO/USDT:USDT | below_1h_threshold | +1.15% | +1.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
