# Decision Report

- generated_at: 2026-09-09T01:52:05.279440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14027**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=14027, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.54% | **+1.38%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.86% | **+1.30%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.55% | **+1.24%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.04% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.70% | **-0.17%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.56% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,013.58** / 初期 $100.00 (+913.58%)
- 確定: 5291件 (Win 1588 / Loss 1707 / Flat 1996) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,013.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.66** / 初期 $100.00 (+90.66%)
- 確定: 2630件 (Win 726 / Loss 622 / Flat 1282) / skip 4808件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0470 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XAN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $190.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.07** / 初期 $100.00 (+19.07%)
- 確定: 2609件 (Win 763 / Loss 992 / Flat 854) / pending 2件 / skip 2887件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000120 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XAN/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $119.07

## 6. Latest Market Context

- 更新: 2026-09-09T01:51:55.601663+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=78844.9
- Funnel: target 1070 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OL/USDT:USDT | +32.01% | $1,928,745.80 |
| WAVES/USDT:USDT | +19.81% | $1,349,878.50 |
| ARX/USDT:USDT | +10.23% | $1,397,126.44 |
| EGLD/USDT:USDT | +8.10% | $2,372,518.77 |
| SOFTBANKSTOCK/USDT:USDT | +7.04% | $7,857,593.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BNCSTOCK/USDT:USDT | below_1h_threshold | +3.97% | +3.85% |
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +3.54% | +3.41% |
| KORU/USDT:USDT | below_1h_threshold | +3.05% | +2.92% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.75% | +2.63% |
| ETC/USDT:USDT | below_1h_threshold | +2.42% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
