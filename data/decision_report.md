# Decision Report

- generated_at: 2026-06-12T23:46:32.937155+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6549**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.52% / filled 20/20。**
- 全期間 MARKET基準: n=6549, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+4.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.52% | **+4.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.52% | **+4.52%** |
| ASK | 20/20 | 100.0% | +3.97% | **+3.97%** |
| LIMIT_1PCT | 14/20 | 70.0% | +3.50% | **+2.45%** |
| LIMIT_2PCT | 11/20 | 55.0% | +3.29% | **+1.81%** |
| LIMIT_ATR | 7/20 | 35.0% | +5.07% | **+1.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.22% | **+0.36%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | -1.98% | **-1.28%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$163.00** / 初期 $100.00 (+63.00%)
- 確定: 1422件 (Win 388 / Loss 463 / Flat 571) / skip 1688件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $163.00

## 4. Latest Market Context

- 更新: 2026-06-12T23:46:30.204961+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=63512.8
- Funnel: target 774 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +17.57% | $67,267,009.55 |
| ORCA/USDT:USDT | +13.74% | $1,581,562.54 |
| H/USDT:USDT | +13.03% | $29,671,001.32 |
| AIN/USDT:USDT | +11.56% | $1,900,407.40 |
| EDGE/USDT:USDT | +10.73% | $1,072,022.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.22% | +4.18% |
| H/USDT:USDT | below_1h_threshold | +2.77% | +2.72% |
| COAI/USDT:USDT | below_1h_threshold | +1.66% | +1.62% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.18% | +1.14% |
| STG/USDT:USDT | below_1h_threshold | +0.74% | +0.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
