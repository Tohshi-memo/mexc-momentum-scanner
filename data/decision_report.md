# Decision Report

- generated_at: 2026-07-16T11:06:26.163521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8803**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8803, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.27% | **-0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.40% | **+1.12%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.58% | **+0.87%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.28% | **+0.64%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.76% | **+0.45%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.89% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$106.87** / 初期 $100.00 (+6.87%)
- 確定トレード: 104件 (TP 38 / SL 64 / EXP 2)
- 最新: ROAM/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$338.75** / 初期 $100.00 (+238.75%)
- 確定: 2918件 (Win 911 / Loss 945 / Flat 1062) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $338.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.97** / 初期 $100.00 (+6.97%)
- 確定: 765件 (Win 176 / Loss 170 / Flat 419) / skip 1449件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0002 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $106.97

## 5. Causal Adaptive DryRun ($100)

- 残高: **$97.78** / 初期 $100.00 (-2.22%)
- 確定: 74件 (Win 21 / Loss 49 / Flat 4) / pending 3件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000354 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $97.78

## 6. Latest Market Context

- 更新: 2026-07-16T11:06:19.158587+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=64113.8
- Funnel: target 875 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +23.90% | $2,244,400.39 |
| AKE/USDT:USDT | +21.32% | $43,729,609.94 |
| ROAM/USDT:USDT | +18.15% | $5,952,427.39 |
| BANK/USDT:USDT | +16.83% | $3,045,262.66 |
| US/USDT:USDT | +13.95% | $16,200,710.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNHSTOCK/USDT:USDT | below_1h_threshold | +0.66% | +0.78% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.65% | +0.77% |
| RE/USDT:USDT | below_1h_threshold | +0.59% | +0.70% |
| AKE/USDT:USDT | below_1h_threshold | +0.46% | +0.57% |
| BASED/USDT:USDT | below_1h_threshold | +0.33% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
