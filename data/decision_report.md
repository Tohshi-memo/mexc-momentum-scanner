# Decision Report

- generated_at: 2026-07-01T10:14:54.455146+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7967**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=7967, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.62% | **+0.47%** |
| ASK | 20/20 | 100.0% | +0.42% | **+0.42%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.15% | **+0.77%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$259.59** / 初期 $100.00 (+159.59%)
- 確定: 2366件 (Win 719 / Loss 787 / Flat 860) / skip 2162件
- 成長率目線: 平均log +0.000403 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAIKO/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $259.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.00** / 初期 $100.00 (+7.00%)
- 確定: 502件 (Win 128 / Loss 121 / Flat 253) / skip 876件
- 成長率目線: 平均log +0.000135 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.00

## 5. Latest Market Context

- 更新: 2026-07-01T10:14:49.432467+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=58742.3
- Funnel: target 820 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +63.00% | $2,607,002.48 |
| BTW/USDT:USDT | +25.19% | $8,566,279.89 |
| BASED/USDT:USDT | +24.43% | $11,196,648.04 |
| BAS/USDT:USDT | +22.25% | $2,624,994.54 |
| DYDX/USDT:USDT | +14.38% | $18,822,632.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +2.77% | +3.08% |
| AALSTOCK/USDT:USDT | below_1h_threshold | +1.34% | +1.65% |
| TAC/USDT:USDT | below_1h_threshold | +1.33% | +1.63% |
| ZBT/USDT:USDT | below_1h_threshold | +1.06% | +1.37% |
| JUP/USDT:USDT | below_1h_threshold | +0.99% | +1.29% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
