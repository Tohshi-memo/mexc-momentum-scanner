# Decision Report

- generated_at: 2026-05-07T11:22:35.639667+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3620**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=3620, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.54% | **+1.47%** |
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| ASK | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.78% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.43% | **+1.36%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.17% | **+0.53%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.59% | **+0.44%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.44% | **+0.42%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.83** / 初期 $100.00 (+6.83%)
- 確定: 114件 (Win 37 / Loss 46 / Flat 31) / skip 67件
- 成長率目線: 平均log +0.000580 / 幾何平均 +0.058% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $106.83

## 4. Latest Market Context

- 更新: 2026-05-07T11:22:32.643060+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=80873.3
- Funnel: target 771 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +105.78% | $11,511,924.27 |
| SATO/USDT:USDT | +103.03% | $2,211,413.14 |
| PENGUIN/USDT:USDT | +86.05% | $3,563,326.01 |
| DOGS/USDT:USDT | +56.96% | $15,564,097.56 |
| NIL/USDT:USDT | +39.20% | $2,557,593.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +3.54% | +3.45% |
| ENA/USDT:USDT | below_1h_threshold | +3.27% | +3.18% |
| XPL/USDT:USDT | below_1h_threshold | +2.17% | +2.08% |
| ONDO/USDT:USDT | below_1h_threshold | +1.52% | +1.43% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.27% | +1.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
