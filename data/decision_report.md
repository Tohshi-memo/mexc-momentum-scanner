# Decision Report

- generated_at: 2026-06-30T10:03:51.506286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7878**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=7878, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.99% | **+1.99%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.69% | **+0.55%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.68% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.19% | **+0.78%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.46% | **+0.41%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.42% | **+0.28%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.14% | **+0.03%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.05% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$259.13** / 初期 $100.00 (+159.13%)
- 確定: 2354件 (Win 714 / Loss 785 / Flat 855) / skip 2085件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $259.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 832件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T10:03:46.798010+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=59360.0
- Funnel: target 813 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +39.66% | $6,229,301.07 |
| AIGENSYN/USDT:USDT | +36.15% | $10,708,928.44 |
| SYN/USDT:USDT | +34.17% | $30,680,196.70 |
| M/USDT:USDT | +23.44% | $3,587,162.32 |
| AVAVSTOCK/USDT:USDT | +19.66% | $1,633,599.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.67% | +1.65% |
| H/USDT:USDT | below_1h_threshold | +0.90% | +0.88% |
| M/USDT:USDT | below_1h_threshold | +0.71% | +0.69% |
| EVAA/USDT:USDT | below_1h_threshold | +0.60% | +0.58% |
| BTW/USDT:USDT | below_1h_threshold | +0.55% | +0.53% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
