# Decision Report

- generated_at: 2026-08-08T10:16:26.878859+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10831**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=10831, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.35% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.50% | **+6.50%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +3.56% | **+1.60%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.97% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$631.17** / 初期 $100.00 (+531.17%)
- 確定: 3832件 (Win 1212 / Loss 1252 / Flat 1368) / skip 3560件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.28% 残高後 $631.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2732件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1468 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.63** / 初期 $100.00 (+18.63%)
- 確定: 1200件 (Win 385 / Loss 468 / Flat 347) / pending 5件 / skip 1099件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000368 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.04% 残高後 $118.63

## 6. Latest Market Context

- 更新: 2026-08-08T10:16:18.055158+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64973.1
- Funnel: target 961 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1, 4h RSI 90.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +274.88% | $9,186,388.32 |
| BLUAI/USDT:USDT | +53.84% | $2,499,924.49 |
| TUT/USDT:USDT | +44.52% | $4,215,195.15 |
| CYS/USDT:USDT | +41.70% | $20,464,629.62 |
| MMT/USDT:USDT | +34.86% | $5,475,879.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.13% | +3.11% |
| SLX/USDT:USDT | below_1h_threshold | +3.09% | +3.07% |
| HEI/USDT:USDT | below_1h_threshold | +2.52% | +2.50% |
| KAS/USDT:USDT | below_1h_threshold | +1.19% | +1.17% |
| MMT/USDT:USDT | below_1h_threshold | +1.18% | +1.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
