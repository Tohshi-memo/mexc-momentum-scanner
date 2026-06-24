# Decision Report

- generated_at: 2026-06-24T01:46:16.958529+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7454**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7454, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| ASK | 20/20 | 100.0% | -0.07% | **-0.07%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | -2.04% | **-0.20%** |
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.69% | **+1.53%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.34% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$102.45** / 初期 $100.00 (+2.45%)
- 確定トレード: 31件 (TP 12 / SL 19 / EXP 0)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$233.37** / 初期 $100.00 (+133.37%)
- 確定: 2085件 (Win 620 / Loss 691 / Flat 774) / skip 1930件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $233.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 328件 (Win 92 / Loss 88 / Flat 148) / skip 537件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-24T01:46:08.905159+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=62930.3
- Funnel: target 802 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +61.49% | $9,623,417.08 |
| BEAT/USDT:USDT | +22.63% | $64,280,555.21 |
| CLO/USDT:USDT | +18.55% | $5,481,388.58 |
| SYN/USDT:USDT | +13.82% | $15,394,822.57 |
| ALLO/USDT:USDT | +9.31% | $5,276,593.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ID/USDT:USDT | below_1h_threshold | +4.25% | +4.33% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.75% | +1.83% |
| ALLO/USDT:USDT | below_1h_threshold | +1.59% | +1.67% |
| OPN/USDT:USDT | below_1h_threshold | +1.57% | +1.66% |
| UP/USDT:USDT | below_1h_threshold | +1.29% | +1.38% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
