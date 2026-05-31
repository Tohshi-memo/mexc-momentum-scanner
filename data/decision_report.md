# Decision Report

- generated_at: 2026-05-31T22:40:11.928639+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5235**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5235, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.38% | **+0.71%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.88% | **+0.49%** |
| LIMIT_BB3S | 7/14 | 50.0% | +0.91% | **+0.45%** |
| LIMIT_10PCT | 3/20 | 15.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.70% | **+2.02%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.08% | **+1.85%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.40% | **+1.70%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.13% | **+1.56%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.68% | **+1.52%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.13** / 初期 $100.00 (+34.13%)
- 確定: 870件 (Win 203 / Loss 258 / Flat 409) / skip 926件
- 成長率目線: 平均log +0.000338 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $134.13

## 4. Latest Market Context

- 更新: 2026-05-31T22:40:09.105007+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=73879.4
- Funnel: target 773 → liquid 131 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.9 >= 65=1, 4h RSI 74.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +83.26% | $15,477,774.22 |
| STG/USDT:USDT | +47.59% | $19,674,428.20 |
| HOME/USDT:USDT | +13.93% | $3,066,995.73 |
| BIANRENSHENG/USDT:USDT | +12.80% | $3,155,945.39 |
| H/USDT:USDT | +11.10% | $11,713,325.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +2.55% | +2.53% |
| LIT/USDT:USDT | below_1h_threshold | +2.17% | +2.15% |
| DYDX/USDT:USDT | below_1h_threshold | +2.00% | +1.98% |
| HYPE/USDT:USDT | below_1h_threshold | +1.71% | +1.68% |
| ZEC/USDT:USDT | below_1h_threshold | +1.50% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
