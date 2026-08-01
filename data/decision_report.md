# Decision Report

- generated_at: 2026-08-01T04:01:29.417671+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10056**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=10056, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.45% | **+0.45%** |
| LIMIT_ATR | 7/20 | 35.0% | +1.20% | **+0.42%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.57% | **+0.34%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.41% | **+0.23%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.17% | **+0.15%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.01% | **-0.01%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$568.06** / 初期 $100.00 (+468.06%)
- 確定: 3608件 (Win 1151 / Loss 1180 / Flat 1277) / skip 3009件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $568.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2188件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0255 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.28** / 初期 $100.00 (+12.28%)
- 確定: 873件 (Win 283 / Loss 344 / Flat 246) / pending 6件 / skip 653件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000279 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $112.28

## 6. Latest Market Context

- 更新: 2026-08-01T04:01:21.008937+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=62973.7
- Funnel: target 921 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +36.62% | $1,216,596.65 |
| KOMA/USDT:USDT | +31.71% | $18,189,036.80 |
| BTW/USDT:USDT | +24.56% | $2,724,414.46 |
| LAB/USDT:USDT | +20.64% | $1,887,738.95 |
| TLM/USDT:USDT | +14.23% | $1,867,546.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +1.08% | +1.08% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +0.55% | +0.55% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.54% | +0.54% |
| KAITO/USDT:USDT | below_1h_threshold | +0.46% | +0.46% |
| BTW/USDT:USDT | below_1h_threshold | +0.45% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
