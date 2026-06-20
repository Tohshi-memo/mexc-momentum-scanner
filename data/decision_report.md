# Decision Report

- generated_at: 2026-06-20T21:42:48.630281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7273**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7273, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.54% | **-1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.24% | **+0.37%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.17% | **+0.98%** |
| ASK_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.92% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$101.45** / 初期 $100.00 (+1.45%)
- 確定トレード: 24件 (TP 9 / SL 15 / EXP 0)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.43** / 初期 $100.00 (+137.43%)
- 確定: 2002件 (Win 591 / Loss 653 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALICE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $237.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 374件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T21:42:43.987794+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63939.9
- Funnel: target 796 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +44.50% | $46,603,859.24 |
| ALICE/USDT:USDT | +22.15% | $1,846,704.65 |
| ASTEROID/USDT:USDT | +9.93% | $1,629,229.92 |
| VELVET/USDT:USDT | +9.84% | $16,831,480.44 |
| LAB/USDT:USDT | +6.61% | $23,991,100.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXS/USDT:USDT | below_1h_threshold | +3.84% | +3.77% |
| BICO/USDT:USDT | below_1h_threshold | +2.77% | +2.71% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.68% | +1.62% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.58% | +1.52% |
| JUP/USDT:USDT | below_1h_threshold | +1.52% | +1.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
