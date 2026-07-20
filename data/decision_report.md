# Decision Report

- generated_at: 2026-07-20T04:26:09.845210+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9082**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=9082, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.10% | **+1.04%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.00% | **+0.85%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.02% | **+0.76%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.51% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.05% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$398.82** / 初期 $100.00 (+298.82%)
- 確定: 3144件 (Win 985 / Loss 1001 / Flat 1158) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $398.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.83** / 初期 $100.00 (+25.83%)
- 確定: 1043件 (Win 267 / Loss 218 / Flat 558) / skip 1450件
- 成長率目線: 平均log +0.000220 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0269 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $125.83

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.94** / 初期 $100.00 (+0.94%)
- 確定: 281件 (Win 95 / Loss 131 / Flat 55) / pending 3件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.94

## 6. Latest Market Context

- 更新: 2026-07-20T04:26:03.379425+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=64699.6
- Funnel: target 885 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +59.95% | $93,202,141.66 |
| ACE/USDT:USDT | +43.71% | $4,066,461.47 |
| PROM/USDT:USDT | +17.74% | $2,290,349.98 |
| PUMPFUN/USDT:USDT | +17.06% | $18,108,168.63 |
| DEXE/USDT:USDT | +9.00% | $1,569,704.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +2.90% | +3.11% |
| BANK/USDT:USDT | below_1h_threshold | +2.42% | +2.63% |
| VELVET/USDT:USDT | below_1h_threshold | +1.04% | +1.26% |
| PI/USDT:USDT | below_1h_threshold | +1.00% | +1.21% |
| SOXL/USDT:USDT | below_1h_threshold | +0.90% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
