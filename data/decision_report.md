# Decision Report

- generated_at: 2026-09-03T15:51:49.540362+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13495**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13495, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.60% | **-2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.55% | **+0.54%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.47% | **+0.09%** |
| LIMIT_7PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT | 2/20 | 10.0% | -4.00% | **-0.40%** |
| LIMIT_10PCT | 2/20 | 10.0% | -4.00% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +4.85% | **+2.42%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.32% | **+2.33%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +5.16% | **+2.32%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +5.90% | **+2.06%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5048件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2373件 (Win 671 / Loss 576 / Flat 1126) / skip 4533件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1655 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.00** / 初期 $100.00 (+17.00%)
- 確定: 2179件 (Win 651 / Loss 852 / Flat 676) / pending 6件 / skip 2791件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000472 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.00

## 6. Latest Market Context

- 更新: 2026-09-03T15:51:34.799948+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=80847.0
- Funnel: target 1046 → liquid 165 → pre 50 → checked 50 → surge 7 → strict 1
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1, 4h RSI 90.6 >= 65=1, 4h RSI 79.3 >= 65=1, 4h RSI 68.7 >= 65=1, 4h RSI 74.7 >= 65=1, 4h RSI 74.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +111.45% | $9,331,519.64 |
| BULLA/USDT:USDT | +80.32% | $9,911,926.71 |
| EDGE/USDT:USDT | +66.04% | $9,085,992.74 |
| BASECAT/USDT:USDT | +53.34% | $1,161,345.71 |
| USELESS/USDT:USDT | +52.92% | $29,462,740.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +4.95% | +4.53% |
| ZEN/USDT:USDT | below_1h_threshold | +4.60% | +4.17% |
| HEMI/USDT:USDT | below_1h_threshold | +4.49% | +4.07% |
| SPX/USDT:USDT | below_1h_threshold | +3.51% | +3.09% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.46% | +3.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
