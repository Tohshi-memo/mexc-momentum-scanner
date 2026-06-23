# Decision Report

- generated_at: 2026-06-23T12:02:36.153870+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7422**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7422, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.85% | **-1.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/18 | 33.3% | +1.71% | **+0.57%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.56% | **+0.08%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.19% | **+1.53%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.87% | **+1.15%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.09% | **+1.04%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.93% | **+0.87%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.90% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.17** / 初期 $100.00 (+132.17%)
- 確定: 2078件 (Win 617 / Loss 687 / Flat 774) / skip 1905件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $232.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.59** / 初期 $100.00 (+6.59%)
- 確定: 314件 (Win 90 / Loss 87 / Flat 137) / skip 519件
- 成長率目線: 平均log +0.000203 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0199 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RESOLV/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $106.59

## 5. Latest Market Context

- 更新: 2026-06-23T12:02:31.605282+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=62502.7
- Funnel: target 802 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARX/USDT:USDT | +30.69% | $17,577,792.46 |
| RESOLV/USDT:USDT | +24.27% | $8,726,123.85 |
| BR/USDT:USDT | +19.06% | $1,445,951.14 |
| BTW/USDT:USDT | +13.17% | $19,986,968.46 |
| POPCAT/USDT:USDT | +12.21% | $1,717,389.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +1.15% | +1.11% |
| ALGO/USDT:USDT | below_1h_threshold | +0.54% | +0.51% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.47% | +0.43% |
| RE/USDT:USDT | below_1h_threshold | +0.43% | +0.40% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.38% | +0.34% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
