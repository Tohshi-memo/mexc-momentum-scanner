# Decision Report

- generated_at: 2026-05-22T17:39:06.269526+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4729**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=4729, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +4.23% | **+1.06%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.09% | **+0.93%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.98% | **+0.50%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.61% | **+1.56%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.51% | **+1.00%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.44** / 初期 $100.00 (+24.44%)
- 確定: 575件 (Win 148 / Loss 187 / Flat 240) / skip 715件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $124.44

## 4. Latest Market Context

- 更新: 2026-05-22T17:39:03.219875+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=76944.2
- Funnel: target 765 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +63.24% | $30,518,930.57 |
| BEAT/USDT:USDT | +7.32% | $33,193,574.35 |
| INJ/USDT:USDT | +5.61% | $36,148,492.70 |
| GUA/USDT:USDT | +5.52% | $1,075,688.86 |
| GRASS/USDT:USDT | +3.95% | $8,734,854.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +4.50% | +4.46% |
| INJ/USDT:USDT | below_1h_threshold | +3.91% | +3.87% |
| GRASS/USDT:USDT | below_1h_threshold | +3.03% | +2.99% |
| GUA/USDT:USDT | below_1h_threshold | +2.08% | +2.04% |
| UNI/USDT:USDT | below_1h_threshold | +1.53% | +1.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
