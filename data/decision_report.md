# Decision Report

- generated_at: 2026-07-01T13:06:06.755283+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7987**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.35% / filled 20/20。**
- 全期間 MARKET基準: n=7987, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| MARKET | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.44% | **+0.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.87% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +4.00% | **+1.40%** |
| MARKET_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |
| ASK_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.69% | **+0.41%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.59% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$264.10** / 初期 $100.00 (+164.10%)
- 確定: 2386件 (Win 724 / Loss 789 / Flat 873) / skip 2162件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: M/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $264.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.79** / 初期 $100.00 (+6.79%)
- 確定: 507件 (Win 129 / Loss 122 / Flat 256) / skip 891件
- 成長率目線: 平均log +0.000130 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0383 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: M/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.79

## 5. Latest Market Context

- 更新: 2026-07-01T13:06:00.758790+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=58636.8
- Funnel: target 825 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +108.71% | $13,301,774.35 |
| M/USDT:USDT | +44.79% | $6,482,626.36 |
| BAS/USDT:USDT | +38.81% | $2,860,914.48 |
| BASED/USDT:USDT | +27.32% | $13,109,616.35 |
| BTW/USDT:USDT | +22.73% | $6,667,099.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.89% | +2.65% |
| DYDX/USDT:USDT | below_1h_threshold | +2.36% | +2.12% |
| BASED/USDT:USDT | below_1h_threshold | +1.81% | +1.57% |
| RESOLV/USDT:USDT | below_1h_threshold | +1.58% | +1.34% |
| ZBT/USDT:USDT | below_1h_threshold | +1.54% | +1.30% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
