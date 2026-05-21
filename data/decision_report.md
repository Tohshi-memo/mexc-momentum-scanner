# Decision Report

- generated_at: 2026-05-21T05:53:51.085638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4610**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=4610, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| ASK | 20/20 | 100.0% | +1.63% | **+1.63%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.35% | **+1.02%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.38% | **+0.97%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.87% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.23% | **+1.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.64% | **+0.74%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.04% | **-0.02%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.07% | **-0.03%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 545件 (Win 138 / Loss 185 / Flat 222) / skip 626件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T05:53:45.822271+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=77745.6
- Funnel: target 765 → liquid 132 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.1 >= 65=1, 4h RSI 70.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +46.00% | $1,790,796.16 |
| EDEN/USDT:USDT | +34.39% | $30,157,343.62 |
| SATO/USDT:USDT | +25.84% | $3,695,511.38 |
| USELESS/USDT:USDT | +20.05% | $1,253,442.72 |
| BSB/USDT:USDT | +17.68% | $63,110,716.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.88% | +4.19% |
| SPACE/USDT:USDT | below_1h_threshold | +1.25% | +1.57% |
| HYPE/USDT:USDT | below_1h_threshold | +0.57% | +0.89% |
| LIT/USDT:USDT | below_1h_threshold | +0.24% | +0.55% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.21% | +0.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
