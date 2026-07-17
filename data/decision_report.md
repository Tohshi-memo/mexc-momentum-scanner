# Decision Report

- generated_at: 2026-07-17T15:36:24.475727+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8863**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8863, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.49% | **+1.22%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.10% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.19% | **+0.98%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.42% | **+0.85%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$355.51** / 初期 $100.00 (+255.51%)
- 確定: 2978件 (Win 928 / Loss 949 / Flat 1101) / skip 2446件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LRC/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $355.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$109.68** / 初期 $100.00 (+9.68%)
- 確定: 825件 (Win 196 / Loss 172 / Flat 457) / skip 1449件
- 成長率目線: 平均log +0.000112 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0684 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LRC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $109.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.24** / 初期 $100.00 (-0.76%)
- 確定: 129件 (Win 42 / Loss 74 / Flat 13) / pending 4件 / skip 201件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000258 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LRC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $99.24

## 6. Latest Market Context

- 更新: 2026-07-17T15:36:13.926030+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=63180.0
- Funnel: target 885 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LRC/USDT:USDT | +63.66% | $5,520,062.98 |
| AKE/USDT:USDT | +23.98% | $40,177,231.82 |
| XEC/USDT:USDT | +22.51% | $2,446,311.83 |
| KAITO/USDT:USDT | +17.91% | $5,802,480.74 |
| BULLA/USDT:USDT | +17.55% | $1,295,000.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +3.78% | +3.72% |
| DEXE/USDT:USDT | below_1h_threshold | +2.81% | +2.76% |
| AEHRSTOCK/USDT:USDT | below_1h_threshold | +2.81% | +2.76% |
| DRAM/USDT:USDT | below_1h_threshold | +2.51% | +2.46% |
| O/USDT:USDT | below_1h_threshold | +2.33% | +2.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
