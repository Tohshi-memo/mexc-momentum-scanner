# Decision Report

- generated_at: 2026-11-27T18:41:25.024984+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19800**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19800, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 3/16 | 18.8% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.90% | **-0.36%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.18% | **-0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.89% | **+1.04%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.45% | **+0.86%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.87% | **+0.79%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.23% | **+0.67%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.13% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,928.72** / 初期 $100.00 (+1828.72%)
- 確定: 7645件 (Win 2199 / Loss 2461 / Flat 2985) / skip 8716件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,928.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5297件 (Win 1410 / Loss 1141 / Flat 2746) / skip 7914件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0276 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000153 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-27T18:41:08.948940+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=59829.8
- Funnel: target 1101 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +37.39% | $9,555,651.51 |
| VELVET/USDT:USDT | +12.69% | $4,029,571.60 |
| PIEVERSE/USDT:USDT | +10.93% | $6,695,581.91 |
| SSV/USDT:USDT | +6.83% | $2,065,236.27 |
| BTW/USDT:USDT | +6.60% | $7,246,877.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.90% | +5.06% |
| LISTA/USDT:USDT | below_1h_threshold | +4.75% | +4.92% |
| SOXL/USDT:USDT | below_1h_threshold | +4.17% | +4.33% |
| BTW/USDT:USDT | below_1h_threshold | +3.50% | +3.66% |
| SSV/USDT:USDT | below_1h_threshold | +3.30% | +3.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
