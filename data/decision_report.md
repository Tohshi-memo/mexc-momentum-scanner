# Decision Report

- generated_at: 2026-05-15T04:23:08.105908+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4322**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.20% / filled 20/20。**
- 全期間 MARKET基準: n=4322, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.26% | **+2.26%** |
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_BB3S | 4/13 | 30.8% | +5.64% | **+1.74%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.74% | **+1.30%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.96% | **+1.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.91% | **+0.86%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.79% | **+0.47%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.93% | **+0.47%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.69% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 44件 (TP 11 / SL 30 / EXP 3)
- 最新: SKYAI/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 374件 (Win 97 / Loss 131 / Flat 146) / skip 509件
- 成長率目線: 平均log +0.000497 / 幾何平均 +0.050% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIGSTOCK/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $120.42

## 4. Latest Market Context

- 更新: 2026-05-15T04:23:04.759091+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=80857.1
- Funnel: target 764 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +30.61% | $2,804,996.44 |
| GWEI/USDT:USDT | +21.67% | $1,091,508.61 |
| UP/USDT:USDT | +18.93% | $4,024,416.40 |
| FIGSTOCK/USDT:USDT | +14.10% | $3,138,157.98 |
| TAC/USDT:USDT | +12.65% | $2,083,648.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +3.10% | +3.31% |
| RIVER/USDT:USDT | below_1h_threshold | +1.46% | +1.66% |
| UB/USDT:USDT | below_1h_threshold | +1.21% | +1.42% |
| GWEI/USDT:USDT | below_1h_threshold | +0.76% | +0.96% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.67% | +0.87% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
