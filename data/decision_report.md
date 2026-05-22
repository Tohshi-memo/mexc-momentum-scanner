# Decision Report

- generated_at: 2026-05-22T17:44:56.502359+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4730**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=4730, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +4.29% | **+1.29%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.97% | **+0.83%** |
| LIMIT_10PCT | 4/20 | 20.0% | +3.73% | **+0.75%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.65% | **+0.74%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.29% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.72% | **+1.63%** |
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

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 576件 (Win 149 / Loss 187 / Flat 240) / skip 715件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-22T17:44:50.757886+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=76974.4
- Funnel: target 765 → liquid 135 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +60.26% | $30,889,119.81 |
| BEAT/USDT:USDT | +7.81% | $33,540,486.61 |
| BILL/USDT:USDT | +6.99% | $13,441,890.42 |
| INJ/USDT:USDT | +6.21% | $36,565,893.66 |
| GUA/USDT:USDT | +5.55% | $1,083,055.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +4.23% | +4.15% |
| GRASS/USDT:USDT | below_1h_threshold | +2.42% | +2.35% |
| GUA/USDT:USDT | below_1h_threshold | +2.30% | +2.22% |
| AGT/USDT:USDT | below_1h_threshold | +1.69% | +1.61% |
| PEAQ/USDT:USDT | below_1h_threshold | +1.66% | +1.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
