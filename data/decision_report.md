# Decision Report

- generated_at: 2026-05-13T04:23:04.126687+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4188**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=4188, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.98% | **+0.88%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.12% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.75% | **+0.75%** |
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.16% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.12% | **+0.09%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.22% | **+0.08%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.01% | **+0.01%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.34** / 初期 $100.00 (+20.34%)
- 確定: 324件 (Win 92 / Loss 115 / Flat 117) / skip 425件
- 成長率目線: 平均log +0.000571 / 幾何平均 +0.057% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $120.34

## 4. Latest Market Context

- 更新: 2026-05-13T04:23:00.294242+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=81179.3
- Funnel: target 762 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +29.88% | $1,095,708.37 |
| IRYS/USDT:USDT | +27.51% | $3,554,360.95 |
| PEAQ/USDT:USDT | +19.41% | $2,479,888.34 |
| LAB/USDT:USDT | +15.94% | $104,642,663.28 |
| TIA/USDT:USDT | +15.10% | $30,285,344.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TROLLSOL/USDT:USDT | below_1h_threshold | +4.49% | +4.54% |
| BILL/USDT:USDT | below_1h_threshold | +2.95% | +2.99% |
| PEAQ/USDT:USDT | below_1h_threshold | +2.46% | +2.51% |
| VELO/USDT:USDT | below_1h_threshold | +2.22% | +2.27% |
| INJ/USDT:USDT | below_1h_threshold | +2.09% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
