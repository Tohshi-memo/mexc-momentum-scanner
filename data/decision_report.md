# Decision Report

- generated_at: 2026-07-30T04:16:26.606056+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9857**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.37% / filled 20/20。**
- 全期間 MARKET基準: n=9857, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.37% | **+2.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.37% | **+2.37%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.74% | **+2.33%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.47% | **+1.73%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.52% | **+0.91%** |
| LIMIT_BB3S | 5/17 | 29.4% | +2.75% | **+0.81%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.00% | **-0.00%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.76% | **-0.19%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.57% | **-0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 170件 (TP 67 / SL 98 / EXP 5)
- 最新: LASERTECSTOCK/USDT:USDT TP_HIT PnL +3.98% 残高後 $121.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2899件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2026件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.33** / 初期 $100.00 (+10.33%)
- 確定: 771件 (Win 250 / Loss 298 / Flat 223) / pending 2件 / skip 562件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000740 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $110.33

## 6. Latest Market Context

- 更新: 2026-07-30T04:16:18.018398+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64098.5
- Funnel: target 911 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +16.62% | $1,017,185.81 |
| UAI/USDT:USDT | +15.89% | $16,379,878.86 |
| RE/USDT:USDT | +13.64% | $8,550,183.34 |
| MSFU/USDT:USDT | +13.33% | $3,889,668.14 |
| US/USDT:USDT | +13.10% | $1,132,458.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOLO/USDT:USDT | below_1h_threshold | +2.64% | +2.70% |
| QXOSTOCK/USDT:USDT | below_1h_threshold | +1.96% | +2.02% |
| ACH/USDT:USDT | below_1h_threshold | +1.55% | +1.60% |
| US/USDT:USDT | below_1h_threshold | +0.73% | +0.79% |
| ZIL/USDT:USDT | below_1h_threshold | +0.59% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
