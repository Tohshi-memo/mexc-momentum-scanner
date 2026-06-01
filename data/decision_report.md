# Decision Report

- generated_at: 2026-06-01T03:01:12.487939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5267**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.73% / filled 20/20。**
- 全期間 MARKET基準: n=5267, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.82% | **+1.82%** |
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.57% | **+1.33%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.88% | **+1.32%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.87% | **+1.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.19% | **+0.33%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.46% | **+0.29%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.23% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 934件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T03:01:09.819197+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=73808.4
- Funnel: target 777 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +168.33% | $26,071,523.21 |
| H/USDT:USDT | +68.11% | $19,795,172.79 |
| STG/USDT:USDT | +31.44% | $22,428,585.00 |
| FHE/USDT:USDT | +25.14% | $1,026,172.47 |
| HOME/USDT:USDT | +21.17% | $3,808,756.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +2.28% | +2.22% |
| HOME/USDT:USDT | below_1h_threshold | +1.92% | +1.87% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.14% | +1.08% |
| BASED/USDT:USDT | below_1h_threshold | +0.57% | +0.51% |
| ZEC/USDT:USDT | below_1h_threshold | +0.49% | +0.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
