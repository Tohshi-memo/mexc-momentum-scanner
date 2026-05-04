# Decision Report

- generated_at: 2026-05-04T05:47:18.987685+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3160**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=3160, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.06% | **+0.95%** |
| LIMIT_BB3S | 4/11 | 36.4% | +2.37% | **+0.86%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.64% | **+0.74%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.48% | **+0.74%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.65% | **+0.49%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T05:47:16.404377+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=80020.2
- Funnel: target 758 → liquid 173 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1, 4h RSI 85.7 >= 65=1, 4h RSI 81.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +62.31% | $23,263,961.62 |
| SKYAI/USDT:USDT | +53.10% | $46,591,213.52 |
| TAG/USDT:USDT | +49.83% | $7,503,545.52 |
| LAB/USDT:USDT | +47.30% | $218,095,495.44 |
| TST/USDT:USDT | +43.18% | $6,476,034.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.89% | +5.24% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.73% | +5.08% |
| SAPIEN/USDT:USDT | below_1h_threshold | +3.06% | +3.41% |
| ORDI/USDT:USDT | below_1h_threshold | +2.80% | +3.15% |
| USTC/USDT:USDT | below_1h_threshold | +2.53% | +2.88% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
