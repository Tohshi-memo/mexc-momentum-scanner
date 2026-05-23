# Decision Report

- generated_at: 2026-05-23T09:03:56.835638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4765**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.11% / filled 20/20。**
- 全期間 MARKET基準: n=4765, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+2.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.11% | **+2.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.11% | **+2.11%** |
| ASK | 20/20 | 100.0% | +2.07% | **+2.07%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.95% | **+0.76%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.23% | **+0.62%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.31% | **-0.15%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.57% | **-0.43%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 62件 (TP 17 / SL 42 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +6.60% 残高後 $97.16
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.52** / 初期 $100.00 (+21.52%)
- 確定: 611件 (Win 150 / Loss 194 / Flat 267) / skip 715件
- 成長率目線: 平均log +0.000319 / 幾何平均 +0.032% per trade / maxDD +4.21%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GMTTOKEN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $121.52

## 4. Latest Market Context

- 更新: 2026-05-23T09:03:54.669068+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=74622.8
- Funnel: target 764 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +126.71% | $67,171,415.23 |
| BEAT/USDT:USDT | +20.03% | $64,976,651.23 |
| GMTTOKEN/USDT:USDT | +18.57% | $2,085,957.61 |
| IN/USDT:USDT | +14.34% | $1,908,993.94 |
| MYX/USDT:USDT | +10.34% | $2,040,532.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.44% | +3.48% |
| BSB/USDT:USDT | below_1h_threshold | +1.41% | +1.45% |
| TAG/USDT:USDT | below_1h_threshold | +1.35% | +1.39% |
| BILL/USDT:USDT | below_1h_threshold | +0.67% | +0.72% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.54% | +0.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
