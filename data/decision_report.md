# Decision Report

- generated_at: 2026-06-02T15:07:46.754064+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5459**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5459, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_BB3S | 4/17 | 23.5% | +2.64% | **+0.62%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.57% | **+0.51%** |
| LIMIT_2PCT | 15/20 | 75.0% | -0.10% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.15% | **+0.75%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.21% | **+0.15%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.10% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 87件 (TP 25 / SL 59 / EXP 3)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.70** / 初期 $100.00 (+33.70%)
- 確定: 971件 (Win 229 / Loss 295 / Flat 447) / skip 1049件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $133.70

## 4. Latest Market Context

- 更新: 2026-06-02T15:07:43.970958+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=67949.7
- Funnel: target 773 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +46.11% | $5,187,651.52 |
| USELESS/USDT:USDT | +31.56% | $4,269,194.45 |
| MRVLSTOCK/USDT:USDT | +28.92% | $9,219,692.12 |
| PIEVERSE/USDT:USDT | +25.26% | $4,731,662.92 |
| LAB/USDT:USDT | +24.43% | $173,218,411.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.99% | +3.05% |
| HOME/USDT:USDT | below_1h_threshold | +2.93% | +2.99% |
| US/USDT:USDT | below_1h_threshold | +1.52% | +1.58% |
| SLX/USDT:USDT | below_1h_threshold | +1.51% | +1.57% |
| USELESS/USDT:USDT | below_1h_threshold | +1.29% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
