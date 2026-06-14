# Decision Report

- generated_at: 2026-06-14T22:18:28.597342+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6706**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=6706, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.99% | **+0.70%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.29% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.55% | **+1.15%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.70% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.74** / 初期 $100.00 (+72.74%)
- 確定: 1579件 (Win 420 / Loss 498 / Flat 661) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPG/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $172.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定: 76件 (Win 20 / Loss 15 / Flat 41) / skip 41件
- 成長率目線: 平均log -0.000172 / 幾何平均 -0.017% per trade / maxDD +2.07%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0481 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: OPG/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.70

## 5. Latest Market Context

- 更新: 2026-06-14T22:18:24.551271+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.47% price=64978.6
- Funnel: target 770 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +31.02% | $3,666,485.40 |
| EVAA/USDT:USDT | +22.83% | $13,242,818.33 |
| EDEN/USDT:USDT | +15.88% | $1,164,858.75 |
| RIF/USDT:USDT | +13.27% | $7,360,604.37 |
| BABY/USDT:USDT | +12.25% | $2,051,334.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MITO/USDT:USDT | below_1h_threshold | +2.13% | +2.60% |
| BABY/USDT:USDT | below_1h_threshold | +1.05% | +1.52% |
| EDEN/USDT:USDT | below_1h_threshold | +0.56% | +1.03% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.32% | +0.80% |
| RIVER/USDT:USDT | below_1h_threshold | +0.26% | +0.73% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
