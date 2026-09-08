# Decision Report

- generated_at: 2026-09-08T06:21:21.731180+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13964**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13964, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.96% | **-0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.65% | **+1.06%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_BB3S | 12/14 | 85.7% | -0.34% | **-0.30%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -1.59% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.75% | **+1.46%** |
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.20% | **+1.21%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.32% | **+0.92%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,013.72** / 初期 $100.00 (+913.72%)
- 確定: 5237件 (Win 1579 / Loss 1700 / Flat 1958) / skip 5288件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,013.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4803件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1387 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.76** / 初期 $100.00 (+22.76%)
- 確定: 2554件 (Win 752 / Loss 957 / Flat 845) / pending 2件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000367 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.76

## 6. Latest Market Context

- 更新: 2026-09-08T06:21:09.764115+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=78433.1
- Funnel: target 1065 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +102.16% | $8,153,930.82 |
| IOST/USDT:USDT | +20.61% | $4,991,750.63 |
| MEMEROBINHOOD/USDT:USDT | +20.00% | $7,285,157.21 |
| AKE/USDT:USDT | +13.82% | $13,010,072.65 |
| USELESS/USDT:USDT | +13.28% | $11,873,035.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HNT/USDT:USDT | below_1h_threshold | +3.53% | +3.69% |
| BONER/USDT:USDT | below_1h_threshold | +3.46% | +3.61% |
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +2.99% | +3.14% |
| AKE/USDT:USDT | below_1h_threshold | +2.89% | +3.04% |
| SOXS/USDT:USDT | below_1h_threshold | +2.29% | +2.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
