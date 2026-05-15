# Decision Report

- generated_at: 2026-05-15T02:23:21.351054+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4320**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.05% / filled 20/20。**
- 全期間 MARKET基準: n=4320, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+2.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.09% | **+2.09%** |
| MARKET | 20/20 | 100.0% | +2.05% | **+2.05%** |
| LIMIT_BB3S | 4/14 | 28.6% | +5.64% | **+1.61%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.40% | **+1.12%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.56% | **+1.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +2.72% | **+2.72%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.18% | **+0.65%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.65% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.02** / 初期 $100.00 (+21.02%)
- 確定: 372件 (Win 97 / Loss 130 / Flat 145) / skip 509件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEAQ/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $121.02

## 4. Latest Market Context

- 更新: 2026-05-15T02:23:17.772094+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=80928.9
- Funnel: target 763 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +27.29% | $2,361,171.94 |
| GWEI/USDT:USDT | +19.23% | $1,032,173.58 |
| UP/USDT:USDT | +18.62% | $3,822,924.48 |
| FIGSTOCK/USDT:USDT | +11.75% | $3,056,646.11 |
| TAC/USDT:USDT | +10.91% | $2,003,421.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +1.82% | +2.02% |
| LAB/USDT:USDT | below_1h_threshold | +1.46% | +1.66% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.36% | +1.57% |
| AIO/USDT:USDT | below_1h_threshold | +1.17% | +1.37% |
| ZBT/USDT:USDT | below_1h_threshold | +1.06% | +1.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
