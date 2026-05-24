# Decision Report

- generated_at: 2026-05-24T15:30:11.686039+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4826**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4826, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.49% | **-1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.21% | **-0.12%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.45% | **+2.45%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.08% | **+2.00%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.19% | **+1.75%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.03% | **+1.51%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.92% | **+1.31%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.52** / 初期 $100.00 (+23.52%)
- 確定: 632件 (Win 156 / Loss 199 / Flat 277) / skip 755件
- 成長率目線: 平均log +0.000334 / 幾何平均 +0.033% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $123.52

## 4. Latest Market Context

- 更新: 2026-05-24T15:30:06.437678+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=76406.6
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +41.97% | $6,025,091.10 |
| NIL/USDT:USDT | +29.47% | $5,454,994.30 |
| FIDA/USDT:USDT | +21.59% | $3,464,652.13 |
| UB/USDT:USDT | +21.24% | $2,825,772.99 |
| PLUME/USDT:USDT | +15.54% | $2,818,489.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.07% | +3.09% |
| CHIP/USDT:USDT | below_1h_threshold | +2.24% | +2.27% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +1.75% | +1.77% |
| VVV/USDT:USDT | below_1h_threshold | +1.72% | +1.75% |
| LIT/USDT:USDT | below_1h_threshold | +1.36% | +1.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
