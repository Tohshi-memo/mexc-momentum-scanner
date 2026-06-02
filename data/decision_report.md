# Decision Report

- generated_at: 2026-06-02T15:02:18.839245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5458**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5458, expectancy=-0.04%
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
| LIMIT_BB3S | 4/16 | 25.0% | +2.64% | **+0.66%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.63% | **+0.57%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.60% | **+1.20%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.15% | **+0.75%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.73% | **+0.55%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.19% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 87件 (TP 25 / SL 59 / EXP 3)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.70** / 初期 $100.00 (+33.70%)
- 確定: 970件 (Win 229 / Loss 295 / Flat 446) / skip 1049件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $133.70

## 4. Latest Market Context

- 更新: 2026-06-02T15:02:15.994947+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=67887.3
- Funnel: target 773 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +44.04% | $5,150,015.92 |
| USELESS/USDT:USDT | +30.55% | $4,244,995.45 |
| MRVLSTOCK/USDT:USDT | +28.23% | $9,161,219.27 |
| CLO/USDT:USDT | +24.11% | $1,501,512.37 |
| PIEVERSE/USDT:USDT | +23.71% | $4,723,661.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.81% | +1.96% |
| EPIC/USDT:USDT | below_1h_threshold | +1.52% | +1.67% |
| SLX/USDT:USDT | below_1h_threshold | +1.27% | +1.42% |
| USELESS/USDT:USDT | below_1h_threshold | +0.50% | +0.66% |
| JTO/USDT:USDT | below_1h_threshold | +0.27% | +0.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
