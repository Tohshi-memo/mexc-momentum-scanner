# Decision Report

- generated_at: 2026-10-09T06:26:21.342388+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16409**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=16409, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +1.07% | **+0.75%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.59% | **+0.56%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.06% | **-0.03%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.42% | **-0.04%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,315.82** / 初期 $100.00 (+1215.82%)
- 確定: 6282件 (Win 1845 / Loss 2012 / Flat 2425) / skip 6688件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,315.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3634件 (Win 1010 / Loss 853 / Flat 1771) / skip 6186件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4569件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-09T06:26:11.827418+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=82439.4
- Funnel: target 1084 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +74.34% | $3,960,393.26 |
| RLC/USDT:USDT | +70.71% | $25,704,173.74 |
| BATON/USDT:USDT | +58.02% | $6,132,526.05 |
| SI/USDT:USDT | +30.01% | $2,272,153.24 |
| LONGXIA/USDT:USDT | +16.95% | $4,143,761.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APT/USDT:USDT | below_1h_threshold | +2.37% | +2.24% |
| JCT/USDT:USDT | below_1h_threshold | +1.97% | +1.84% |
| KAS/USDT:USDT | below_1h_threshold | +1.78% | +1.65% |
| OGN/USDT:USDT | below_1h_threshold | +1.70% | +1.58% |
| PYTH/USDT:USDT | below_1h_threshold | +1.43% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
