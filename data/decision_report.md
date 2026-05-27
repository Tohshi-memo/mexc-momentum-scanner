# Decision Report

- generated_at: 2026-05-27T20:59:41.864906+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4942**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4942, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +3.68% | **+2.39%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.74% | **+2.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.80% | **+1.62%** |
| LIMIT_4PCT | 10/20 | 50.0% | +2.87% | **+1.43%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +2.67% | **+1.60%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +4.07% | **+1.22%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.38% | **+0.83%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$96.19** / 初期 $100.00 (-3.81%)
- 確定トレード: 67件 (TP 18 / SL 46 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.19
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 819件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T20:59:36.647711+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=75252.0
- Funnel: target 771 → liquid 147 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +31.90% | $4,232,724.72 |
| RIVER/USDT:USDT | +10.82% | $9,017,868.05 |
| MRVLSTOCK/USDT:USDT | +6.10% | $6,118,602.73 |
| JTO/USDT:USDT | +5.16% | $2,617,454.22 |
| GENIUS/USDT:USDT | +5.04% | $1,282,773.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRT/USDT:USDT | below_1h_threshold | +4.55% | +4.27% |
| RIVER/USDT:USDT | below_1h_threshold | +3.19% | +2.91% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.75% | +1.46% |
| XLM/USDT:USDT | below_1h_threshold | +1.03% | +0.75% |
| XMR/USDT:USDT | below_1h_threshold | +0.89% | +0.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
