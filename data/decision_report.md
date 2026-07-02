# Decision Report

- generated_at: 2026-07-02T11:47:29.617437+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8071**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=8071, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.06% | **+2.06%** |
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | +2.30% | **+0.35%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.56% | **+0.53%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.31% | **+0.17%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.03% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 49件 (TP 18 / SL 30 / EXP 1)
- 最新: NOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2188件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 556件 (Win 136 / Loss 131 / Flat 289) / skip 926件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T11:47:17.672681+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=61253.4
- Funnel: target 834 → liquid 168 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1, 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +70.87% | $10,595,242.98 |
| BIRB/USDT:USDT | +63.25% | $7,247,762.86 |
| BREV/USDT:USDT | +41.66% | $5,038,448.91 |
| SYN/USDT:USDT | +32.25% | $21,953,280.98 |
| US/USDT:USDT | +31.11% | $1,283,864.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_relative_strength | +5.01% | +4.98% |
| TAIKO/USDT:USDT | below_1h_threshold | +4.54% | +4.51% |
| BIRB/USDT:USDT | below_1h_threshold | +3.70% | +3.68% |
| JUP/USDT:USDT | below_1h_threshold | +3.18% | +3.15% |
| COOKIE/USDT:USDT | below_1h_threshold | +2.02% | +2.00% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
