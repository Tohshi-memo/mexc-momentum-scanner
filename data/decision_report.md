# Decision Report

- generated_at: 2026-05-31T22:09:52.011296+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5230**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5230, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.20% | **+0.77%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_6PCT | 9/20 | 45.0% | +0.60% | **+0.27%** |
| LIMIT_BB3S | 11/17 | 64.7% | +0.07% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.53% | **+2.12%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.39% | **+1.92%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.62% | **+1.81%** |
| ASK_LONG | 20/20 | 100.0% | +1.67% | **+1.67%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.14** / 初期 $100.00 (+34.14%)
- 確定: 865件 (Win 202 / Loss 256 / Flat 407) / skip 926件
- 成長率目線: 平均log +0.000340 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $134.14

## 4. Latest Market Context

- 更新: 2026-05-31T22:09:48.963115+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=73743.7
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +84.10% | $14,106,149.31 |
| STG/USDT:USDT | +46.72% | $18,606,678.18 |
| HOME/USDT:USDT | +15.19% | $2,981,290.52 |
| ZORA/USDT:USDT | +13.85% | $1,545,150.17 |
| BIANRENSHENG/USDT:USDT | +13.18% | $3,092,387.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.08% | +4.24% |
| H/USDT:USDT | below_1h_threshold | +1.74% | +1.90% |
| USOIL/USDT:USDT | below_1h_threshold | +1.39% | +1.55% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +1.18% | +1.34% |
| LDO/USDT:USDT | below_1h_threshold | +1.02% | +1.17% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
