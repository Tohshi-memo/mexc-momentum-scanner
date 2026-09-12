# Decision Report

- generated_at: 2026-09-12T20:31:17.758907+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14322**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.85% / filled 20/20。**
- 全期間 MARKET基準: n=14322, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.25% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_BB3S | 4/20 | 20.0% | +3.54% | **+0.71%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.62% | **+0.56%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.69% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.37% | **+1.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.84% | **+0.80%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.89% | **+0.67%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.86% | **+0.34%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.44% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5454件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$211.25** / 初期 $100.00 (+111.25%)
- 確定: 2840件 (Win 782 / Loss 658 / Flat 1400) / skip 4893件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1338 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $211.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.74** / 初期 $100.00 (+23.74%)
- 確定: 2773件 (Win 820 / Loss 1066 / Flat 887) / pending 4件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000451 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.74

## 6. Latest Market Context

- 更新: 2026-09-12T20:31:05.509760+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77159.6
- Funnel: target 1068 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +22.94% | $24,920,512.45 |
| LONGXIA/USDT:USDT | +19.10% | $9,378,973.78 |
| RIVER/USDT:USDT | +13.79% | $14,344,644.68 |
| REZ/USDT:USDT | +11.08% | $1,520,855.71 |
| AKE/USDT:USDT | +7.59% | $3,383,197.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRIFFAIN/USDT:USDT | below_1h_threshold | +1.70% | +1.61% |
| VVV/USDT:USDT | below_1h_threshold | +1.24% | +1.14% |
| XMR/USDT:USDT | below_1h_threshold | +1.18% | +1.08% |
| ABNBSTOCK/USDT:USDT | below_1h_threshold | +0.97% | +0.88% |
| IOST/USDT:USDT | below_1h_threshold | +0.97% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
