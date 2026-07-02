# Decision Report

- generated_at: 2026-07-02T20:46:18.965315+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8105**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8105, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +2.30% | **+0.35%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.29% | **+0.04%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_6PCT | 8/20 | 40.0% | -0.32% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.49% | **+1.87%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.70% | **+1.80%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.40% | **+1.32%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.57% | **+1.18%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.82% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 52件 (TP 19 / SL 32 / EXP 1)
- 最新: TAIKO/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2222件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 565件 (Win 136 / Loss 131 / Flat 298) / skip 951件
- 成長率目線: 平均log +0.000089 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0334 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIPPIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T20:46:08.142114+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=61363.9
- Funnel: target 834 → liquid 173 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +17.12% | $4,518,543.58 |
| PIPPIN/USDT:USDT | +14.08% | $3,178,107.26 |
| BASED/USDT:USDT | +13.86% | $14,558,631.37 |
| LAB/USDT:USDT | +11.75% | $11,509,736.82 |
| TAIKO/USDT:USDT | +9.88% | $101,600,496.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +3.93% | +4.07% |
| LAB/USDT:USDT | below_1h_threshold | +3.83% | +3.97% |
| BILL/USDT:USDT | below_1h_threshold | +2.96% | +3.10% |
| RAVE/USDT:USDT | below_1h_threshold | +1.97% | +2.12% |
| ADA/USDT:USDT | below_1h_threshold | +1.32% | +1.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
