# Decision Report

- generated_at: 2026-06-18T18:31:28.535471+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7068**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=7068, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_BB3S | 6/19 | 31.6% | +4.92% | **+1.55%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.56% | **+1.41%** |
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.07% | **+0.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.47** / 初期 $100.00 (+1.47%)
- 確定トレード: 15件 (TP 6 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.47
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$218.94** / 初期 $100.00 (+118.94%)
- 確定: 1889件 (Win 534 / Loss 604 / Flat 751) / skip 1740件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEREBRO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $218.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 171件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T18:31:23.122692+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=62740.2
- Funnel: target 795 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +19.71% | $28,072,695.38 |
| PLAY/USDT:USDT | +10.22% | $1,628,731.56 |
| BASED/USDT:USDT | +9.48% | $1,023,073.43 |
| ZEREBRO/USDT:USDT | +9.24% | $1,270,444.23 |
| LAB/USDT:USDT | +7.05% | $25,883,944.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.97% | +4.72% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.76% | +4.51% |
| BASED/USDT:USDT | below_1h_threshold | +3.81% | +3.56% |
| JTO/USDT:USDT | below_1h_threshold | +2.37% | +2.12% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.92% | +1.67% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
