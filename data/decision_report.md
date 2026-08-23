# Decision Report

- generated_at: 2026-08-23T17:56:34.594876+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12464**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12464, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.54% | **-1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.18% | **-0.10%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.23% | **-0.18%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.28% | **-0.18%** |
| LIMIT_BB3S | 6/14 | 42.9% | -1.12% | **-0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +5.60% | **+4.48%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.05% | **+1.68%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.58% | **+1.61%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.19% | **+1.59%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.54% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$707.63** / 初期 $100.00 (+607.63%)
- 確定: 4491件 (Win 1371 / Loss 1470 / Flat 1650) / skip 4534件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $707.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.63** / 初期 $100.00 (+56.63%)
- 確定: 1943件 (Win 534 / Loss 468 / Flat 941) / skip 3932件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $156.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1865件 (Win 550 / Loss 707 / Flat 608) / pending 0件 / skip 2077件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000074 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `MARKET` EXPIRED account +0.24% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-23T17:56:25.023770+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=77172.2
- Funnel: target 1018 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.3 >= 65=1, 4h RSI 80.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +11.58% | $3,171,515.66 |
| BTW/USDT:USDT | +8.11% | $17,925,246.00 |
| STRK/USDT:USDT | +7.10% | $1,535,863.60 |
| SPK/USDT:USDT | +6.23% | $1,977,270.56 |
| ZORA/USDT:USDT | +4.47% | $1,572,907.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +2.82% | +3.10% |
| AR/USDT:USDT | below_1h_threshold | +2.70% | +2.98% |
| EGLD/USDT:USDT | below_1h_threshold | +2.17% | +2.45% |
| FF/USDT:USDT | below_1h_threshold | +2.17% | +2.45% |
| CHIP/USDT:USDT | below_1h_threshold | +1.61% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
