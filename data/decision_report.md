# Decision Report

- generated_at: 2026-09-08T04:01:22.883426+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13948**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13948, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +2.30% | **+2.30%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.96% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$996.94** / 初期 $100.00 (+896.94%)
- 確定: 5221件 (Win 1573 / Loss 1695 / Flat 1953) / skip 5288件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $996.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2572件 (Win 717 / Loss 618 / Flat 1237) / skip 4787件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1598 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.25** / 初期 $100.00 (+22.25%)
- 確定: 2538件 (Win 748 / Loss 952 / Flat 838) / pending 5件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000351 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.25

## 6. Latest Market Context

- 更新: 2026-09-08T04:01:10.897209+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78895.1
- Funnel: target 1062 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +75.80% | $3,403,521.25 |
| MEMEROBINHOOD/USDT:USDT | +38.92% | $6,968,126.22 |
| CP/USDT:USDT | +23.10% | $2,662,124.60 |
| IOST/USDT:USDT | +20.99% | $4,349,084.97 |
| AERO/USDT:USDT | +20.21% | $4,783,605.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.62% |
| KORU/USDT:USDT | below_1h_threshold | +1.46% | +1.44% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.35% |
| DRAM/USDT:USDT | below_1h_threshold | +0.96% | +0.94% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.92% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
