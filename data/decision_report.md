# Decision Report

- generated_at: 2026-07-12T11:41:10.820280+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8588**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=8588, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.34% | **+0.31%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +2.11% | **+2.11%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.80% | **+0.56%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.45% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$102.02** / 初期 $100.00 (+2.02%)
- 確定トレード: 87件 (TP 30 / SL 56 / EXP 1)
- 最新: VANRY/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.03** / 初期 $100.00 (+221.03%)
- 確定: 2776件 (Win 874 / Loss 921 / Flat 981) / skip 2373件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $321.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1355件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0338 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.17** / 初期 $100.00 (-0.83%)
- 確定: 26件 (Win 9 / Loss 17 / Flat 0) / pending 0件 / skip 37件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000179 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: T/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.17

## 6. Latest Market Context

- 更新: 2026-07-12T11:41:04.555075+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=63961.3
- Funnel: target 863 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SXT/USDT:USDT | +20.56% | $20,600,847.19 |
| T/USDT:USDT | +20.50% | $22,511,937.05 |
| BILL/USDT:USDT | +16.86% | $3,003,781.02 |
| VANRY/USDT:USDT | +16.13% | $3,294,394.13 |
| DEXE/USDT:USDT | +15.74% | $7,530,582.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +4.21% | +4.02% |
| PARTI/USDT:USDT | below_1h_threshold | +3.38% | +3.19% |
| BILL/USDT:USDT | below_1h_threshold | +2.82% | +2.63% |
| TLM/USDT:USDT | below_1h_threshold | +2.00% | +1.81% |
| FHE/USDT:USDT | below_1h_threshold | +1.88% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
