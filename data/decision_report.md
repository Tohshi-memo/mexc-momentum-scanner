# Decision Report

- generated_at: 2026-07-31T05:21:28.547736+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9963**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9963, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.79% | **-1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +3.83% | **+0.77%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.61% | **+0.72%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.06% | **+0.62%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.57% | **+0.54%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.15% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.59% | **+2.20%** |
| MARKET_LONG | 20/20 | 100.0% | +2.13% | **+2.13%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.91% | **+0.95%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.43% | **+0.86%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.21% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$546.81** / 初期 $100.00 (+446.81%)
- 確定: 3554件 (Win 1133 / Loss 1158 / Flat 1263) / skip 2970件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $546.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.26** / 初期 $100.00 (+41.26%)
- 確定: 1259件 (Win 353 / Loss 288 / Flat 618) / skip 2115件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1745 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $141.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 0件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000530 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T05:21:23.542014+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=64396.6
- Funnel: target 920 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +45.64% | $9,051,831.46 |
| AXTISTOCK/USDT:USDT | +32.59% | $4,163,231.51 |
| MMT/USDT:USDT | +31.50% | $11,058,444.58 |
| SNXX/USDT:USDT | +21.90% | $12,302,322.21 |
| BULLA/USDT:USDT | +19.52% | $1,109,970.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +4.56% | +4.38% |
| SNXX/USDT:USDT | below_1h_threshold | +3.65% | +3.47% |
| MVLL/USDT:USDT | below_1h_threshold | +2.89% | +2.71% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.64% | +2.46% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
