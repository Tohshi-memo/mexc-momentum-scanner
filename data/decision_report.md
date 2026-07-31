# Decision Report

- generated_at: 2026-07-31T02:51:22.526190+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9952**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9952, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.09% | **-1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.28% | **+0.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_2PCT | 16/20 | 80.0% | -0.23% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.83% | **+1.56%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.81% | **+1.55%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.47% | **+1.23%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +2.48% | **+0.99%** |
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$540.09** / 初期 $100.00 (+440.09%)
- 確定: 3543件 (Win 1128 / Loss 1152 / Flat 1263) / skip 2970件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $540.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.63** / 初期 $100.00 (+39.63%)
- 確定: 1249件 (Win 348 / Loss 283 / Flat 618) / skip 2114件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $139.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 0件 / skip 625件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000634 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T02:51:14.649182+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=64284.6
- Funnel: target 920 → liquid 171 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AXTISTOCK/USDT:USDT | +28.80% | $3,805,053.59 |
| MMT/USDT:USDT | +28.05% | $9,573,224.34 |
| KOMA/USDT:USDT | +22.64% | $7,172,201.19 |
| GRVT/USDT:USDT | +19.92% | $1,407,609.14 |
| AMZU/USDT:USDT | +16.93% | $1,956,686.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MMT/USDT:USDT | below_1h_threshold | +4.64% | +5.02% |
| CAP/USDT:USDT | below_1h_threshold | +2.78% | +3.17% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.60% | +2.99% |
| AKE/USDT:USDT | below_1h_threshold | +2.34% | +2.73% |
| QXOSTOCK/USDT:USDT | below_1h_threshold | +1.30% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
