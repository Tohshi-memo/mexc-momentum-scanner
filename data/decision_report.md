# Decision Report

- generated_at: 2026-06-15T00:42:54.940697+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6714**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6714, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.09% | **+0.27%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +6.81% | **+1.70%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.91% | **+1.05%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.49% | **+0.74%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.97% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.59** / 初期 $100.00 (+73.59%)
- 確定: 1587件 (Win 422 / Loss 498 / Flat 667) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.25% 残高後 $173.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.85** / 初期 $100.00 (-1.15%)
- 確定: 84件 (Win 21 / Loss 15 / Flat 48) / skip 41件
- 成長率目線: 平均log -0.000138 / 幾何平均 -0.014% per trade / maxDD +2.07%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0517 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.85

## 5. Latest Market Context

- 更新: 2026-06-15T00:42:48.152166+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=65490.0
- Funnel: target 770 → liquid 139 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +42.36% | $6,265,844.61 |
| EVAA/USDT:USDT | +24.61% | $16,259,348.85 |
| BABY/USDT:USDT | +16.99% | $2,324,609.82 |
| RIF/USDT:USDT | +16.49% | $5,588,227.84 |
| USELESS/USDT:USDT | +15.37% | $1,095,629.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IP/USDT:USDT | below_1h_threshold | +2.84% | +3.16% |
| SOXL/USDT:USDT | below_1h_threshold | +2.60% | +2.93% |
| EDEN/USDT:USDT | below_1h_threshold | +2.34% | +2.67% |
| BANANAS31/USDT:USDT | below_1h_threshold | +2.23% | +2.56% |
| BABY/USDT:USDT | below_1h_threshold | +1.69% | +2.02% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
