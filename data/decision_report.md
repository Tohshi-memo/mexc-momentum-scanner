# Decision Report

- generated_at: 2026-07-21T14:46:25.187667+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9184**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9184, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.80% | **-0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_BB3S | 6/16 | 37.5% | +2.08% | **+0.78%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.48% | **+0.31%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +3.34% | **+1.84%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.43% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$421.91** / 初期 $100.00 (+321.91%)
- 確定: 3246件 (Win 1021 / Loss 1037 / Flat 1188) / skip 2499件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRAM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $421.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.49** / 初期 $100.00 (+32.49%)
- 確定: 1145件 (Win 309 / Loss 245 / Flat 591) / skip 1450件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0749 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GRAM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.52% 残高後 $132.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 342件 (Win 120 / Loss 152 / Flat 70) / pending 2件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000203 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRAM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T14:46:16.433864+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=66885.9
- Funnel: target 885 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.5 >= 65=1, 4h RSI 84.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +107.82% | $1,346,032.95 |
| JIMOTHY/USDT:USDT | +84.43% | $5,046,693.76 |
| ERA/USDT:USDT | +64.41% | $12,309,237.54 |
| ESPORTS/USDT:USDT | +41.05% | $7,921,574.64 |
| ONE/USDT:USDT | +36.24% | $1,717,386.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.60% | +4.39% |
| SNXX/USDT:USDT | below_1h_threshold | +4.46% | +4.25% |
| ZRO/USDT:USDT | below_1h_threshold | +4.13% | +3.92% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.82% | +3.62% |
| POETSTOCK/USDT:USDT | below_1h_threshold | +3.47% | +3.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
