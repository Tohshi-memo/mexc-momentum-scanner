# Decision Report

- generated_at: 2026-08-23T21:26:34.529886+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12472**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12472, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.15% | **-2.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 8/14 | 57.1% | +0.60% | **+0.34%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +5.34% | **+4.45%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +4.58% | **+2.75%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.42% | **+2.05%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.60% | **+1.98%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +4.67% | **+1.87%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$718.25** / 初期 $100.00 (+618.25%)
- 確定: 4499件 (Win 1373 / Loss 1471 / Flat 1655) / skip 4534件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $718.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.26** / 初期 $100.00 (+57.26%)
- 確定: 1948件 (Win 536 / Loss 469 / Flat 943) / skip 3935件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0027 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $157.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.75** / 初期 $100.00 (+16.75%)
- 確定: 1868件 (Win 551 / Loss 708 / Flat 609) / pending 2件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000103 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.75

## 6. Latest Market Context

- 更新: 2026-08-23T21:26:24.705342+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.65% price=77881.1
- Funnel: target 1018 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +19.04% | $62,020,397.70 |
| BASECAT/USDT:USDT | +14.89% | $2,819,000.10 |
| PENGU/USDT:USDT | +13.40% | $19,648,286.96 |
| 1000RATS/USDT:USDT | +12.00% | $2,158,104.66 |
| BRETT/USDT:USDT | +10.82% | $1,405,598.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +4.52% | +3.87% |
| MORPHO/USDT:USDT | below_1h_threshold | +3.73% | +3.08% |
| PEPE/USDT:USDT | below_1h_threshold | +3.20% | +2.55% |
| AAVE/USDT:USDT | below_1h_threshold | +3.15% | +2.50% |
| FLOKI/USDT:USDT | below_1h_threshold | +3.12% | +2.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
