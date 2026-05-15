# Decision Report

- generated_at: 2026-05-15T17:16:35.174534+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4345**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=4345, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.53% | **+0.48%** |
| LIMIT_BB3S | 8/14 | 57.1% | +0.77% | **+0.44%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.58% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.60% | **+0.30%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.19% | **+0.30%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.69** / 初期 $100.00 (-2.31%)
- 確定トレード: 46件 (TP 12 / SL 31 / EXP 3)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 390件 (Win 97 / Loss 136 / Flat 157) / skip 516件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-15T17:16:31.926804+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=79258.0
- Funnel: target 764 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +7.97% | $1,116,137.77 |
| CGPT/USDT:USDT | +4.90% | $1,727,371.98 |
| PNUT/USDT:USDT | +3.37% | $1,181,427.82 |
| GOAT/USDT:USDT | +3.13% | $1,409,466.68 |
| STAR/USDT:USDT | +3.12% | $1,041,147.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RUNE/USDT:USDT | below_1h_threshold | +1.89% | +1.89% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.88% | +1.89% |
| STAR/USDT:USDT | below_1h_threshold | +1.87% | +1.88% |
| SIREN/USDT:USDT | below_1h_threshold | +1.78% | +1.79% |
| GWEI/USDT:USDT | below_1h_threshold | +1.38% | +1.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
