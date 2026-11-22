# Decision Report

- generated_at: 2026-11-22T01:16:25.421770+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19350**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19350, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.33% | **-1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 15/20 | 75.0% | +1.60% | **+1.20%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.71% | **+1.08%** |
| LIMIT_5PCT | 9/20 | 45.0% | +2.20% | **+0.99%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.19% | **+1.88%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.18% | **+1.85%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.29% | **+1.60%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.14% | **+1.41%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,783.80** / 初期 $100.00 (+1683.80%)
- 確定: 7478件 (Win 2148 / Loss 2406 / Flat 2924) / skip 8433件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,783.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$448.22** / 初期 $100.00 (+348.22%)
- 確定: 5124件 (Win 1363 / Loss 1100 / Flat 2661) / skip 7637件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1272 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $448.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7512件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000404 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T01:16:15.105810+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=60165.4
- Funnel: target 1086 → liquid 118 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DCTY/USDT:USDT | +23.25% | $1,322,685.63 |
| CLAUDIA/USDT:USDT | +20.26% | $2,009,686.08 |
| PIEVERSE/USDT:USDT | +13.06% | $5,417,540.71 |
| ENSO/USDT:USDT | +13.05% | $1,104,470.61 |
| BTW/USDT:USDT | +12.14% | $5,565,321.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +1.16% | +1.18% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +1.00% | +1.02% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.68% | +0.70% |
| JUP/USDT:USDT | below_1h_threshold | +0.60% | +0.62% |
| DODO/USDT:USDT | below_1h_threshold | +0.56% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
