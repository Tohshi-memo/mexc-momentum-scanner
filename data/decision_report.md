# Decision Report

- generated_at: 2026-09-29T18:41:35.035970+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15784**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.99% / filled 20/20。**
- 全期間 MARKET基準: n=15784, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/16 | 56.2% | +2.20% | **+1.24%** |
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.13% | **+0.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.42% | **+0.37%** |
| MARKET_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5986件 (Win 1766 / Loss 1925 / Flat 2295) / skip 6359件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3535件 (Win 974 / Loss 812 / Flat 1749) / skip 5660件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3947件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000154 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-29T18:41:20.887107+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.65% price=83578.4
- Funnel: target 1073 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 68.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +15.95% | $1,217,100.73 |
| QNT/USDT:USDT | +7.49% | $326,172,020.72 |
| NIL/USDT:USDT | +4.94% | $2,697,310.85 |
| SOONNETWORK/USDT:USDT | +4.62% | $2,744,986.41 |
| NMR/USDT:USDT | +4.13% | $15,297,089.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_relative_strength | +5.29% | +4.65% |
| NIL/USDT:USDT | below_1h_threshold | +4.16% | +3.52% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.95% | +3.31% |
| USELESS/USDT:USDT | below_1h_threshold | +3.41% | +2.77% |
| PENGU/USDT:USDT | below_1h_threshold | +3.00% | +2.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
