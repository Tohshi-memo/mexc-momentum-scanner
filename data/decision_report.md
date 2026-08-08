# Decision Report

- generated_at: 2026-08-08T07:11:25.684409+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10820**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=10820, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_BB3S | 5/14 | 35.7% | +0.84% | **+0.30%** |
| LIMIT_6PCT | 9/20 | 45.0% | +0.63% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +7.04% | **+2.11%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +5.30% | **+1.85%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.41% | **+1.18%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$621.46** / 初期 $100.00 (+521.46%)
- 確定: 3821件 (Win 1209 / Loss 1252 / Flat 1360) / skip 3560件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_10PCT_LONG` TP_HIT account +1.00% 残高後 $621.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2721件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1273 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.43** / 初期 $100.00 (+18.43%)
- 確定: 1190件 (Win 382 / Loss 468 / Flat 340) / pending 4件 / skip 1098件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000333 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +0.34% 残高後 $118.43

## 6. Latest Market Context

- 更新: 2026-08-08T07:11:17.805901+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=64980.5
- Funnel: target 961 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +270.15% | $7,746,673.59 |
| BLESS/USDT:USDT | +36.72% | $90,434,414.57 |
| MMT/USDT:USDT | +36.20% | $3,357,726.26 |
| TUT/USDT:USDT | +31.06% | $2,884,672.43 |
| CYS/USDT:USDT | +23.36% | $16,678,125.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +3.12% | +3.12% |
| MMT/USDT:USDT | below_1h_threshold | +2.45% | +2.44% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.41% | +1.40% |
| ORDI/USDT:USDT | below_1h_threshold | +0.76% | +0.76% |
| CRV/USDT:USDT | below_1h_threshold | +0.63% | +0.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
