# Decision Report

- generated_at: 2026-05-22T03:38:57.170202+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4661**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.45% / filled 20/20。**
- 全期間 MARKET基準: n=4661, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.45% | **+2.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.45% | **+2.45%** |
| ASK | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.24% | **+1.46%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.57% | **+1.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +1.63% | **+0.65%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -2.61% | **-0.52%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.65% | **-0.58%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 674件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T03:38:52.916690+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=77743.0
- Funnel: target 766 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEAR/USDT:USDT | +16.55% | $55,661,395.66 |
| GRASS/USDT:USDT | +15.86% | $3,756,452.87 |
| PEAQ/USDT:USDT | +11.17% | $1,949,052.21 |
| PLAY/USDT:USDT | +11.07% | $3,309,292.09 |
| PLUME/USDT:USDT | +10.31% | $1,724,106.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ATOM/USDT:USDT | below_1h_threshold | +2.99% | +2.85% |
| LUNC/USDT:USDT | below_1h_threshold | +2.19% | +2.05% |
| NEAR/USDT:USDT | below_1h_threshold | +2.13% | +2.00% |
| FET/USDT:USDT | below_1h_threshold | +1.71% | +1.57% |
| WLD/USDT:USDT | below_1h_threshold | +1.49% | +1.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
