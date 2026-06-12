# Decision Report

- generated_at: 2026-06-12T18:14:36.156151+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6538**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.02% / filled 20/20。**
- 全期間 MARKET基準: n=6538, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+3.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.02% | **+3.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.02% | **+3.02%** |
| ASK | 20/20 | 100.0% | +2.15% | **+2.15%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.58% | **+1.81%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.06% | **+1.65%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.88% | **+1.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.71% | **+0.56%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.36% | **-0.20%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.73% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$95.16** / 初期 $100.00 (-4.84%)
- 確定トレード: 23件 (TP 4 / SL 18 / EXP 1)
- 最新: AIO/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.64** / 初期 $100.00 (+64.64%)
- 確定: 1411件 (Win 388 / Loss 461 / Flat 562) / skip 1688件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_10PCT_LONG` TP_HIT account +1.00% 残高後 $164.64

## 4. Latest Market Context

- 更新: 2026-06-12T18:14:33.091727+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63799.4
- Funnel: target 774 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +13.79% | $9,223,474.13 |
| ESPORTS/USDT:USDT | +8.80% | $65,679,978.33 |
| HOME/USDT:USDT | +7.64% | $3,043,846.76 |
| BTW/USDT:USDT | +6.20% | $2,859,340.04 |
| RKLBSTOCK/USDT:USDT | +5.88% | $1,494,438.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +2.94% | +3.00% |
| BTW/USDT:USDT | below_1h_threshold | +2.13% | +2.19% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.82% | +0.88% |
| LUMIA/USDT:USDT | below_1h_threshold | +0.44% | +0.49% |
| ENJ/USDT:USDT | below_1h_threshold | +0.35% | +0.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
