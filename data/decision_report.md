# Decision Report

- generated_at: 2026-06-13T03:06:26.402706+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6558**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.65% / filled 20/20。**
- 全期間 MARKET基準: n=6558, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.65% | **+2.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.71% | **+2.71%** |
| MARKET | 20/20 | 100.0% | +2.65% | **+2.65%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.12% | **+0.78%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.88% | **+0.72%** |
| LIMIT_ATR | 5/20 | 25.0% | +1.38% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.97% | **-0.29%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.67% | **-0.61%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1431件 (Win 389 / Loss 464 / Flat 578) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T03:06:23.672102+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=63678.1
- Funnel: target 774 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDGE/USDT:USDT | +22.55% | $1,562,305.42 |
| VVV/USDT:USDT | +17.76% | $4,111,665.62 |
| SQD/USDT:USDT | +14.41% | $1,101,724.96 |
| RIF/USDT:USDT | +12.32% | $1,345,314.29 |
| TRUMPOFFICIAL/USDT:USDT | +10.33% | $39,038,242.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +1.49% | +1.38% |
| COAI/USDT:USDT | below_1h_threshold | +1.01% | +0.90% |
| BTW/USDT:USDT | below_1h_threshold | +1.00% | +0.90% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.58% | +0.48% |
| AIN/USDT:USDT | below_1h_threshold | +0.55% | +0.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
