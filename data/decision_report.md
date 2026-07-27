# Decision Report

- generated_at: 2026-07-27T00:11:15.444180+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9587**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=9587, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.67% | **+1.58%** |
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.47% | **+1.10%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.27% | **+0.19%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$105.34** / 初期 $100.00 (+5.34%)
- 確定トレード: 142件 (TP 48 / SL 89 / EXP 5)
- 最新: ZAMA/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.34
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$452.56** / 初期 $100.00 (+352.56%)
- 確定: 3399件 (Win 1078 / Loss 1106 / Flat 1215) / skip 2749件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $452.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.72** / 初期 $100.00 (+37.72%)
- 確定: 1222件 (Win 338 / Loss 274 / Flat 610) / skip 1776件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0547 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.21** / 初期 $100.00 (+8.21%)
- 確定: 616件 (Win 207 / Loss 238 / Flat 171) / pending 0件 / skip 440件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.11% 残高後 $108.21

## 6. Latest Market Context

- 更新: 2026-07-27T00:11:08.689012+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=65181.6
- Funnel: target 898 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESP/USDT:USDT | +18.88% | $5,546,966.64 |
| SAFE/USDT:USDT | +14.31% | $1,262,495.85 |
| 4/USDT:USDT | +11.50% | $2,206,396.54 |
| UB/USDT:USDT | +11.27% | $3,432,835.91 |
| AKE/USDT:USDT | +10.84% | $17,317,225.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESP/USDT:USDT | below_1h_threshold | +1.86% | +2.15% |
| AKE/USDT:USDT | below_1h_threshold | +1.64% | +1.94% |
| SOXL/USDT:USDT | below_1h_threshold | +1.51% | +1.80% |
| 4/USDT:USDT | below_1h_threshold | +1.17% | +1.47% |
| CROSS/USDT:USDT | below_1h_threshold | +0.99% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
