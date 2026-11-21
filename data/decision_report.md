# Decision Report

- generated_at: 2026-11-21T07:21:23.685457+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19284**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.28% / filled 20/20。**
- 全期間 MARKET基準: n=19284, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +2.36% | **+1.89%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.58% | **+1.34%** |
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.68% | **+0.67%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.69% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.52% | **+0.34%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.13% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,669.22** / 初期 $100.00 (+1569.22%)
- 確定: 7427件 (Win 2135 / Loss 2396 / Flat 2896) / skip 8418件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $1,669.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$441.55** / 初期 $100.00 (+341.55%)
- 確定: 5090件 (Win 1355 / Loss 1088 / Flat 2647) / skip 7605件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $441.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7443件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T07:21:09.237514+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=58264.3
- Funnel: target 1086 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +33.23% | $26,160,051.28 |
| PIEVERSE/USDT:USDT | +15.81% | $4,106,946.34 |
| BTW/USDT:USDT | +14.74% | $4,134,422.20 |
| UVXY/USDT:USDT | +9.84% | $6,202,119.25 |
| RARE/USDT:USDT | +9.61% | $5,674,895.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.12% | +2.72% |
| AKE/USDT:USDT | below_1h_threshold | +2.89% | +2.50% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.59% | +1.20% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +1.58% | +1.19% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.32% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
