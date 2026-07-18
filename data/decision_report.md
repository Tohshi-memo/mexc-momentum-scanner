# Decision Report

- generated_at: 2026-07-18T21:46:23.720982+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8979**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8979, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.17% | **-2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.25% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.70% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.09% | **+2.78%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.19% | **+2.08%** |
| MARKET_LONG | 20/20 | 100.0% | +1.95% | **+1.95%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.08% | **+1.39%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +3.20% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2491件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$118.36** / 初期 $100.00 (+18.36%)
- 確定: 940件 (Win 233 / Loss 191 / Flat 516) / skip 1450件
- 成長率目線: 平均log +0.000179 / 幾何平均 +0.018% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1863 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $118.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定: 196件 (Win 62 / Loss 107 / Flat 27) / pending 0件 / skip 253件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000562 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `MARKET` EXPIRED account +0.16% 残高後 $99.04

## 6. Latest Market Context

- 更新: 2026-07-18T21:46:14.492530+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=64593.6
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +52.18% | $26,625,895.88 |
| BANK/USDT:USDT | +41.23% | $18,552,654.09 |
| B/USDT:USDT | +12.93% | $30,366,601.50 |
| AKE/USDT:USDT | +12.64% | $86,532,803.77 |
| ANSEM/USDT:USDT | +8.65% | $1,846,961.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.22% | +4.33% |
| FWDISTOCK/USDT:USDT | below_1h_threshold | +3.74% | +3.85% |
| LAB/USDT:USDT | below_1h_threshold | +3.45% | +3.56% |
| TLM/USDT:USDT | below_1h_threshold | +3.37% | +3.48% |
| ZBT/USDT:USDT | below_1h_threshold | +2.78% | +2.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
