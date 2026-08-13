# Decision Report

- generated_at: 2026-08-13T17:16:27.733670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11461**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11461, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.03% | **-1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.01% | **+0.50%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.35% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.76% | **+1.88%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.42% | **+1.70%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.61% | **+1.62%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.31% | **+1.29%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.37% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.41** / 初期 $100.00 (+506.41%)
- 確定: 3979件 (Win 1240 / Loss 1303 / Flat 1436) / skip 4043件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $606.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$150.46** / 初期 $100.00 (+50.46%)
- 確定: 1649件 (Win 471 / Loss 396 / Flat 782) / skip 3223件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0371 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $150.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.69** / 初期 $100.00 (+16.69%)
- 確定: 1462件 (Win 431 / Loss 551 / Flat 480) / pending 6件 / skip 1470件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000234 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.69

## 6. Latest Market Context

- 更新: 2026-08-13T17:16:18.030712+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63097.6
- Funnel: target 978 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +8.40% | $9,692,169.86 |
| BEAT/USDT:USDT | +8.12% | $37,290,065.10 |
| ACU/USDT:USDT | +6.21% | $8,673,097.80 |
| US/USDT:USDT | +4.99% | $4,272,480.52 |
| AVNT/USDT:USDT | +4.89% | $3,831,926.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVNT/USDT:USDT | below_1h_threshold | +4.12% | +4.18% |
| TUT/USDT:USDT | below_1h_threshold | +3.86% | +3.92% |
| CAP/USDT:USDT | below_1h_threshold | +3.65% | +3.71% |
| US/USDT:USDT | below_1h_threshold | +2.58% | +2.64% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.36% | +2.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
