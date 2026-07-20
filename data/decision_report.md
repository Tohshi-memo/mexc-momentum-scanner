# Decision Report

- generated_at: 2026-07-20T05:56:22.275254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9084**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.00% / filled 20/20。**
- 全期間 MARKET基準: n=9084, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.34% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.02% | **+0.76%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.51% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.51% | **+0.38%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.20% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.37** / 初期 $100.00 (+299.37%)
- 確定: 3146件 (Win 986 / Loss 1001 / Flat 1159) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.14% 残高後 $399.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.83** / 初期 $100.00 (+25.83%)
- 確定: 1045件 (Win 267 / Loss 218 / Flat 560) / skip 1450件
- 成長率目線: 平均log +0.000220 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0796 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.83

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.98** / 初期 $100.00 (+0.98%)
- 確定: 283件 (Win 96 / Loss 131 / Flat 56) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000179 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.04% 残高後 $100.98

## 6. Latest Market Context

- 更新: 2026-07-20T05:56:13.345564+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.65% price=64089.6
- Funnel: target 886 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +57.86% | $99,751,668.91 |
| ACE/USDT:USDT | +41.23% | $4,674,037.55 |
| PUMPFUN/USDT:USDT | +16.52% | $19,043,723.32 |
| VELVET/USDT:USDT | +13.73% | $6,007,598.77 |
| PROM/USDT:USDT | +11.69% | $2,438,028.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +3.15% | +3.80% |
| VELVET/USDT:USDT | below_1h_threshold | +2.47% | +3.13% |
| ACE/USDT:USDT | below_1h_threshold | +1.58% | +2.23% |
| XPL/USDT:USDT | below_1h_threshold | +1.15% | +1.81% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.00% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
