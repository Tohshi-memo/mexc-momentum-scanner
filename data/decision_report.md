# Decision Report

- generated_at: 2026-06-30T22:58:08.655345+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7932**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7932, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.89% | **+0.27%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.40% | **+0.16%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.11% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.41% | **+0.70%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.26% | **+0.10%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.03% | **+0.01%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.84** / 初期 $100.00 (+157.84%)
- 確定: 2355件 (Win 714 / Loss 786 / Flat 855) / skip 2138件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $257.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.52** / 初期 $100.00 (+6.52%)
- 確定: 474件 (Win 125 / Loss 121 / Flat 228) / skip 869件
- 成長率目線: 平均log +0.000133 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0353 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.52

## 5. Latest Market Context

- 更新: 2026-06-30T22:58:01.655126+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=58576.9
- Funnel: target 818 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +13.73% | $1,010,924.97 |
| BESTOCK/USDT:USDT | +12.60% | $1,107,342.79 |
| TAIKO/USDT:USDT | +12.14% | $1,187,889.49 |
| AIGENSYN/USDT:USDT | +11.80% | $15,408,018.26 |
| H/USDT:USDT | +8.44% | $11,976,295.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPG/USDT:USDT | below_1h_threshold | +3.57% | +3.63% |
| BASED/USDT:USDT | below_1h_threshold | +1.61% | +1.67% |
| EVAA/USDT:USDT | below_1h_threshold | +1.46% | +1.52% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.87% | +0.93% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.78% | +0.84% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
