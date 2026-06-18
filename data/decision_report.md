# Decision Report

- generated_at: 2026-06-18T19:42:02.800966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7071**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=7071, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.31% | **+1.31%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_BB3S | 5/19 | 26.3% | +4.30% | **+1.13%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.19% | **+1.02%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.01% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.14% | **+0.12%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.31% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$101.47** / 初期 $100.00 (+1.47%)
- 確定トレード: 15件 (TP 6 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.47
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.02** / 初期 $100.00 (+120.02%)
- 確定: 1892件 (Win 536 / Loss 605 / Flat 751) / skip 1740件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $220.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 174件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T19:41:56.617194+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=62870.6
- Funnel: target 795 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +24.65% | $30,195,680.56 |
| ZEREBRO/USDT:USDT | +13.73% | $1,857,289.82 |
| EDEN/USDT:USDT | +13.44% | $1,183,457.40 |
| PLAY/USDT:USDT | +13.27% | $1,868,155.39 |
| LAB/USDT:USDT | +10.19% | $28,005,933.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JTO/USDT:USDT | below_relative_strength | +5.09% | +4.79% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +4.64% | +4.34% |
| VELVET/USDT:USDT | below_1h_threshold | +4.31% | +4.01% |
| LAB/USDT:USDT | below_1h_threshold | +4.01% | +3.72% |
| BLESS/USDT:USDT | below_1h_threshold | +2.93% | +2.64% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
