# Decision Report

- generated_at: 2026-07-03T00:17:01.155962+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8117**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.41% / filled 20/20。**
- 全期間 MARKET基準: n=8117, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.46% | **+1.46%** |
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.16% | **+0.35%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.74% | **+0.35%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.35% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.67% | **+1.08%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.65% | **+0.55%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.21% | **+0.20%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.02% | **+0.01%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.15% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2234件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.83** / 初期 $100.00 (+5.83%)
- 確定: 575件 (Win 140 / Loss 136 / Flat 299) / skip 953件
- 成長率目線: 平均log +0.000099 / 幾何平均 +0.010% per trade / maxDD +3.55%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0495 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.83

## 5. Latest Market Context

- 更新: 2026-07-03T00:16:55.289583+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=61382.2
- Funnel: target 834 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +31.17% | $1,804,474.99 |
| RPL/USDT:USDT | +21.60% | $1,219,181.90 |
| MAGMA/USDT:USDT | +19.55% | $5,081,022.81 |
| PIPPIN/USDT:USDT | +17.26% | $5,988,628.05 |
| BASED/USDT:USDT | +11.94% | $14,188,289.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BREV/USDT:USDT | below_1h_threshold | +3.42% | +3.68% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.53% | +2.79% |
| BASED/USDT:USDT | below_1h_threshold | +2.37% | +2.62% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +1.90% | +2.16% |
| THE/USDT:USDT | below_1h_threshold | +1.86% | +2.12% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
