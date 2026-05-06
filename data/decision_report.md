# Decision Report

- generated_at: 2026-05-06T19:52:39.494456+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3496**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=3496, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.86% | **+0.77%** |
| ASK | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 4/14 | 28.6% | +1.81% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +7.12% | **+2.37%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.60% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$98.01** / 初期 $100.00 (-1.99%)
- 確定: 9件 (Win 0 / Loss 4 / Flat 5) / skip 48件
- 成長率目線: 平均log -0.002228 / 幾何平均 -0.223% per trade / maxDD +1.99%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $98.01

## 4. Latest Market Context

- 更新: 2026-05-06T19:52:36.866961+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=81458.5
- Funnel: target 765 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +46.27% | $8,870,221.81 |
| VVV/USDT:USDT | +7.94% | $5,667,486.71 |
| ZEREBRO/USDT:USDT | +7.86% | $1,132,855.38 |
| SMCISTOCK/USDT:USDT | +7.42% | $9,528,175.10 |
| ZRO/USDT:USDT | +6.55% | $3,302,577.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHZ/USDT:USDT | below_1h_threshold | +2.76% | +2.57% |
| UB/USDT:USDT | below_1h_threshold | +2.58% | +2.39% |
| PLAY/USDT:USDT | below_1h_threshold | +2.51% | +2.31% |
| VVV/USDT:USDT | below_1h_threshold | +1.99% | +1.80% |
| ORDI/USDT:USDT | below_1h_threshold | +1.80% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
