# Decision Report

- generated_at: 2026-10-16T19:16:17.222671+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16824**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=16824, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.55% | **+1.55%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_BB3S | 7/14 | 50.0% | +0.76% | **+0.38%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.89% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.46% | **+0.20%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.39% | **+0.20%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.26% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 242件 (TP 90 / SL 145 / EXP 7)
- 最新: BTW/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,254.65** / 初期 $100.00 (+1154.65%)
- 確定: 6316件 (Win 1849 / Loss 2027 / Flat 2440) / skip 7069件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,254.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3688件 (Win 1027 / Loss 878 / Flat 1783) / skip 6547件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0730 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4982件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000416 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-16T19:16:05.761242+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=81360.0
- Funnel: target 1084 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UVXY/USDT:USDT | +12.14% | $2,306,903.36 |
| AGT/USDT:USDT | +5.77% | $10,286,704.43 |
| LONGXIA/USDT:USDT | +4.07% | $1,371,511.49 |
| AKE/USDT:USDT | +3.68% | $11,965,176.52 |
| SOXS/USDT:USDT | +3.44% | $4,662,149.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_1h_threshold | +1.88% | +1.58% |
| UVXY/USDT:USDT | below_1h_threshold | +1.87% | +1.57% |
| LIT/USDT:USDT | below_1h_threshold | +1.70% | +1.39% |
| SOXS/USDT:USDT | below_1h_threshold | +1.59% | +1.29% |
| SYN/USDT:USDT | below_1h_threshold | +1.35% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
