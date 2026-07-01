# Decision Report

- generated_at: 2026-07-01T01:31:48.442849+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7940**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=7940, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +1.49% | **+1.04%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.43% | **+1.00%** |
| ASK | 20/20 | 100.0% | +0.90% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.69% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.50% | **+0.90%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.78% | **+0.39%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.40% | **+0.22%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.19% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$256.55** / 初期 $100.00 (+156.55%)
- 確定: 2356件 (Win 714 / Loss 787 / Flat 855) / skip 2145件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $256.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.52** / 初期 $100.00 (+6.52%)
- 確定: 482件 (Win 125 / Loss 121 / Flat 236) / skip 869件
- 成長率目線: 平均log +0.000131 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0273 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.52

## 5. Latest Market Context

- 更新: 2026-07-01T01:31:43.599623+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=58445.7
- Funnel: target 818 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +17.47% | $14,459,879.49 |
| BASED/USDT:USDT | +12.94% | $3,268,195.20 |
| TAIKO/USDT:USDT | +12.71% | $1,582,264.43 |
| OPG/USDT:USDT | +12.28% | $1,132,106.71 |
| BTW/USDT:USDT | +12.21% | $10,096,882.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +1.56% | +1.74% |
| H/USDT:USDT | below_1h_threshold | +1.48% | +1.65% |
| EVAA/USDT:USDT | below_1h_threshold | +1.28% | +1.45% |
| NES/USDT:USDT | below_1h_threshold | +1.16% | +1.34% |
| XLM/USDT:USDT | below_1h_threshold | +0.89% | +1.07% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
