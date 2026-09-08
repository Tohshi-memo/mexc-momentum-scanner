# Decision Report

- generated_at: 2026-09-08T04:56:30.854382+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13954**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13954, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +1.59% | **+0.88%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.25% | **+0.20%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | -0.78% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +2.61% | **+2.24%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.45% | **+1.22%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.80% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,008.20** / 初期 $100.00 (+908.20%)
- 確定: 5227件 (Win 1575 / Loss 1696 / Flat 1956) / skip 5288件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,008.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4793件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1839 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.46** / 初期 $100.00 (+22.46%)
- 確定: 2544件 (Win 749 / Loss 953 / Flat 842) / pending 5件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000399 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.46

## 6. Latest Market Context

- 更新: 2026-09-08T04:56:15.920618+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=78668.1
- Funnel: target 1062 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.9 >= 65=1, 4h RSI 84.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +109.34% | $4,617,080.02 |
| IOST/USDT:USDT | +30.46% | $4,676,612.96 |
| MEMEROBINHOOD/USDT:USDT | +20.23% | $7,145,249.01 |
| CP/USDT:USDT | +18.49% | $2,857,961.36 |
| AERO/USDT:USDT | +16.99% | $5,031,006.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +2.70% | +2.97% |
| AVNT/USDT:USDT | below_1h_threshold | +2.56% | +2.83% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.91% |
| CAKE/USDT:USDT | below_1h_threshold | +1.61% | +1.88% |
| AKE/USDT:USDT | below_1h_threshold | +1.55% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
