# Decision Report

- generated_at: 2026-10-07T08:16:27.168560+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16275**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.66% / filled 20/20。**
- 全期間 MARKET基準: n=16275, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.30% | **+0.97%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.52% | **+0.84%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.78% | **+0.67%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.95% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.62% | **+0.97%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.16% | **+0.75%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.03% | **+0.72%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.46% | **+0.34%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 232件 (TP 84 / SL 141 / EXP 7)
- 最新: BEAT/USDT:USDT TP_HIT PnL +3.87% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,322.43** / 初期 $100.00 (+1222.43%)
- 確定: 6276件 (Win 1845 / Loss 2011 / Flat 2420) / skip 6560件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,322.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6054件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4435件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000583 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-07T08:16:13.256550+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=84000.0
- Funnel: target 1074 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +13.93% | $9,707,285.07 |
| SAND/USDT:USDT | +9.92% | $17,294,542.74 |
| ORCA/USDT:USDT | +8.94% | $11,444,404.06 |
| STX/USDT:USDT | +6.82% | $4,093,498.58 |
| CT/USDT:USDT | +5.59% | $1,912,530.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +1.63% | +1.75% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.85% | +0.97% |
| NGAS/USDT:USDT | below_1h_threshold | +0.85% | +0.97% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.84% | +0.96% |
| SOXS/USDT:USDT | below_1h_threshold | +0.64% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
