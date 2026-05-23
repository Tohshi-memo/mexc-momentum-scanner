# Decision Report

- generated_at: 2026-05-23T10:14:10.862545+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4767**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.11% / filled 20/20。**
- 全期間 MARKET基準: n=4767, expectancy=-0.08%
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
| ASK | 20/20 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.61% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -0.03% | **-0.03%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.31% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 62件 (TP 17 / SL 42 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +6.60% 残高後 $97.16
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.52** / 初期 $100.00 (+21.52%)
- 確定: 613件 (Win 150 / Loss 194 / Flat 269) / skip 715件
- 成長率目線: 平均log +0.000318 / 幾何平均 +0.032% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $121.52

## 4. Latest Market Context

- 更新: 2026-05-23T10:14:05.270259+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=74703.8
- Funnel: target 764 → liquid 132 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.1 >= 65=1, 4h RSI 78.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +174.44% | $72,122,880.10 |
| BEAT/USDT:USDT | +24.14% | $65,290,740.88 |
| GMTTOKEN/USDT:USDT | +19.71% | $2,597,308.52 |
| IN/USDT:USDT | +12.95% | $1,968,514.21 |
| BILL/USDT:USDT | +12.35% | $16,649,384.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +1.73% | +1.63% |
| GRASS/USDT:USDT | below_1h_threshold | +1.37% | +1.27% |
| KITE/USDT:USDT | below_1h_threshold | +1.33% | +1.24% |
| UB/USDT:USDT | below_1h_threshold | +0.95% | +0.85% |
| RIVER/USDT:USDT | below_1h_threshold | +0.84% | +0.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
