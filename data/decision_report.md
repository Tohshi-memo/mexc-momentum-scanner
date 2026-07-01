# Decision Report

- generated_at: 2026-07-01T01:04:27.460453+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7938**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.30% / filled 20/20。**
- 全期間 MARKET基準: n=7938, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.31% | **+0.98%** |
| LIMIT_6PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.87% | **+0.35%** |
| ASK | 20/20 | 100.0% | +0.30% | **+0.30%** |
| MARKET | 20/20 | 100.0% | +0.30% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.40% | **+0.70%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.19% | **+0.22%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.48% | **+0.19%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.43% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$256.55** / 初期 $100.00 (+156.55%)
- 確定: 2356件 (Win 714 / Loss 787 / Flat 855) / skip 2143件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $256.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.52** / 初期 $100.00 (+6.52%)
- 確定: 480件 (Win 125 / Loss 121 / Flat 234) / skip 869件
- 成長率目線: 平均log +0.000131 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0273 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.52

## 5. Latest Market Context

- 更新: 2026-07-01T01:04:22.684690+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=58438.1
- Funnel: target 818 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +20.28% | $1,500,443.01 |
| AIGENSYN/USDT:USDT | +17.34% | $13,939,241.02 |
| OPG/USDT:USDT | +15.61% | $1,101,102.65 |
| BASED/USDT:USDT | +13.42% | $3,088,475.91 |
| BESTOCK/USDT:USDT | +11.88% | $1,178,776.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAIKO/USDT:USDT | below_1h_threshold | +1.94% | +2.13% |
| BAS/USDT:USDT | below_1h_threshold | +1.10% | +1.29% |
| OPG/USDT:USDT | below_1h_threshold | +0.82% | +1.01% |
| M/USDT:USDT | below_1h_threshold | +0.70% | +0.88% |
| RIF/USDT:USDT | below_1h_threshold | +0.47% | +0.66% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
