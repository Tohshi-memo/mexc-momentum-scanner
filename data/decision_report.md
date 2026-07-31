# Decision Report

- generated_at: 2026-07-31T04:26:27.197441+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9959**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9959, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.13% | **-2.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.36% | **+1.06%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.27% | **+2.78%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.27% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +2.11% | **+2.11%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.40% | **+2.04%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +3.97% | **+1.59%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$557.88** / 初期 $100.00 (+457.88%)
- 確定: 3550件 (Win 1133 / Loss 1154 / Flat 1263) / skip 2970件
- 成長率目線: 平均log +0.000484 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $557.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.75** / 初期 $100.00 (+42.75%)
- 確定: 1256件 (Win 353 / Loss 285 / Flat 618) / skip 2114件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2306 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $142.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 0件 / skip 631件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000674 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T04:26:18.532069+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=64242.9
- Funnel: target 920 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +54.51% | $8,139,681.24 |
| MMT/USDT:USDT | +33.63% | $10,467,321.74 |
| AXTISTOCK/USDT:USDT | +31.55% | $3,994,118.78 |
| RLC/USDT:USDT | +20.78% | $1,172,974.63 |
| SNXX/USDT:USDT | +17.00% | $12,113,571.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +3.48% | +3.64% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.08% | +2.23% |
| ROBO/USDT:USDT | below_1h_threshold | +2.06% | +2.22% |
| UNI/USDT:USDT | below_1h_threshold | +2.05% | +2.21% |
| CAP/USDT:USDT | below_1h_threshold | +1.93% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
