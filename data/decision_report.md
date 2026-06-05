# Decision Report

- generated_at: 2026-06-05T10:13:19.336497+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5708**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.13% / filled 20/20。**
- 全期間 MARKET基準: n=5708, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.25% | **+1.25%** |
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.81% | **+0.84%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.95% | **+0.71%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.17% | **+0.35%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.17% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1010件 (Win 239 / Loss 313 / Flat 458) / skip 1259件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T10:13:16.479197+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=62713.7
- Funnel: target 773 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +81.28% | $22,839,865.29 |
| BABY/USDT:USDT | +32.35% | $3,194,582.34 |
| OPN/USDT:USDT | +29.02% | $39,933,075.95 |
| CLO/USDT:USDT | +20.22% | $1,074,173.94 |
| BEAT/USDT:USDT | +14.58% | $27,583,740.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +2.70% | +2.89% |
| APPSTOCK/USDT:USDT | below_1h_threshold | +0.81% | +1.00% |
| BTW/USDT:USDT | below_1h_threshold | +0.80% | +0.98% |
| HOME/USDT:USDT | below_1h_threshold | +0.63% | +0.82% |
| HEI/USDT:USDT | below_1h_threshold | +0.54% | +0.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
