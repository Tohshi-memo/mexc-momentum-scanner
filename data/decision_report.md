# Decision Report

- generated_at: 2026-05-27T22:29:37.255417+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4944**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=4944, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 12/20 | 60.0% | +3.30% | **+1.98%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.40% | **+1.92%** |
| LIMIT_4PCT | 10/20 | 50.0% | +2.87% | **+1.43%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.43% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +2.69% | **+1.61%** |
| LIMIT_10PCT_LONG | 8/20 | 40.0% | +3.64% | **+1.46%** |
| LIMIT_9PCT_LONG | 9/20 | 45.0% | +2.29% | **+1.03%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$97.15** / 初期 $100.00 (-2.85%)
- 確定トレード: 68件 (TP 19 / SL 46 / EXP 3)
- 最新: B/USDT:USDT TP_HIT PnL +6.46% 残高後 $97.15
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 821件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T22:29:35.128725+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=74584.1
- Funnel: target 771 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +32.81% | $5,626,184.08 |
| NBISSTOCK/USDT:USDT | +14.95% | $1,196,655.25 |
| RIVER/USDT:USDT | +6.29% | $12,098,240.33 |
| GENIUS/USDT:USDT | +5.27% | $1,293,164.41 |
| RKLBSTOCK/USDT:USDT | +3.55% | $1,987,067.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FET/USDT:USDT | below_1h_threshold | +2.89% | +2.69% |
| WLFI/USDT:USDT | below_1h_threshold | +0.86% | +0.66% |
| UB/USDT:USDT | below_1h_threshold | +0.83% | +0.63% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.80% | +0.61% |
| HIGH/USDT:USDT | below_1h_threshold | +0.80% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
