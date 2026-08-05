# Decision Report

- generated_at: 2026-08-05T18:06:25.819732+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10439**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10439, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.33% | **+0.25%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_BB3S | 4/20 | 20.0% | -0.39% | **-0.08%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.32% | **-0.16%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.03% | **+2.12%** |
| MARKET_LONG | 20/20 | 100.0% | +2.01% | **+2.01%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.20% | **+1.98%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.81% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3230件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.28** / 初期 $100.00 (+41.28%)
- 確定: 1338件 (Win 377 / Loss 315 / Flat 646) / skip 2512件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0996 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.02% 残高後 $141.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.74** / 初期 $100.00 (+17.74%)
- 確定: 1142件 (Win 365 / Loss 444 / Flat 333) / pending 0件 / skip 775件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000402 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.74

## 6. Latest Market Context

- 更新: 2026-08-05T18:06:18.114175+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64712.5
- Funnel: target 948 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +36.12% | $36,441,564.20 |
| BLESS/USDT:USDT | +33.44% | $84,370,760.88 |
| UB/USDT:USDT | +21.25% | $23,188,740.11 |
| ESPORTS/USDT:USDT | +15.10% | $4,648,552.82 |
| BICO/USDT:USDT | +9.78% | $13,361,023.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +2.10% | +2.13% |
| BTW/USDT:USDT | below_1h_threshold | +1.72% | +1.75% |
| UB/USDT:USDT | below_1h_threshold | +1.62% | +1.65% |
| SHOPSTOCK/USDT:USDT | below_1h_threshold | +1.60% | +1.64% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.58% | +1.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
