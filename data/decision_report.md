# Decision Report

- generated_at: 2026-06-16T15:18:02.740705+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6869**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=6869, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.35% | **+0.35%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.20% | **+0.07%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +3.45% | **+2.87%** |
| ASK_LONG | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.54% | **+0.40%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.17% | **+0.11%** |
| MARKET_LONG | 20/20 | 100.0% | +0.09% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.06** / 初期 $100.00 (+84.06%)
- 確定: 1742件 (Win 457 / Loss 546 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000350 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARMSTOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $184.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 124件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0053 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T15:17:58.637768+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=65863.4
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +46.81% | $4,921,877.81 |
| BSB/USDT:USDT | +44.76% | $35,893,434.32 |
| PORTAL/USDT:USDT | +37.60% | $4,330,273.46 |
| LAB/USDT:USDT | +28.82% | $17,778,086.71 |
| ROAM/USDT:USDT | +22.15% | $6,407,089.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AERO/USDT:USDT | below_relative_strength | +5.05% | +4.70% |
| ROAM/USDT:USDT | below_1h_threshold | +2.61% | +2.25% |
| VELVET/USDT:USDT | below_1h_threshold | +2.49% | +2.14% |
| STG/USDT:USDT | below_1h_threshold | +2.37% | +2.01% |
| ROSE/USDT:USDT | below_1h_threshold | +1.91% | +1.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
