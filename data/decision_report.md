# Decision Report

- generated_at: 2026-05-23T10:54:12.018261+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4770**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.71% / filled 20/20。**
- 全期間 MARKET基準: n=4770, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+2.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.71% | **+2.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.71% | **+2.71%** |
| ASK | 20/20 | 100.0% | +2.65% | **+2.65%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.64% | **+1.31%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.55% | **+0.30%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.48% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | -0.32% | **-0.23%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.38% | **-0.32%** |
| MARKET_LONG | 20/20 | 100.0% | -0.34% | **-0.34%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 62件 (TP 17 / SL 42 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +6.60% 残高後 $97.16
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 715件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T10:54:06.617940+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=74691.2
- Funnel: target 764 → liquid 132 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.9 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +140.33% | $76,865,759.99 |
| BEAT/USDT:USDT | +26.20% | $68,751,253.46 |
| IN/USDT:USDT | +20.86% | $2,035,152.30 |
| GMTTOKEN/USDT:USDT | +16.87% | $2,686,637.40 |
| BILL/USDT:USDT | +13.01% | $16,926,990.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +3.28% | +3.19% |
| H/USDT:USDT | below_1h_threshold | +2.00% | +1.92% |
| SIREN/USDT:USDT | below_1h_threshold | +1.62% | +1.54% |
| GRASS/USDT:USDT | below_1h_threshold | +1.49% | +1.41% |
| VVV/USDT:USDT | below_1h_threshold | +1.06% | +0.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
