# Decision Report

- generated_at: 2026-05-23T10:44:09.493357+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4769**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.11% / filled 20/20。**
- 全期間 MARKET基準: n=4769, expectancy=-0.08%
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
| LIMIT_ATR | 12/20 | 60.0% | +0.58% | **+0.35%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.33% | **+0.28%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 62件 (TP 17 / SL 42 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +6.60% 残高後 $97.16
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.52** / 初期 $100.00 (+21.52%)
- 確定: 615件 (Win 150 / Loss 194 / Flat 271) / skip 715件
- 成長率目線: 平均log +0.000317 / 幾何平均 +0.032% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $121.52

## 4. Latest Market Context

- 更新: 2026-05-23T10:44:04.409934+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=74726.1
- Funnel: target 764 → liquid 132 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1, 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +162.88% | $75,732,132.13 |
| BEAT/USDT:USDT | +29.00% | $68,213,498.66 |
| IN/USDT:USDT | +19.47% | $2,017,903.62 |
| GMTTOKEN/USDT:USDT | +17.72% | $2,674,527.92 |
| BILL/USDT:USDT | +13.36% | $16,880,669.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.38% | +3.25% |
| MYX/USDT:USDT | below_1h_threshold | +3.33% | +3.20% |
| H/USDT:USDT | below_1h_threshold | +2.05% | +1.92% |
| GRASS/USDT:USDT | below_1h_threshold | +1.64% | +1.51% |
| KITE/USDT:USDT | below_1h_threshold | +1.11% | +0.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
