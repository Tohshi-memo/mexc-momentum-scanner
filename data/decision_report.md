# Decision Report

- generated_at: 2026-05-25T07:44:13.749293+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4848**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=4848, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.45% | **+0.45%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.09% | **-0.01%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.36% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.32% | **+1.19%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.01% | **+1.01%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.24% | **+0.93%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.11% | **+0.83%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.64% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.50** / 初期 $100.00 (+26.50%)
- 確定: 654件 (Win 164 / Loss 206 / Flat 284) / skip 755件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $126.50

## 4. Latest Market Context

- 更新: 2026-05-25T07:44:08.691841+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=77283.6
- Funnel: target 764 → liquid 118 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAN/USDT:USDT | +41.91% | $4,806,524.21 |
| PLAY/USDT:USDT | +21.40% | $4,347,825.59 |
| SPORTFUN/USDT:USDT | +11.69% | $1,313,420.16 |
| SAGA/USDT:USDT | +11.33% | $1,497,934.12 |
| UB/USDT:USDT | +10.72% | $5,776,587.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.11% | +4.24% |
| PHA/USDT:USDT | below_1h_threshold | +2.81% | +2.94% |
| BILL/USDT:USDT | below_1h_threshold | +2.39% | +2.53% |
| GRASS/USDT:USDT | below_1h_threshold | +1.46% | +1.60% |
| XAN/USDT:USDT | below_1h_threshold | +1.31% | +1.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
