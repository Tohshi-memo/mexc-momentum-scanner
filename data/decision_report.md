# Decision Report

- generated_at: 2026-10-01T10:06:20.653353+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15887**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15887, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.70% | **-0.18%** |
| LIMIT_BB3S | 2/14 | 14.3% | -3.23% | **-0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.40% | **+2.38%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.48% | **+2.11%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.10% | **+2.07%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.03% | **+1.21%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.33% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,281.30** / 初期 $100.00 (+1181.30%)
- 確定: 6006件 (Win 1777 / Loss 1931 / Flat 2298) / skip 6442件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,281.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$266.48** / 初期 $100.00 (+166.48%)
- 確定: 3540件 (Win 977 / Loss 812 / Flat 1751) / skip 5758件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1447 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $266.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4047件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000289 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T10:06:07.630690+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=83452.1
- Funnel: target 1097 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +62.97% | $16,769,243.95 |
| NOM/USDT:USDT | +25.00% | $2,377,438.14 |
| CT/USDT:USDT | +18.99% | $5,172,003.08 |
| NIGHT/USDT:USDT | +17.96% | $8,155,823.11 |
| JASMY/USDT:USDT | +15.75% | $8,317,344.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CT/USDT:USDT | below_1h_threshold | +1.85% | +2.20% |
| MOVR/USDT:USDT | below_1h_threshold | +1.11% | +1.46% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +0.61% | +0.96% |
| KODSTOCK/USDT:USDT | below_1h_threshold | +0.59% | +0.94% |
| KORU/USDT:USDT | below_1h_threshold | +0.44% | +0.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
