# Decision Report

- generated_at: 2026-09-12T00:21:08.269283+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14265**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=14265, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.74% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.26% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.57% | **+1.07%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.67% | **+0.50%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,102.31** / 初期 $100.00 (+1002.31%)
- 確定: 5420件 (Win 1635 / Loss 1756 / Flat 2029) / skip 5406件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STONK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,102.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2833件 (Win 780 / Loss 656 / Flat 1397) / skip 4843件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1233 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.42** / 初期 $100.00 (+24.42%)
- 確定: 2756件 (Win 817 / Loss 1057 / Flat 882) / pending 2件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000354 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STONK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $124.42

## 6. Latest Market Context

- 更新: 2026-09-12T00:21:00.189229+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=77262.8
- Funnel: target 1067 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +37.36% | $16,028,920.18 |
| LAB/USDT:USDT | +25.50% | $12,402,962.81 |
| LSK/USDT:USDT | +17.91% | $3,381,198.93 |
| CYS/USDT:USDT | +17.30% | $1,507,764.78 |
| BEAT/USDT:USDT | +15.47% | $11,900,416.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +1.80% | +1.70% |
| CNPY/USDT:USDT | below_1h_threshold | +1.70% | +1.61% |
| MINA/USDT:USDT | below_1h_threshold | +1.44% | +1.34% |
| HNT/USDT:USDT | below_1h_threshold | +1.16% | +1.06% |
| 4/USDT:USDT | below_1h_threshold | +1.06% | +0.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
