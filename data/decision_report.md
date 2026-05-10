# Decision Report

- generated_at: 2026-05-10T13:12:38.213391+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3964**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=3964, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.32% | **+0.32%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.33% | **+0.23%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.25% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +2.98% | **+1.79%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.67% | **+0.57%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.43% | **+0.39%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.58% | **+0.35%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.06% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 197件 (Win 48 / Loss 66 / Flat 83) / skip 328件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_5PCT_LONG` EXPIRED account +0.00% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T13:12:35.036448+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80857.1
- Funnel: target 769 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +61.80% | $2,183,517.99 |
| LAYER/USDT:USDT | +38.48% | $9,260,431.29 |
| GIGA/USDT:USDT | +21.53% | $1,223,288.13 |
| XEC/USDT:USDT | +19.97% | $3,231,564.73 |
| BAS/USDT:USDT | +17.59% | $1,217,195.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.72% | +2.76% |
| LAB/USDT:USDT | below_1h_threshold | +2.57% | +2.61% |
| LAYER/USDT:USDT | below_1h_threshold | +2.10% | +2.14% |
| UNI/USDT:USDT | below_1h_threshold | +2.06% | +2.10% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.55% | +1.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
