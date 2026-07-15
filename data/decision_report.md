# Decision Report

- generated_at: 2026-07-15T23:11:17.640845+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8773**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.48% / filled 20/20。**
- 全期間 MARKET基準: n=8773, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.48% | **+2.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.48% | **+2.48%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.46% | **+2.34%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.73% | **+1.38%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.93% | **+1.16%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.33% | **+0.20%** |
| LIMIT_BB3S_LONG | 10/10 | 100.0% | +0.13% | **+0.13%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.36% | **-0.09%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.58% | **-0.15%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -2.62% | **-0.66%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 99件 (TP 34 / SL 63 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$339.45** / 初期 $100.00 (+239.45%)
- 確定: 2891件 (Win 904 / Loss 942 / Flat 1045) / skip 2443件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $339.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.85** / 初期 $100.00 (+6.85%)
- 確定: 737件 (Win 169 / Loss 168 / Flat 400) / skip 1447件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1134 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HOME/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $106.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 181件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000318 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-15T23:11:10.224170+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=64899.9
- Funnel: target 871 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +25.54% | $1,455,414.18 |
| ROAM/USDT:USDT | +22.52% | $5,491,312.73 |
| CAP/USDT:USDT | +14.72% | $1,556,325.96 |
| ONDO/USDT:USDT | +10.20% | $36,515,954.77 |
| SKL/USDT:USDT | +10.13% | $1,810,784.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +2.02% | +1.91% |
| CAP/USDT:USDT | below_1h_threshold | +0.99% | +0.88% |
| EDGE/USDT:USDT | below_1h_threshold | +0.86% | +0.75% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.76% | +0.65% |
| JASMY/USDT:USDT | below_1h_threshold | +0.53% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
