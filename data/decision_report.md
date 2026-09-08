# Decision Report

- generated_at: 2026-09-08T04:16:16.073703+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13950**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13950, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_BB3S | 6/13 | 46.2% | +0.38% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +2.61% | **+2.24%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.03% | **+1.62%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.94% | **+0.52%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,003.23** / 初期 $100.00 (+903.23%)
- 確定: 5223件 (Win 1574 / Loss 1695 / Flat 1954) / skip 5288件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,003.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4789件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1644 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.25** / 初期 $100.00 (+22.25%)
- 確定: 2540件 (Win 748 / Loss 952 / Flat 840) / pending 3件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000426 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.25

## 6. Latest Market Context

- 更新: 2026-09-08T04:16:09.072581+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=78789.6
- Funnel: target 1062 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +80.29% | $3,663,076.99 |
| MEMEROBINHOOD/USDT:USDT | +40.83% | $6,991,578.69 |
| IOST/USDT:USDT | +21.96% | $4,408,921.11 |
| CP/USDT:USDT | +21.65% | $2,741,981.84 |
| AERO/USDT:USDT | +19.20% | $4,837,873.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOPH/USDT:USDT | below_1h_threshold | +3.60% | +3.72% |
| IOST/USDT:USDT | below_1h_threshold | +1.85% | +1.96% |
| HNT/USDT:USDT | below_1h_threshold | +1.73% | +1.85% |
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +1.72% | +1.84% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
