# Decision Report

- generated_at: 2026-07-26T07:56:22.834482+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9562**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9562, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.87% | **-0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.04% | **+0.76%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.36% | **+0.54%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.88% | **+0.51%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.38% | **+0.36%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.08% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.62% | **+2.62%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.41% | **+1.69%** |
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.61% | **+1.29%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.87% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$468.72** / 初期 $100.00 (+368.72%)
- 確定: 3390件 (Win 1078 / Loss 1099 / Flat 1213) / skip 2733件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $468.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.15** / 初期 $100.00 (+40.15%)
- 確定: 1215件 (Win 338 / Loss 269 / Flat 608) / skip 1758件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1503 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.62** / 初期 $100.00 (+9.62%)
- 確定: 605件 (Win 206 / Loss 230 / Flat 169) / pending 3件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000595 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $109.62

## 6. Latest Market Context

- 更新: 2026-07-26T07:56:13.838984+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=64339.3
- Funnel: target 898 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +65.49% | $37,494,772.64 |
| PIEVERSE/USDT:USDT | +51.52% | $3,062,537.88 |
| DIA/USDT:USDT | +36.55% | $2,115,571.28 |
| BANK/USDT:USDT | +18.72% | $94,985,535.13 |
| SHIB/USDT:USDT | +17.72% | $71,088,806.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +4.21% | +4.32% |
| BEAT/USDT:USDT | below_1h_threshold | +2.83% | +2.93% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.57% | +2.68% |
| ALLO/USDT:USDT | below_1h_threshold | +2.34% | +2.45% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.78% | +1.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
