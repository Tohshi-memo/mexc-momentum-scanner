# Decision Report

- generated_at: 2026-08-15T00:46:30.764186+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11620**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11620, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.45% | **+1.10%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.37% | **+0.35%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.95% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.90% | **+0.63%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.48% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$644.83** / 初期 $100.00 (+544.83%)
- 確定: 4088件 (Win 1282 / Loss 1345 / Flat 1461) / skip 4093件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $644.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$153.05** / 初期 $100.00 (+53.05%)
- 確定: 1683件 (Win 482 / Loss 407 / Flat 794) / skip 3348件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0896 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $153.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.73** / 初期 $100.00 (+17.73%)
- 確定: 1568件 (Win 477 / Loss 600 / Flat 491) / pending 2件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.73

## 6. Latest Market Context

- 更新: 2026-08-15T00:46:15.603663+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=62999.8
- Funnel: target 985 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +29.65% | $1,328,954.07 |
| US/USDT:USDT | +17.69% | $6,788,434.70 |
| ROBO/USDT:USDT | +13.87% | $1,006,808.99 |
| NIL/USDT:USDT | +11.24% | $1,295,273.56 |
| VELVET/USDT:USDT | +9.16% | $43,881,273.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVNT/USDT:USDT | below_1h_threshold | +4.12% | +4.15% |
| ON/USDT:USDT | below_1h_threshold | +3.83% | +3.86% |
| EDEN/USDT:USDT | below_1h_threshold | +3.71% | +3.74% |
| NIL/USDT:USDT | below_1h_threshold | +3.63% | +3.65% |
| MYX/USDT:USDT | below_1h_threshold | +2.67% | +2.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
