# Decision Report

- generated_at: 2026-07-17T14:56:09.258071+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8858**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8858, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.60% | **+1.26%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.65% | **+1.06%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.31% | **+2.32%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.64% | **+1.32%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$354.11** / 初期 $100.00 (+254.11%)
- 確定: 2973件 (Win 927 / Loss 947 / Flat 1099) / skip 2446件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $354.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$109.90** / 初期 $100.00 (+9.90%)
- 確定: 820件 (Win 195 / Loss 171 / Flat 454) / skip 1449件
- 成長率目線: 平均log +0.000115 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0695 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $109.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定: 124件 (Win 41 / Loss 72 / Flat 11) / pending 4件 / skip 201件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000306 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.32

## 6. Latest Market Context

- 更新: 2026-07-17T14:56:02.789815+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63161.9
- Funnel: target 885 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LRC/USDT:USDT | +46.70% | $4,884,727.17 |
| XEC/USDT:USDT | +31.88% | $2,295,681.97 |
| AKE/USDT:USDT | +29.84% | $40,051,960.62 |
| BANK/USDT:USDT | +22.44% | $16,063,538.18 |
| KAITO/USDT:USDT | +20.73% | $5,638,511.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.66% | +3.61% |
| US/USDT:USDT | below_1h_threshold | +2.83% | +2.78% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.78% | +2.73% |
| TAG/USDT:USDT | below_1h_threshold | +2.75% | +2.70% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +2.14% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
