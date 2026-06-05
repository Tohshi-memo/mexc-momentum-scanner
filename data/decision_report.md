# Decision Report

- generated_at: 2026-06-05T01:25:24.521485+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5690**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.75% / filled 20/20。**
- 全期間 MARKET基準: n=5690, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.85% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.74% | **+0.48%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.87% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.30% | **+0.97%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.21% | **+0.85%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.09% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1008件 (Win 239 / Loss 312 / Flat 457) / skip 1243件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-05T01:25:21.456548+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=63264.5
- Funnel: target 771 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +87.61% | $11,731,314.68 |
| HOME/USDT:USDT | +28.31% | $7,443,943.90 |
| OPN/USDT:USDT | +19.15% | $36,701,117.53 |
| MEME/USDT:USDT | +9.22% | $2,024,576.08 |
| BEAT/USDT:USDT | +7.20% | $24,215,468.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +3.30% | +3.51% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.77% | +2.98% |
| BEAT/USDT:USDT | below_1h_threshold | +2.48% | +2.70% |
| ALLO/USDT:USDT | below_1h_threshold | +2.43% | +2.64% |
| AIA/USDT:USDT | below_1h_threshold | +2.05% | +2.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
