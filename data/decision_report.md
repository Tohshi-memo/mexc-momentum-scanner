# Decision Report

- generated_at: 2026-05-15T15:38:23.556089+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4344**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.44% / filled 20/20。**
- 全期間 MARKET基準: n=4344, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.44% | **+1.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.54% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.20% | **+1.08%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.70% | **+0.49%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.19% | **+0.30%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.35% | **+0.19%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.69** / 初期 $100.00 (-2.31%)
- 確定トレード: 46件 (TP 12 / SL 31 / EXP 3)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 390件 (Win 97 / Loss 136 / Flat 157) / skip 515件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-15T15:38:20.152518+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=79106.7
- Funnel: target 764 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +24.52% | $6,194,719.52 |
| GWEI/USDT:USDT | +23.38% | $2,034,572.87 |
| IRYS/USDT:USDT | +20.92% | $10,580,582.33 |
| CGPT/USDT:USDT | +17.74% | $1,468,100.39 |
| PEAQ/USDT:USDT | +14.74% | $4,838,009.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +2.47% | +2.49% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +2.38% | +2.40% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +2.32% | +2.34% |
| FF/USDT:USDT | below_1h_threshold | +2.06% | +2.08% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.03% | +2.05% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
