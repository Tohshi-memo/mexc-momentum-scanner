# Decision Report

- generated_at: 2026-07-07T16:47:04.218715+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8446**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8446, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.78% | **+0.53%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_BB3S | 5/14 | 35.7% | -0.21% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.50% | **+0.98%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.08% | **+0.87%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.21% | **+0.79%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$100.55** / 初期 $100.00 (+0.55%)
- 確定トレード: 69件 (TP 23 / SL 45 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.55
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$322.09** / 初期 $100.00 (+222.09%)
- 確定: 2651件 (Win 845 / Loss 896 / Flat 910) / skip 2356件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $322.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 640件 (Win 152 / Loss 158 / Flat 330) / skip 1217件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0280 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T16:46:56.497775+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=63997.9
- Funnel: target 847 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.9 >= 65=1, 4h RSI 87.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +13.43% | $22,189,042.02 |
| EDGE/USDT:USDT | +11.48% | $8,862,857.00 |
| USELESS/USDT:USDT | +3.71% | $1,829,126.88 |
| VVV/USDT:USDT | +3.18% | $3,815,673.83 |
| SOXL/USDT:USDT | +3.16% | $18,402,047.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.74% | +3.61% |
| VVV/USDT:USDT | below_1h_threshold | +3.19% | +3.05% |
| SOXL/USDT:USDT | below_1h_threshold | +3.17% | +3.03% |
| UAI/USDT:USDT | below_1h_threshold | +2.92% | +2.78% |
| ZEC/USDT:USDT | below_1h_threshold | +2.62% | +2.48% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
