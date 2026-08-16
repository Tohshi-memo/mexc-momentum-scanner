# Decision Report

- generated_at: 2026-08-16T18:11:17.438800+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11757**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=11757, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.95% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.33% | **+0.47%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.62% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +4.16% | **+2.38%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.50% | **+0.90%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.02% | **+0.41%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.94% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4135件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.89** / 初期 $100.00 (+54.89%)
- 確定: 1784件 (Win 495 / Loss 417 / Flat 872) / skip 3384件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0012 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CROSS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.26** / 初期 $100.00 (+19.26%)
- 確定: 1654件 (Win 500 / Loss 626 / Flat 528) / pending 3件 / skip 1572件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000079 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.26

## 6. Latest Market Context

- 更新: 2026-08-16T18:11:09.027720+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63136.6
- Funnel: target 986 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +12.28% | $7,277,324.64 |
| APR/USDT:USDT | +9.88% | $4,698,231.22 |
| CYS/USDT:USDT | +5.82% | $48,383,774.85 |
| RIVER/USDT:USDT | +5.43% | $1,997,716.05 |
| BEAT/USDT:USDT | +4.07% | $43,152,087.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +3.99% | +3.98% |
| BEAT/USDT:USDT | below_1h_threshold | +3.79% | +3.78% |
| CYS/USDT:USDT | below_1h_threshold | +2.85% | +2.84% |
| VELVET/USDT:USDT | below_1h_threshold | +1.44% | +1.44% |
| TUT/USDT:USDT | below_1h_threshold | +0.96% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
