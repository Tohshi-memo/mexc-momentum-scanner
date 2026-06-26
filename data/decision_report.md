# Decision Report

- generated_at: 2026-06-26T14:07:44.611538+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7634**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=7634, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| ASK | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_BB3S | 2/13 | 15.4% | +3.43% | **+0.53%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.35% | **+0.26%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| ASK_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.85% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$229.08** / 初期 $100.00 (+129.08%)
- 確定: 2159件 (Win 638 / Loss 715 / Flat 806) / skip 2036件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $229.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 382件 (Win 103 / Loss 100 / Flat 179) / skip 663件
- 成長率目線: 平均log +0.000192 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T14:07:38.922756+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=59887.8
- Funnel: target 806 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +61.82% | $5,345,600.42 |
| ICNT/USDT:USDT | +43.56% | $2,995,084.73 |
| VELVET/USDT:USDT | +24.83% | $8,095,605.42 |
| HEI/USDT:USDT | +20.91% | $9,063,250.66 |
| BEAT/USDT:USDT | +20.61% | $48,642,258.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +2.35% | +2.78% |
| BLESS/USDT:USDT | below_1h_threshold | +0.67% | +1.10% |
| JASMY/USDT:USDT | below_1h_threshold | +0.62% | +1.05% |
| ALLO/USDT:USDT | below_1h_threshold | +0.46% | +0.89% |
| JTO/USDT:USDT | below_1h_threshold | +0.43% | +0.87% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
