# Decision Report

- generated_at: 2026-06-07T03:38:48.507405+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5924**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=5924, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.25% | **+1.25%** |
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.25% | **+1.30%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.21% | **+0.81%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.26% | **+0.22%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$99.99** / 初期 $100.00 (-0.01%)
- 確定トレード: 3件 (TP 1 / SL 2 / EXP 0)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.39** / 初期 $100.00 (+37.39%)
- 確定: 1044件 (Win 251 / Loss 321 / Flat 472) / skip 1441件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $137.39

## 4. Latest Market Context

- 更新: 2026-06-07T03:38:46.549471+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=61553.4
- Funnel: target 771 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +40.95% | $64,764,533.25 |
| FIDA/USDT:USDT | +29.59% | $3,698,518.69 |
| BTW/USDT:USDT | +27.32% | $10,536,810.33 |
| BLESS/USDT:USDT | +20.22% | $4,313,291.83 |
| EDEN/USDT:USDT | +17.58% | $1,352,773.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.51% | +3.38% |
| H/USDT:USDT | below_1h_threshold | +2.50% | +2.37% |
| BTW/USDT:USDT | below_1h_threshold | +2.18% | +2.05% |
| BLESS/USDT:USDT | below_1h_threshold | +1.51% | +1.37% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.44% | +1.31% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
