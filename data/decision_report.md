# Decision Report

- generated_at: 2026-05-07T18:07:53.094131+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3675**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3675, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.07% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.46% | **+2.46%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.49% | **+2.44%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.62% | **+1.46%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +3.48% | **+1.39%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.17** / 初期 $100.00 (+11.17%)
- 確定: 169件 (Win 47 / Loss 57 / Flat 65) / skip 67件
- 成長率目線: 平均log +0.000627 / 幾何平均 +0.063% per trade / maxDD +2.62%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JTO/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $111.17

## 4. Latest Market Context

- 更新: 2026-05-07T18:07:49.605073+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=80120.0
- Funnel: target 767 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +31.52% | $1,344,807.13 |
| JTO/USDT:USDT | +27.61% | $12,759,603.25 |
| B/USDT:USDT | +13.39% | $4,667,456.06 |
| NIL/USDT:USDT | +12.17% | $7,237,132.65 |
| SATO/USDT:USDT | +11.15% | $5,834,686.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +2.42% | +2.33% |
| JTO/USDT:USDT | below_1h_threshold | +1.97% | +1.89% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.85% | +1.76% |
| BSB/USDT:USDT | below_1h_threshold | +1.68% | +1.60% |
| DYDX/USDT:USDT | below_1h_threshold | +1.39% | +1.30% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
