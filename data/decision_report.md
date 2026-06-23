# Decision Report

- generated_at: 2026-06-23T21:02:34.085944+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7443**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=7443, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.82% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.25% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.73% | **+0.58%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.73% | **+0.41%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.49% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$101.43** / 初期 $100.00 (+1.43%)
- 確定トレード: 30件 (TP 11 / SL 19 / EXP 0)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.43
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.71** / 初期 $100.00 (+128.71%)
- 確定: 2081件 (Win 617 / Loss 690 / Flat 774) / skip 1923件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $228.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 326件 (Win 92 / Loss 88 / Flat 146) / skip 528件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-23T21:02:29.411944+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62456.8
- Funnel: target 802 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +35.22% | $5,446,640.29 |
| BEAT/USDT:USDT | +29.10% | $36,883,392.34 |
| RAVE/USDT:USDT | +9.08% | $2,143,931.56 |
| ALLO/USDT:USDT | +6.87% | $4,676,870.55 |
| ESPORTS/USDT:USDT | +6.77% | $7,160,638.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +1.07% | +1.04% |
| DEXE/USDT:USDT | below_1h_threshold | +0.59% | +0.57% |
| XMR/USDT:USDT | below_1h_threshold | +0.51% | +0.49% |
| RIVER/USDT:USDT | below_1h_threshold | +0.49% | +0.46% |
| BASED/USDT:USDT | below_1h_threshold | +0.48% | +0.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
