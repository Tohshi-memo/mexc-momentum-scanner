# Decision Report

- generated_at: 2026-07-03T17:04:57.515947+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8177**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.39% / filled 20/20。**
- 全期間 MARKET基準: n=8177, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.39% | **+2.39%** |
| ASK | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.21% | **+0.84%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.70% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.36% | **+0.23%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.15% | **-0.07%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -1.05% | **-0.16%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.25% | **-0.17%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.61** / 初期 $100.00 (+2.61%)
- 確定トレード: 56件 (TP 20 / SL 35 / EXP 1)
- 最新: RIF/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$286.20** / 初期 $100.00 (+186.20%)
- 確定: 2496件 (Win 768 / Loss 833 / Flat 895) / skip 2242件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $286.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 977件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T17:04:51.570026+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=62141.6
- Funnel: target 834 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +22.37% | $8,313,369.55 |
| GUA/USDT:USDT | +12.85% | $5,883,008.35 |
| TLM/USDT:USDT | +7.13% | $16,922,607.33 |
| VELVET/USDT:USDT | +6.69% | $26,645,652.06 |
| BASED/USDT:USDT | +6.40% | $8,891,878.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TLM/USDT:USDT | below_1h_threshold | +4.85% | +4.75% |
| NEX/USDT:USDT | below_1h_threshold | +3.60% | +3.51% |
| VELVET/USDT:USDT | below_1h_threshold | +1.26% | +1.17% |
| BAS/USDT:USDT | below_1h_threshold | +1.16% | +1.07% |
| ZKP/USDT:USDT | below_1h_threshold | +1.16% | +1.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
