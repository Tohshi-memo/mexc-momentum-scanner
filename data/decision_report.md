# Decision Report

- generated_at: 2026-07-12T13:31:11.338269+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8593**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=8593, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +3.16% | **+3.01%** |
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.85% | **+0.51%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.14% | **+0.10%** |
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | +0.10% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$101.51** / 初期 $100.00 (+1.51%)
- 確定トレード: 88件 (TP 30 / SL 57 / EXP 1)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.42** / 初期 $100.00 (+221.42%)
- 確定: 2781件 (Win 875 / Loss 921 / Flat 985) / skip 2373件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $321.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1360件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.17** / 初期 $100.00 (-0.83%)
- 確定: 26件 (Win 9 / Loss 17 / Flat 0) / pending 0件 / skip 40件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000252 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: T/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.17

## 6. Latest Market Context

- 更新: 2026-07-12T13:31:05.188553+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64017.7
- Funnel: target 863 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SXT/USDT:USDT | +23.05% | $23,250,728.83 |
| DEXE/USDT:USDT | +19.93% | $9,232,653.78 |
| VANRY/USDT:USDT | +18.26% | $3,511,009.19 |
| BILL/USDT:USDT | +17.82% | $3,997,768.30 |
| T/USDT:USDT | +16.89% | $23,828,323.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VANRY/USDT:USDT | below_1h_threshold | +3.03% | +3.00% |
| B/USDT:USDT | below_1h_threshold | +2.94% | +2.91% |
| US/USDT:USDT | below_1h_threshold | +2.88% | +2.85% |
| CASHCAT/USDT:USDT | below_1h_threshold | +2.75% | +2.72% |
| FHE/USDT:USDT | below_1h_threshold | +1.67% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
