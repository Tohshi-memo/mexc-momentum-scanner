# Decision Report

- generated_at: 2026-05-07T18:27:59.216154+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3678**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3678, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.69% | **-1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.13% | **+0.68%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.99% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.61% | **+2.53%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +4.94% | **+2.22%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.07% | **+1.87%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.46% | **+1.64%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.96% | **+1.47%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.17** / 初期 $100.00 (+11.17%)
- 確定: 172件 (Win 47 / Loss 57 / Flat 68) / skip 67件
- 成長率目線: 平均log +0.000616 / 幾何平均 +0.062% per trade / maxDD +2.62%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOGS/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $111.17

## 4. Latest Market Context

- 更新: 2026-05-07T18:27:55.749064+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=80119.9
- Funnel: target 767 → liquid 182 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.3 >= 65=1, 4h RSI 73.8 >= 65=1, 4h RSI 70.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +37.62% | $1,930,117.01 |
| JTO/USDT:USDT | +21.62% | $13,737,848.18 |
| NOT/USDT:USDT | +16.16% | $7,523,541.48 |
| SATO/USDT:USDT | +13.23% | $5,947,701.64 |
| DYDX/USDT:USDT | +12.59% | $6,620,033.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +4.95% | +4.87% |
| DYDX/USDT:USDT | below_1h_threshold | +4.16% | +4.08% |
| BSB/USDT:USDT | below_1h_threshold | +3.30% | +3.22% |
| DOGS/USDT:USDT | below_1h_threshold | +3.11% | +3.03% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.41% | +2.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
