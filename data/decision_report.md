# Decision Report

- generated_at: 2026-07-23T04:06:15.655828+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9352**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.49% / filled 20/20。**
- 全期間 MARKET基準: n=9352, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.86% | **+0.69%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_4PCT | 10/20 | 50.0% | +1.20% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.15% | **+0.06%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 136件 (TP 45 / SL 86 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -2.63% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$426.05** / 初期 $100.00 (+326.05%)
- 確定: 3320件 (Win 1048 / Loss 1075 / Flat 1197) / skip 2593件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $426.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1161件 (Win 312 / Loss 254 / Flat 595) / skip 1602件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0522 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.27** / 初期 $100.00 (+1.27%)
- 確定: 428件 (Win 143 / Loss 178 / Flat 107) / pending 0件 / skip 393件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000219 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CBRSSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.27

## 6. Latest Market Context

- 更新: 2026-07-23T04:06:07.650283+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=65627.6
- Funnel: target 892 → liquid 183 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +57.80% | $5,753,456.25 |
| RIF/USDT:USDT | +32.30% | $5,212,021.65 |
| BANK/USDT:USDT | +29.26% | $104,597,627.50 |
| ON/USDT:USDT | +20.11% | $2,994,380.89 |
| ERA/USDT:USDT | +18.07% | $5,805,659.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ERA/USDT:USDT | below_1h_threshold | +4.11% | +4.11% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.46% | +3.46% |
| RIF/USDT:USDT | below_1h_threshold | +1.87% | +1.87% |
| KORU/USDT:USDT | below_1h_threshold | +1.54% | +1.53% |
| DODO/USDT:USDT | below_1h_threshold | +1.41% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
