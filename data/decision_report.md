# Decision Report

- generated_at: 2026-06-23T02:40:22.776586+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7406**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7406, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.00% | **+0.00%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.37% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.04% | **+1.52%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$235.04** / 初期 $100.00 (+135.04%)
- 確定: 2062件 (Win 612 / Loss 678 / Flat 772) / skip 1905件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $235.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 313件 (Win 89 / Loss 87 / Flat 137) / skip 504件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0073 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-23T02:40:18.280715+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64159.5
- Funnel: target 808 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARX/USDT:USDT | +51.46% | $7,966,852.67 |
| CLO/USDT:USDT | +18.92% | $3,447,827.32 |
| FOLKS/USDT:USDT | +18.43% | $4,946,708.62 |
| LAB/USDT:USDT | +12.98% | $33,354,464.75 |
| FIDA/USDT:USDT | +10.28% | $1,180,124.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +4.97% | +4.92% |
| AERO/USDT:USDT | below_1h_threshold | +2.94% | +2.89% |
| MMT/USDT:USDT | below_1h_threshold | +2.62% | +2.57% |
| LAYER/USDT:USDT | below_1h_threshold | +1.95% | +1.90% |
| BSB/USDT:USDT | below_1h_threshold | +1.39% | +1.34% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
