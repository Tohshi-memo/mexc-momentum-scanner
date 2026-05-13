# Decision Report

- generated_at: 2026-05-13T18:43:06.423866+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4245**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=4245, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.35% | **+1.29%** |
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_BB3S | 4/16 | 25.0% | +0.83% | **+0.21%** |
| ASK | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.09% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$98.19** / 初期 $100.00 (-1.81%)
- 確定トレード: 39件 (TP 10 / SL 26 / EXP 3)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 464件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T18:43:00.798790+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=79686.0
- Funnel: target 761 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +25.36% | $1,140,409.69 |
| BEAT/USDT:USDT | +13.18% | $2,013,578.12 |
| GUA/USDT:USDT | +12.59% | $3,747,862.38 |
| GIGA/USDT:USDT | +12.53% | $2,078,047.47 |
| UB/USDT:USDT | +10.25% | $10,713,400.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.50% | +4.23% |
| GUA/USDT:USDT | below_1h_threshold | +4.29% | +4.01% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.81% | +2.54% |
| IRYS/USDT:USDT | below_1h_threshold | +2.75% | +2.48% |
| CFX/USDT:USDT | below_1h_threshold | +2.66% | +2.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
