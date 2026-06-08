# Decision Report

- generated_at: 2026-06-08T06:15:33.987574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6036**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.20% / filled 20/20。**
- 全期間 MARKET基準: n=6036, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |
| ASK | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.48% | **+1.25%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.31% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.22% | **+0.14%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.04% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.08** / 初期 $100.00 (-1.92%)
- 確定トレード: 8件 (TP 1 / SL 6 / EXP 1)
- 最新: HOME/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.08
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1453件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T06:15:30.772167+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=62891.2
- Funnel: target 773 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +41.63% | $101,018,561.36 |
| PIPPIN/USDT:USDT | +27.08% | $8,855,887.37 |
| ALLO/USDT:USDT | +23.04% | $37,159,185.41 |
| VELVET/USDT:USDT | +18.93% | $3,371,282.43 |
| BANK/USDT:USDT | +16.27% | $5,140,565.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +3.79% | +3.54% |
| ALLO/USDT:USDT | below_1h_threshold | +2.60% | +2.36% |
| BANK/USDT:USDT | below_1h_threshold | +2.46% | +2.22% |
| ONDO/USDT:USDT | below_1h_threshold | +2.19% | +1.94% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.09% | +1.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
