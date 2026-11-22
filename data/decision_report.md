# Decision Report

- generated_at: 2026-11-22T06:11:16.541660+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19361**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19361, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.07% | **-0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/17 | 58.8% | +2.66% | **+1.56%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.01% | **+0.81%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.67%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.29% | **+1.37%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.88% | **+1.23%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.70% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,778.01** / 初期 $100.00 (+1678.01%)
- 確定: 7481件 (Win 2149 / Loss 2408 / Flat 2924) / skip 8441件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ENSO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,778.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$449.72** / 初期 $100.00 (+349.72%)
- 確定: 5126件 (Win 1364 / Loss 1101 / Flat 2661) / skip 7646件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0285 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $449.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7519件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000349 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T06:11:05.587126+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=59121.9
- Funnel: target 1086 → liquid 112 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +31.07% | $2,196,259.28 |
| DCTY/USDT:USDT | +23.04% | $1,685,291.89 |
| BLESS/USDT:USDT | +21.83% | $58,539,943.98 |
| PIEVERSE/USDT:USDT | +18.94% | $6,093,461.76 |
| SKYAI/USDT:USDT | +14.36% | $1,611,030.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.00% | +2.62% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.01% | +1.63% |
| DCTY/USDT:USDT | below_1h_threshold | +1.92% | +1.54% |
| ASTER/USDT:USDT | below_1h_threshold | +0.76% | +0.38% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.51% | +0.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
