# Decision Report

- generated_at: 2026-06-20T21:31:19.801265+00:00
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

- 更新: 2026-06-20T21:31:14.237522+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=63901.8
- Funnel: target 796 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +40.05% | $46,122,370.64 |
| ALICE/USDT:USDT | +26.04% | $1,763,787.81 |
| VELVET/USDT:USDT | +10.64% | $16,763,459.96 |
| ASTEROID/USDT:USDT | +8.24% | $1,583,351.96 |
| LAB/USDT:USDT | +6.42% | $23,953,575.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.88% | +1.88% |
| GUA/USDT:USDT | below_1h_threshold | +1.85% | +1.84% |
| AXS/USDT:USDT | below_1h_threshold | +1.74% | +1.74% |
| JUP/USDT:USDT | below_1h_threshold | +1.23% | +1.22% |
| AERO/USDT:USDT | below_1h_threshold | +1.04% | +1.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
