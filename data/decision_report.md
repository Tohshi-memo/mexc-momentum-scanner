# Decision Report

- generated_at: 2026-06-04T13:32:01.395857+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5625**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=5625, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.56% | **+2.56%** |
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.31% | **+0.91%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.01% | **+0.75%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.70% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.29% | **-0.16%** |

## 2. $100 Live Portfolio

- 残高: **$98.55** / 初期 $100.00 (-1.45%)
- 確定トレード: 95件 (TP 29 / SL 63 / EXP 3)
- 最新: OPN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.55
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1006件 (Win 239 / Loss 312 / Flat 455) / skip 1180件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T13:31:56.347981+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=63649.6
- Funnel: target 771 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +40.12% | $41,896,793.59 |
| EPIC/USDT:USDT | +35.03% | $6,589,663.88 |
| HEI/USDT:USDT | +32.68% | $4,813,130.56 |
| SIREN/USDT:USDT | +19.65% | $8,840,378.31 |
| BEAT/USDT:USDT | +14.03% | $18,744,912.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +3.82% | +3.95% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +3.77% | +3.91% |
| H/USDT:USDT | below_1h_threshold | +2.18% | +2.32% |
| SIREN/USDT:USDT | below_1h_threshold | +1.49% | +1.63% |
| OPG/USDT:USDT | below_1h_threshold | +1.47% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
