# Decision Report

- generated_at: 2026-07-31T03:31:25.017992+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9955**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9955, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.87% | **-0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.38% | **+0.48%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.33% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.14% | **+1.82%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.00% | **+1.65%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.66% | **+1.46%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.61% | **+1.17%** |
| MARKET_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$546.19** / 初期 $100.00 (+446.19%)
- 確定: 3546件 (Win 1130 / Loss 1153 / Flat 1263) / skip 2970件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $546.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.70** / 初期 $100.00 (+40.70%)
- 確定: 1252件 (Win 350 / Loss 284 / Flat 618) / skip 2114件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2041 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $140.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 0件 / skip 626件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000686 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T03:31:16.444566+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=64370.4
- Funnel: target 920 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +32.00% | $9,978,463.75 |
| AXTISTOCK/USDT:USDT | +30.55% | $3,889,385.88 |
| KOMA/USDT:USDT | +26.67% | $7,486,977.88 |
| GRVT/USDT:USDT | +23.84% | $1,475,085.55 |
| SNXX/USDT:USDT | +17.00% | $11,835,032.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_1h_threshold | +4.10% | +3.95% |
| MMT/USDT:USDT | below_1h_threshold | +2.04% | +1.88% |
| RCATSTOCK/USDT:USDT | below_1h_threshold | +1.90% | +1.75% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.60% | +1.44% |
| AMZNSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
