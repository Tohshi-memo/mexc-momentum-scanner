# Decision Report

- generated_at: 2026-07-02T03:11:48.149828+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8043**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=8043, expectancy=-0.03%
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
| ASK | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_6PCT | 6/20 | 30.0% | -1.02% | **-0.31%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.64% | **-0.33%** |
| LIMIT_9PCT | 4/20 | 20.0% | -1.85% | **-0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.33% | **+0.21%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +0.49% | **+0.10%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.09% | **+0.04%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +0.07% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$287.55** / 初期 $100.00 (+187.55%)
- 確定: 2440件 (Win 753 / Loss 813 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $287.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 545件 (Win 136 / Loss 131 / Flat 278) / skip 909件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T03:11:42.346808+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=60397.8
- Funnel: target 825 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +206.34% | $76,079,380.75 |
| TLM/USDT:USDT | +42.52% | $7,513,062.18 |
| RIF/USDT:USDT | +25.92% | $3,824,010.46 |
| SLX/USDT:USDT | +20.32% | $8,209,757.64 |
| BASED/USDT:USDT | +18.14% | $19,579,699.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.81% | +4.80% |
| LAB/USDT:USDT | below_1h_threshold | +4.43% | +4.42% |
| BASED/USDT:USDT | below_1h_threshold | +3.26% | +3.25% |
| M/USDT:USDT | below_1h_threshold | +2.41% | +2.40% |
| TLM/USDT:USDT | below_1h_threshold | +1.42% | +1.41% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
