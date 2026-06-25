# Decision Report

- generated_at: 2026-06-25T21:47:15.489337+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7587**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7587, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |
| ASK | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.20% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.98% | **+0.84%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.59% | **+0.24%** |
| MARKET_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$103.17** / 初期 $100.00 (+3.17%)
- 確定トレード: 40件 (TP 15 / SL 24 / EXP 1)
- 最新: DRAM/USDT:USDT EXPIRED PnL +1.79% 残高後 $103.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 2016件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 377件 (Win 103 / Loss 100 / Flat 174) / skip 621件
- 成長率目線: 平均log +0.000194 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XPL/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-25T21:47:09.767063+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.84% price=59926.8
- Funnel: target 807 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FOGO/USDT:USDT | +24.34% | $1,348,441.48 |
| IP/USDT:USDT | +15.05% | $2,402,872.34 |
| IDOL/USDT:USDT | +12.39% | $1,591,566.54 |
| XPL/USDT:USDT | +11.11% | $10,538,720.17 |
| HEI/USDT:USDT | +7.16% | $5,767,949.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +3.93% | +3.09% |
| ZEC/USDT:USDT | below_1h_threshold | +3.39% | +2.55% |
| APE/USDT:USDT | below_1h_threshold | +3.18% | +2.34% |
| PIPPIN/USDT:USDT | below_1h_threshold | +3.12% | +2.28% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.65% | +1.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
