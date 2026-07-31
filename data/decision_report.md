# Decision Report

- generated_at: 2026-07-31T03:16:26.698581+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9954**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9954, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.42% | **-1.42%** |

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
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.62% | **+2.23%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.70% | **+1.85%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.33% | **+1.66%** |
| MARKET_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.43% | **+1.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$548.94** / 初期 $100.00 (+448.94%)
- 確定: 3545件 (Win 1130 / Loss 1152 / Flat 1263) / skip 2970件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MMT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $548.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.19** / 初期 $100.00 (+41.19%)
- 確定: 1251件 (Win 350 / Loss 283 / Flat 618) / skip 2114件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2197 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $141.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.57** / 初期 $100.00 (+10.57%)
- 確定: 805件 (Win 262 / Loss 320 / Flat 223) / pending 0件 / skip 626件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000686 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET` EXPIRED account -0.04% 残高後 $110.57

## 6. Latest Market Context

- 更新: 2026-07-31T03:16:18.218111+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=64208.6
- Funnel: target 920 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +29.36% | $9,727,304.68 |
| AXTISTOCK/USDT:USDT | +29.11% | $3,857,142.75 |
| KOMA/USDT:USDT | +23.34% | $7,403,750.18 |
| GRVT/USDT:USDT | +19.26% | $1,436,949.31 |
| AMZU/USDT:USDT | +16.72% | $1,817,875.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RCATSTOCK/USDT:USDT | below_1h_threshold | +1.90% | +2.00% |
| AMZNSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.55% |
| LAB/USDT:USDT | below_1h_threshold | +1.40% | +1.50% |
| GGLL/USDT:USDT | below_1h_threshold | +0.69% | +0.79% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.67% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
