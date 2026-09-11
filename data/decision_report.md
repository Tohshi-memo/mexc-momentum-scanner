# Decision Report

- generated_at: 2026-09-11T10:16:21.682651+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14207**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=14207, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.47% | **+0.52%** |
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.32% | **-0.18%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.47% | **-0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.94% | **+0.75%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.36% | **+0.25%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.21% | **+0.18%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.11% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,074.76** / 初期 $100.00 (+974.76%)
- 確定: 5372件 (Win 1618 / Loss 1736 / Flat 2018) / skip 5396件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,074.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.52** / 初期 $100.00 (+108.52%)
- 確定: 2801件 (Win 770 / Loss 650 / Flat 1381) / skip 4817件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0084 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.40** / 初期 $100.00 (+23.40%)
- 確定: 2710件 (Win 801 / Loss 1036 / Flat 873) / pending 5件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $123.40

## 6. Latest Market Context

- 更新: 2026-09-11T10:16:12.210342+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77080.0
- Funnel: target 1068 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +65.22% | $16,132,180.13 |
| LSK/USDT:USDT | +25.32% | $2,106,908.74 |
| RAY/USDT:USDT | +22.60% | $18,840,462.74 |
| LAB/USDT:USDT | +21.03% | $1,151,772.31 |
| CNPY/USDT:USDT | +16.03% | $2,699,131.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.00% | +3.89% |
| CNPY/USDT:USDT | below_1h_threshold | +2.18% | +2.08% |
| THETA/USDT:USDT | below_1h_threshold | +1.17% | +1.07% |
| LSK/USDT:USDT | below_1h_threshold | +0.86% | +0.75% |
| RAY/USDT:USDT | below_1h_threshold | +0.70% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
