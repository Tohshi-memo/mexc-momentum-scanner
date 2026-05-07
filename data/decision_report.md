# Decision Report

- generated_at: 2026-05-07T21:02:59.501030+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3697**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=3697, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/17 | 17.6% | +4.70% | **+0.83%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.86% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.41% | **+0.32%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.52% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.21% | **+2.21%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 69件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-07T21:02:56.844933+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=79787.0
- Funnel: target 765 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +36.98% | $6,305,437.84 |
| TST/USDT:USDT | +33.05% | $5,275,999.96 |
| NIL/USDT:USDT | +24.29% | $12,321,089.34 |
| NOT/USDT:USDT | +20.16% | $9,743,670.66 |
| IRENSTOCK/USDT:USDT | +18.51% | $3,456,422.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +1.25% | +1.31% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +0.84% | +0.90% |
| LAB/USDT:USDT | below_1h_threshold | +0.80% | +0.86% |
| DOGS/USDT:USDT | below_1h_threshold | +0.75% | +0.81% |
| USOIL/USDT:USDT | below_1h_threshold | +0.74% | +0.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
