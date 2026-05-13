# Decision Report

- generated_at: 2026-05-13T16:43:20.422618+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4236**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.92% / filled 20/20。**
- 全期間 MARKET基準: n=4236, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.00% | **+1.90%** |
| ASK | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.87% | **+1.31%** |
| LIMIT_BB3S | 7/18 | 38.9% | +1.97% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.27% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 38件 (TP 10 / SL 25 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 455件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T16:43:16.957513+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.43% price=79132.7
- Funnel: target 765 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +6.30% | $5,363,398.97 |
| H/USDT:USDT | +4.93% | $5,498,902.21 |
| COS/USDT:USDT | +4.79% | $2,385,922.21 |
| VELO/USDT:USDT | +4.77% | $1,997,077.64 |
| VELVET/USDT:USDT | +4.48% | $1,115,262.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_relative_strength | +5.15% | +4.72% |
| TRUTH/USDT:USDT | below_relative_strength | +5.11% | +4.68% |
| VELO/USDT:USDT | below_1h_threshold | +4.77% | +4.34% |
| VELVET/USDT:USDT | below_1h_threshold | +4.59% | +4.16% |
| COS/USDT:USDT | below_1h_threshold | +4.57% | +4.14% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
