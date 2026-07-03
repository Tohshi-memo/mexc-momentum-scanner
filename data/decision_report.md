# Decision Report

- generated_at: 2026-07-03T00:45:35.973891+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8120**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=8120, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.19% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.45% | **+0.95%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.39% | **+0.48%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.48% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2445件 (Win 754 / Loss 816 / Flat 875) / skip 2236件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.46** / 初期 $100.00 (+5.46%)
- 確定: 577件 (Win 140 / Loss 137 / Flat 300) / skip 954件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.55%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BREV/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.35% 残高後 $105.46

## 5. Latest Market Context

- 更新: 2026-07-03T00:45:25.380603+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=61320.2
- Funnel: target 834 → liquid 173 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +34.51% | $1,869,830.28 |
| GUA/USDT:USDT | +26.75% | $9,478,285.46 |
| PIPPIN/USDT:USDT | +15.61% | $6,287,395.76 |
| MAGMA/USDT:USDT | +15.00% | $5,159,603.72 |
| RPL/USDT:USDT | +13.46% | $1,389,069.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| THE/USDT:USDT | below_1h_threshold | +4.94% | +5.30% |
| BTW/USDT:USDT | below_1h_threshold | +2.82% | +3.18% |
| NOM/USDT:USDT | below_1h_threshold | +2.42% | +2.78% |
| CHZ/USDT:USDT | below_1h_threshold | +2.34% | +2.70% |
| MYX/USDT:USDT | below_1h_threshold | +1.87% | +2.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
