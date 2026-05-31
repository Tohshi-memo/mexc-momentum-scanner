# Decision Report

- generated_at: 2026-05-31T23:00:01.579380+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5238**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5238, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.10% | **+1.09%** |
| LIMIT_BB3S | 5/12 | 41.7% | +2.27% | **+0.95%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.32% | **-0.16%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.22% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.19% | **+1.97%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +3.58% | **+1.79%** |
| ASK_LONG | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.90% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.46** / 初期 $100.00 (+33.46%)
- 確定: 873件 (Win 203 / Loss 259 / Flat 411) / skip 926件
- 成長率目線: 平均log +0.000331 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $133.46

## 4. Latest Market Context

- 更新: 2026-05-31T22:59:58.845931+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=73920.1
- Funnel: target 773 → liquid 131 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.5 >= 65=1, 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +108.39% | $16,805,220.08 |
| STG/USDT:USDT | +42.89% | $20,260,627.63 |
| H/USDT:USDT | +18.49% | $12,439,956.30 |
| HOME/USDT:USDT | +14.29% | $3,094,339.75 |
| ZORA/USDT:USDT | +12.18% | $1,625,923.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +3.49% | +3.41% |
| GRASS/USDT:USDT | below_1h_threshold | +3.44% | +3.36% |
| XLM/USDT:USDT | below_1h_threshold | +2.86% | +2.78% |
| ZEC/USDT:USDT | below_1h_threshold | +2.39% | +2.31% |
| NEX/USDT:USDT | below_1h_threshold | +2.27% | +2.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
