# Decision Report

- generated_at: 2026-05-21T12:54:00.481485+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4626**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=4626, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/18 | 38.9% | +3.75% | **+1.46%** |
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.20% | **+1.14%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| ASK | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.40% | **+0.22%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.23% | **+0.13%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.13% | **+0.06%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.07% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$95.73** / 初期 $100.00 (-4.27%)
- 確定トレード: 59件 (TP 15 / SL 41 / EXP 3)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.73
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 641件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T12:53:56.798529+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=77259.3
- Funnel: target 766 → liquid 138 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1, 4h RSI 78.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +49.10% | $32,373,357.54 |
| PROVE/USDT:USDT | +41.19% | $5,868,183.48 |
| FIDA/USDT:USDT | +39.59% | $13,948,729.58 |
| ROAM/USDT:USDT | +32.34% | $2,277,206.58 |
| USELESS/USDT:USDT | +25.15% | $2,438,590.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.07% | +3.94% |
| USELESS/USDT:USDT | below_1h_threshold | +2.96% | +2.83% |
| NIL/USDT:USDT | below_1h_threshold | +2.25% | +2.11% |
| BEAT/USDT:USDT | below_1h_threshold | +1.90% | +1.77% |
| SPX/USDT:USDT | below_1h_threshold | +1.65% | +1.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
