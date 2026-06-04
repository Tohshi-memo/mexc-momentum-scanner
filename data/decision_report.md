# Decision Report

- generated_at: 2026-06-04T14:32:19.738471+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5631**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=5631, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.76% | **+0.61%** |
| LIMIT_BB3S | 2/17 | 11.8% | +3.35% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.68%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +0.69% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$98.55** / 初期 $100.00 (-1.45%)
- 確定トレード: 95件 (TP 29 / SL 63 / EXP 3)
- 最新: OPN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.55
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1007件 (Win 239 / Loss 312 / Flat 456) / skip 1185件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T14:32:14.260044+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=63927.0
- Funnel: target 772 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEST/USDT:USDT | +68.32% | $1,746,786.34 |
| EPIC/USDT:USDT | +37.00% | $6,930,623.24 |
| HEI/USDT:USDT | +33.43% | $4,967,851.52 |
| OPN/USDT:USDT | +31.12% | $43,689,882.11 |
| SIREN/USDT:USDT | +20.07% | $9,479,227.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +4.06% | +4.48% |
| HEI/USDT:USDT | below_1h_threshold | +3.95% | +4.38% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.91% | +4.33% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.21% | +2.63% |
| OPG/USDT:USDT | below_1h_threshold | +1.68% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
