# Decision Report

- generated_at: 2026-09-04T20:46:33.758884+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13665**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13665, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/16 | 18.8% | +2.28% | **+0.43%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.99% | **+2.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.19% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5215件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2422件 (Win 682 / Loss 577 / Flat 1163) / skip 4654件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0596 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.38** / 初期 $100.00 (+18.38%)
- 確定: 2302件 (Win 685 / Loss 882 / Flat 735) / pending 6件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000275 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $118.38

## 6. Latest Market Context

- 更新: 2026-09-04T20:46:21.841261+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=79669.9
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.0 >= 65=1, 4h RSI 81.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +51.96% | $6,160,591.18 |
| BASECAT/USDT:USDT | +28.75% | $1,924,231.33 |
| USELESS/USDT:USDT | +10.06% | $44,345,318.90 |
| NEAR/USDT:USDT | +9.32% | $22,118,083.01 |
| UAI/USDT:USDT | +8.61% | $7,494,503.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +3.45% | +3.56% |
| TUT/USDT:USDT | below_1h_threshold | +3.20% | +3.31% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.74% | +2.85% |
| KORU/USDT:USDT | below_1h_threshold | +2.57% | +2.68% |
| MUU/USDT:USDT | below_1h_threshold | +2.02% | +2.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
