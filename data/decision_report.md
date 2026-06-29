# Decision Report

- generated_at: 2026-06-29T23:13:48.370439+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7839**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=7839, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.76% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.80% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +1.09% | **+1.09%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| ASK_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.13** / 初期 $100.00 (+2.13%)
- 確定トレード: 45件 (TP 16 / SL 28 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.13
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$267.05** / 初期 $100.00 (+167.05%)
- 確定: 2343件 (Win 714 / Loss 779 / Flat 850) / skip 2057件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MYX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $267.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 793件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0285 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T23:13:44.549669+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=60317.4
- Funnel: target 811 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +25.04% | $1,960,418.75 |
| SYN/USDT:USDT | +20.93% | $20,714,071.94 |
| CAP/USDT:USDT | +18.56% | $1,204,757.49 |
| AVAVSTOCK/USDT:USDT | +16.82% | $1,745,581.93 |
| BAS/USDT:USDT | +16.05% | $2,554,566.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.13% | +4.14% |
| M/USDT:USDT | below_1h_threshold | +2.13% | +2.15% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.89% | +1.90% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.06% | +1.08% |
| BILL/USDT:USDT | below_1h_threshold | +1.02% | +1.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
