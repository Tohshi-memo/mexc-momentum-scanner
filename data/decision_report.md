# Decision Report

- generated_at: 2026-07-18T10:01:13.265125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8931**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.89% / filled 20/20。**
- 全期間 MARKET基準: n=8931, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_BB3S | 4/18 | 22.2% | +2.52% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.01% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.02% | **+0.36%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.29% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.73% | **+0.61%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.12% | **+0.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.11% | **+0.39%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.43% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$364.21** / 初期 $100.00 (+264.21%)
- 確定: 3046件 (Win 946 / Loss 970 / Flat 1130) / skip 2446件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $364.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.64** / 初期 $100.00 (+10.64%)
- 確定: 892件 (Win 211 / Loss 181 / Flat 500) / skip 1450件
- 成長率目線: 平均log +0.000113 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0393 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.13% 残高後 $110.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.94** / 初期 $100.00 (-0.06%)
- 確定: 186件 (Win 60 / Loss 99 / Flat 27) / pending 4件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000377 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.94

## 6. Latest Market Context

- 更新: 2026-07-18T10:01:06.871612+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63961.1
- Funnel: target 885 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +27.45% | $64,335,976.55 |
| TRADOOR/USDT:USDT | +26.51% | $4,065,596.58 |
| B/USDT:USDT | +20.32% | $1,961,442.35 |
| ESPORTS/USDT:USDT | +13.34% | $14,668,998.31 |
| ROAM/USDT:USDT | +12.93% | $1,017,990.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +1.23% | +1.23% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.96% | +0.96% |
| SOXS/USDT:USDT | below_1h_threshold | +0.70% | +0.70% |
| TRADOOR/USDT:USDT | below_1h_threshold | +0.66% | +0.66% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.42% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
