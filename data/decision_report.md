# Decision Report

- generated_at: 2026-06-14T23:29:02.481085+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6711**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6711, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.56% | **+0.17%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +5.67% | **+1.70%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.50% | **+1.25%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.18% | **+1.20%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.12% | **+1.09%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.10% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.15** / 初期 $100.00 (+73.15%)
- 確定: 1584件 (Win 421 / Loss 498 / Flat 665) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $173.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.85** / 初期 $100.00 (-1.15%)
- 確定: 81件 (Win 21 / Loss 15 / Flat 45) / skip 41件
- 成長率目線: 平均log -0.000143 / 幾何平均 -0.014% per trade / maxDD +2.07%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0522 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $98.85

## 5. Latest Market Context

- 更新: 2026-06-14T23:28:57.334240+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.41% price=65654.9
- Funnel: target 770 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +47.18% | $5,265,844.34 |
| EVAA/USDT:USDT | +23.20% | $15,127,999.02 |
| BABY/USDT:USDT | +16.21% | $2,184,627.68 |
| RIF/USDT:USDT | +14.98% | $6,075,182.05 |
| EDEN/USDT:USDT | +13.99% | $1,324,282.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPG/USDT:USDT | below_1h_threshold | +2.88% | +2.47% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.00% | +1.59% |
| ADA/USDT:USDT | below_1h_threshold | +2.00% | +1.59% |
| AGI/USDT:USDT | below_1h_threshold | +1.95% | +1.54% |
| RIF/USDT:USDT | below_1h_threshold | +1.90% | +1.49% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
