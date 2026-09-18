# Decision Report

- generated_at: 2026-09-18T02:41:20.795019+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14856**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=14856, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.43% | **+0.85%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.24% | **+1.68%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.89% | **+1.42%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.31% | **+1.38%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.63% | **+0.82%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.33% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5604件 (Win 1679 / Loss 1814 / Flat 2111) / skip 5813件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$244.71** / 初期 $100.00 (+144.71%)
- 確定: 3145件 (Win 876 / Loss 750 / Flat 1519) / skip 5122件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1278 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $244.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2959件 (Win 878 / Loss 1165 / Flat 916) / pending 1件 / skip 3366件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000391 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-18T02:41:11.736031+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=76928.0
- Funnel: target 1052 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +42.26% | $3,331,012.26 |
| COTI/USDT:USDT | +17.95% | $6,769,925.22 |
| ARB/USDT:USDT | +16.75% | $76,400,130.83 |
| ONE/USDT:USDT | +15.39% | $49,149,313.64 |
| NEAR/USDT:USDT | +14.26% | $119,913,018.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +3.82% | +3.53% |
| ADA/USDT:USDT | below_1h_threshold | +3.53% | +3.24% |
| WLD/USDT:USDT | below_1h_threshold | +2.58% | +2.29% |
| CROSS/USDT:USDT | below_1h_threshold | +2.45% | +2.16% |
| HEI/USDT:USDT | below_1h_threshold | +2.22% | +1.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
