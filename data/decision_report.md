# Decision Report

- generated_at: 2026-08-25T05:11:31.285125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12579**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.35% / filled 20/20。**
- 全期間 MARKET基準: n=12579, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.53% | **+0.54%** |
| LIMIT_BB3S | 6/14 | 42.9% | +1.11% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.97% | **+0.79%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.53% | **+0.76%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.63% | **+0.73%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$702.17** / 初期 $100.00 (+602.17%)
- 確定: 4559件 (Win 1388 / Loss 1494 / Flat 1677) / skip 4581件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $702.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4013件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0123 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.17** / 初期 $100.00 (+15.17%)
- 確定: 1914件 (Win 561 / Loss 729 / Flat 624) / pending 1件 / skip 2137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000195 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.17

## 6. Latest Market Context

- 更新: 2026-08-25T05:11:18.996469+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=80494.9
- Funnel: target 1026 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +76.18% | $4,185,515.70 |
| TAC/USDT:USDT | +45.48% | $3,539,932.02 |
| PROM/USDT:USDT | +22.99% | $18,608,502.93 |
| CASHCAT/USDT:USDT | +22.23% | $2,711,306.18 |
| PONS/USDT:USDT | +20.42% | $1,440,937.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STX/USDT:USDT | below_1h_threshold | +3.08% | +2.90% |
| KORU/USDT:USDT | below_1h_threshold | +2.35% | +2.17% |
| PYTH/USDT:USDT | below_1h_threshold | +1.98% | +1.80% |
| TAC/USDT:USDT | below_1h_threshold | +1.65% | +1.47% |
| MONAD/USDT:USDT | below_1h_threshold | +1.62% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
