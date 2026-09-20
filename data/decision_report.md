# Decision Report

- generated_at: 2026-09-20T01:21:23.450249+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15119**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.31% / filled 20/20。**
- 全期間 MARKET基準: n=15119, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.69% | **+1.10%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.71% | **+1.09%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.73% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.67% | **+0.57%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.30% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,211.67** / 初期 $100.00 (+1111.67%)
- 確定: 5648件 (Win 1695 / Loss 1829 / Flat 2124) / skip 6032件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AVAX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,211.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$246.78** / 初期 $100.00 (+146.78%)
- 確定: 3232件 (Win 897 / Loss 762 / Flat 1573) / skip 5298件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0356 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AVAX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $246.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.58** / 初期 $100.00 (+21.58%)
- 確定: 2977件 (Win 880 / Loss 1178 / Flat 919) / pending 1件 / skip 3614件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.58

## 6. Latest Market Context

- 更新: 2026-09-20T01:21:12.686041+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=81163.1
- Funnel: target 1050 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +66.65% | $1,894,687.34 |
| OFC/USDT:USDT | +50.15% | $1,946,976.67 |
| ONE/USDT:USDT | +23.78% | $47,614,673.50 |
| EVAA/USDT:USDT | +19.00% | $1,372,606.32 |
| ZIL/USDT:USDT | +14.56% | $1,710,878.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CELR/USDT:USDT | below_1h_threshold | +4.53% | +4.66% |
| G/USDT:USDT | below_1h_threshold | +3.90% | +4.03% |
| HBAR/USDT:USDT | below_1h_threshold | +1.73% | +1.85% |
| EVAA/USDT:USDT | below_1h_threshold | +1.60% | +1.73% |
| TAG/USDT:USDT | below_1h_threshold | +1.44% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
