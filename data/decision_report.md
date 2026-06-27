# Decision Report

- generated_at: 2026-06-27T05:13:33.044223+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7671**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7671, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.23% | **-0.07%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.77% | **+1.52%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.25% | **+1.24%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.39% | **+0.98%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.43% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$236.94** / 初期 $100.00 (+136.94%)
- 確定: 2196件 (Win 658 / Loss 731 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $236.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.06** / 初期 $100.00 (+8.06%)
- 確定: 402件 (Win 109 / Loss 100 / Flat 193) / skip 680件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0631 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARX/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $108.06

## 5. Latest Market Context

- 更新: 2026-06-27T05:13:28.419412+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=60271.4
- Funnel: target 806 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +38.52% | $39,486,752.75 |
| MYX/USDT:USDT | +31.14% | $4,318,089.47 |
| PUNDIX/USDT:USDT | +28.29% | $5,607,923.19 |
| SYRUP/USDT:USDT | +16.08% | $1,142,015.81 |
| ARX/USDT:USDT | +15.62% | $2,750,389.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RE/USDT:USDT | below_1h_threshold | +2.98% | +2.89% |
| VELVET/USDT:USDT | below_1h_threshold | +2.10% | +2.01% |
| USELESS/USDT:USDT | below_1h_threshold | +2.02% | +1.93% |
| MYX/USDT:USDT | below_1h_threshold | +1.59% | +1.50% |
| ICNT/USDT:USDT | below_1h_threshold | +1.28% | +1.18% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
