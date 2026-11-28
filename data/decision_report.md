# Decision Report

- generated_at: 2026-11-28T07:01:21.646384+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19825**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=19825, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.98% | **+1.19%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.82% | **+1.00%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.93% | **+0.87%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.14% | **+0.75%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.19% | **+0.96%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.87% | **+0.74%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.60% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定トレード: 293件 (TP 107 / SL 176 / EXP 10)
- 最新: EVAA/USDT:USDT TP_HIT PnL +8.00% 残高後 $122.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,957.80** / 初期 $100.00 (+1857.80%)
- 確定: 7652件 (Win 2202 / Loss 2463 / Flat 2987) / skip 8734件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,957.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5298件 (Win 1410 / Loss 1141 / Flat 2747) / skip 7938件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0523 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7985件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000131 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-28T07:01:06.541997+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=59742.4
- Funnel: target 1101 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +30.71% | $24,125,069.37 |
| BTW/USDT:USDT | +25.40% | $12,067,109.06 |
| CFG/USDT:USDT | +9.45% | $1,607,654.30 |
| SKY/USDT:USDT | +8.50% | $4,065,878.63 |
| VELVET/USDT:USDT | +5.42% | $5,952,323.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +0.84% | +0.81% |
| EVAA/USDT:USDT | below_1h_threshold | +0.61% | +0.58% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.53% | +0.50% |
| MUU/USDT:USDT | below_1h_threshold | +0.38% | +0.34% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +0.37% | +0.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
