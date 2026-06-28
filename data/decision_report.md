# Decision Report

- generated_at: 2026-06-28T22:41:44.341930+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7775**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.73% / filled 20/20。**
- 全期間 MARKET基準: n=7775, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.73% | **+2.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.73% | **+2.73%** |
| ASK | 20/20 | 100.0% | +2.69% | **+2.69%** |
| LIMIT_BB3S | 7/14 | 50.0% | +4.40% | **+2.20%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.99% | **+1.59%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.06% | **+1.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.46% | **+0.26%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.28% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.10** / 初期 $100.00 (+160.10%)
- 確定: 2279件 (Win 694 / Loss 761 / Flat 824) / skip 2057件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CELO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $260.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 731件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T22:41:39.621574+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=59176.2
- Funnel: target 805 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +13.90% | $2,592,701.37 |
| RAVE/USDT:USDT | +11.68% | $12,842,509.43 |
| BAS/USDT:USDT | +8.15% | $5,635,417.59 |
| MAGIC/USDT:USDT | +5.72% | $2,984,724.84 |
| BEAT/USDT:USDT | +5.65% | $32,696,459.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +3.58% | +3.99% |
| CELO/USDT:USDT | below_1h_threshold | +3.57% | +3.97% |
| ZRO/USDT:USDT | below_1h_threshold | +2.08% | +2.49% |
| SYN/USDT:USDT | below_1h_threshold | +1.81% | +2.22% |
| FET/USDT:USDT | below_1h_threshold | +1.38% | +1.79% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
