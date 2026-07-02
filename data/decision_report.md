# Decision Report

- generated_at: 2026-07-02T21:54:28.519993+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8111**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.41% / filled 20/20。**
- 全期間 MARKET基準: n=8111, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.48% | **+1.48%** |
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.74% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.77% | **+0.44%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.13% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.29% | **+1.14%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.58% | **+0.32%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.14% | **+0.11%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.02% | **+0.01%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.08% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2228件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.84** / 初期 $100.00 (+5.84%)
- 確定: 569件 (Win 138 / Loss 133 / Flat 298) / skip 953件
- 成長率目線: 平均log +0.000100 / 幾何平均 +0.010% per trade / maxDD +3.55%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0548 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $105.84

## 5. Latest Market Context

- 更新: 2026-07-02T21:54:18.654531+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=61552.3
- Funnel: target 834 → liquid 174 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +34.39% | $1,197,218.70 |
| MAGMA/USDT:USDT | +18.09% | $4,737,117.30 |
| PIPPIN/USDT:USDT | +14.95% | $4,213,107.49 |
| LAB/USDT:USDT | +14.16% | $12,741,198.17 |
| BASED/USDT:USDT | +12.15% | $14,906,481.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NES/USDT:USDT | below_1h_threshold | +3.94% | +3.95% |
| UB/USDT:USDT | below_1h_threshold | +2.86% | +2.86% |
| BEAT/USDT:USDT | below_1h_threshold | +2.78% | +2.78% |
| LUNC/USDT:USDT | below_1h_threshold | +2.53% | +2.53% |
| ALLO/USDT:USDT | below_1h_threshold | +2.25% | +2.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
