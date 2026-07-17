# Decision Report

- generated_at: 2026-07-17T15:21:22.628477+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8861**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8861, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.50% | **+0.88%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.46% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$351.99** / 初期 $100.00 (+251.99%)
- 確定: 2976件 (Win 927 / Loss 949 / Flat 1100) / skip 2446件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $351.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.07** / 初期 $100.00 (+10.07%)
- 確定: 823件 (Win 196 / Loss 171 / Flat 456) / skip 1449件
- 成長率目線: 平均log +0.000117 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0695 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $110.07

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.15** / 初期 $100.00 (-0.85%)
- 確定: 127件 (Win 41 / Loss 73 / Flat 13) / pending 4件 / skip 201件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000282 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.15

## 6. Latest Market Context

- 更新: 2026-07-17T15:21:12.713088+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=62923.7
- Funnel: target 885 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LRC/USDT:USDT | +52.93% | $5,072,674.55 |
| AKE/USDT:USDT | +25.70% | $39,673,283.65 |
| XEC/USDT:USDT | +23.71% | $2,383,613.69 |
| KAITO/USDT:USDT | +18.67% | $5,706,754.69 |
| BULLA/USDT:USDT | +18.28% | $1,285,337.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +3.78% | +4.13% |
| LRC/USDT:USDT | below_1h_threshold | +3.16% | +3.52% |
| DRAM/USDT:USDT | below_1h_threshold | +2.51% | +2.86% |
| O/USDT:USDT | below_1h_threshold | +2.16% | +2.51% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.08% | +2.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
