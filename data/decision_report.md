# Decision Report

- generated_at: 2026-07-01T10:33:30.006774+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7970**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=7970, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.62% | **+1.62%** |
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.40% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -2.07% | **-0.31%** |
| ASK_LONG | 20/20 | 100.0% | -0.38% | **-0.38%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$258.29** / 初期 $100.00 (+158.29%)
- 確定: 2369件 (Win 719 / Loss 788 / Flat 862) / skip 2162件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $258.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.00** / 初期 $100.00 (+7.00%)
- 確定: 502件 (Win 128 / Loss 121 / Flat 253) / skip 879件
- 成長率目線: 平均log +0.000135 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.00

## 5. Latest Market Context

- 更新: 2026-07-01T10:33:22.649736+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=58710.1
- Funnel: target 820 → liquid 151 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1, 4h RSI 80.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +81.14% | $7,240,080.29 |
| BASED/USDT:USDT | +27.22% | $11,480,859.06 |
| BTW/USDT:USDT | +26.62% | $8,686,802.79 |
| BAS/USDT:USDT | +22.04% | $2,669,155.11 |
| ZBT/USDT:USDT | +18.40% | $1,690,552.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +2.66% | +3.02% |
| TAC/USDT:USDT | below_1h_threshold | +2.44% | +2.80% |
| BTW/USDT:USDT | below_1h_threshold | +1.81% | +2.17% |
| AALSTOCK/USDT:USDT | below_1h_threshold | +1.29% | +1.65% |
| JUP/USDT:USDT | below_1h_threshold | +1.20% | +1.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
