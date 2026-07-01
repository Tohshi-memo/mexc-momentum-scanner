# Decision Report

- generated_at: 2026-07-01T10:42:06.835156+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7971**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=7971, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| ASK | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.00% | **-0.00%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.07% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$258.29** / 初期 $100.00 (+158.29%)
- 確定: 2370件 (Win 719 / Loss 788 / Flat 863) / skip 2162件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $258.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.00** / 初期 $100.00 (+7.00%)
- 確定: 502件 (Win 128 / Loss 121 / Flat 253) / skip 880件
- 成長率目線: 平均log +0.000135 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.00

## 5. Latest Market Context

- 更新: 2026-07-01T10:42:01.335808+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=58681.2
- Funnel: target 820 → liquid 151 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1, 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +68.14% | $7,787,987.12 |
| BASED/USDT:USDT | +29.49% | $11,579,412.83 |
| BTW/USDT:USDT | +28.43% | $8,746,625.33 |
| M/USDT:USDT | +25.29% | $4,496,291.33 |
| BAS/USDT:USDT | +23.87% | $2,691,782.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +4.18% | +4.59% |
| BTW/USDT:USDT | below_1h_threshold | +3.07% | +3.48% |
| TAC/USDT:USDT | below_1h_threshold | +2.71% | +3.11% |
| AALSTOCK/USDT:USDT | below_1h_threshold | +1.54% | +1.95% |
| JUP/USDT:USDT | below_1h_threshold | +1.29% | +1.70% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
