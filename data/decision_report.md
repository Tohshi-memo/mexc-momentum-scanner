# Decision Report

- generated_at: 2026-08-23T16:56:39.000054+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12462**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12462, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.08% | **+0.04%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.80% | **+3.60%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.96% | **+1.08%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.34% | **+1.05%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.99% | **+0.99%** |
| MARKET_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$700.62** / 初期 $100.00 (+600.62%)
- 確定: 4489件 (Win 1370 / Loss 1470 / Flat 1649) / skip 4534件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $700.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.86** / 初期 $100.00 (+56.86%)
- 確定: 1941件 (Win 534 / Loss 467 / Flat 940) / skip 3932件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $156.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1865件 (Win 550 / Loss 707 / Flat 608) / pending 0件 / skip 2074件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000074 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `MARKET` EXPIRED account +0.24% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-23T16:56:25.643505+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=77386.8
- Funnel: target 1018 → liquid 170 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.5 >= 65=1, 4h RSI 75.4 >= 65=1, 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +12.08% | $3,054,164.33 |
| BTW/USDT:USDT | +9.01% | $16,844,210.04 |
| ZORA/USDT:USDT | +5.68% | $1,214,177.23 |
| STX/USDT:USDT | +5.24% | $14,279,361.81 |
| USELESS/USDT:USDT | +4.15% | $2,409,560.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +4.09% | +3.75% |
| PENGU/USDT:USDT | below_1h_threshold | +3.77% | +3.43% |
| RIVER/USDT:USDT | below_1h_threshold | +2.65% | +2.31% |
| LIT/USDT:USDT | below_1h_threshold | +2.64% | +2.30% |
| CYS/USDT:USDT | below_1h_threshold | +2.60% | +2.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
